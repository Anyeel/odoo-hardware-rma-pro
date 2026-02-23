import re
from odoo import models, fields, api

class PCBuild(models.Model):
    _name = 'pc.build'
    _description = 'Configuración de PC a medida'

    name = fields.Char(string='Referencia del PC', required=True, copy=False, default='Nuevo PC')
    client_id = fields.Many2one('res.partner', string='Cliente')
    
    # 1. Los Componentes
    cpu_id = fields.Many2one('product.product', string='Procesador (CPU)', domain="[('categ_id.name', '=', 'Procesadores')]")
    motherboard_id = fields.Many2one('product.product', string='Placa Base', domain="[('categ_id.name', '=', 'Placas Base')]")
    ram_id = fields.Many2one('product.product', string='Memoria RAM', domain="[('categ_id.name', '=', 'Memoria RAM')]")
    gpu_id = fields.Many2one('product.product', string='Tarjeta Gráfica (GPU)', domain="[('categ_id.name', '=', 'Tarjetas Gráficas (GPU)')]")
    storage_id = fields.Many2one('product.product', string='Almacenamiento', domain="[('categ_id.name', '=', 'Almacenamiento')]")
    case_id = fields.Many2one('product.product', string='Torre / Caja', domain="[('categ_id.name', '=', 'Torres / Cajas')]")
    psu_id = fields.Many2one('product.product', string='Fuente de Alimentación', domain="[('categ_id.name', '=', 'Fuentes de Alimentación')]")
    
    total_price = fields.Float(string='Precio Total', compute='_compute_total_price', store=True)

    @api.depends('cpu_id', 'motherboard_id', 'ram_id', 'gpu_id', 'storage_id', 'case_id', 'psu_id')
    def _compute_total_price(self):
        for build in self:
            price = sum([
                build.cpu_id.lst_price if build.cpu_id else 0.0,
                build.motherboard_id.lst_price if build.motherboard_id else 0.0,
                build.ram_id.lst_price if build.ram_id else 0.0,
                build.gpu_id.lst_price if build.gpu_id else 0.0,
                build.storage_id.lst_price if build.storage_id else 0.0,
                build.case_id.lst_price if build.case_id else 0.0,
                build.psu_id.lst_price if build.psu_id else 0.0,
            ])
            build.total_price = price

    # --- HELPER: Función para extraer atributos fácilmente ---
    def _get_attr_value(self, product, keyword):
        """Busca en el producto un atributo que contenga la palabra clave (ej. 'RAM' o 'POTENCIA')"""
        if not product:
            return False
        for line in product.product_tmpl_id.attribute_line_ids:
            if keyword in line.attribute_id.name.upper():
                if line.value_ids:
                    return line.value_ids[0].name.upper()
        return False

    # --- MOTOR DE REGLAS DE COMPATIBILIDAD ---
    @api.onchange('cpu_id', 'motherboard_id', 'ram_id', 'gpu_id', 'psu_id')
    def _check_compatibility(self):
        errores = []

        # 1. REGLA DEL SOCKET (CPU vs Placa Base)
        cpu_sock = self._get_attr_value(self.cpu_id, 'SOCKET')
        mobo_sock = self._get_attr_value(self.motherboard_id, 'SOCKET')
        
        if cpu_sock and mobo_sock and cpu_sock != mobo_sock:
            self.motherboard_id = False  # Vaciamos el campo erróneo
            errores.append(f"🔌 SOCKET: El procesador es {cpu_sock} pero la Placa Base es {mobo_sock}.")

        # 2. REGLA DE LA MEMORIA (Placa Base vs RAM)
        mobo_ram = self._get_attr_value(self.motherboard_id, 'RAM')
        ram_type = self._get_attr_value(self.ram_id, 'RAM')

        if mobo_ram and ram_type and mobo_ram != ram_type:
            self.ram_id = False
            errores.append(f"🧠 MEMORIA: La Placa Base solo soporta {mobo_ram}, pero has seleccionado memoria {ram_type}.")

        # 3. REGLA DE ENERGÍA (Tarjeta Gráfica vs Fuente)
        gpu_w_str = self._get_attr_value(self.gpu_id, 'POTENCIA')
        psu_w_str = self._get_attr_value(self.psu_id, 'POTENCIA')

        if gpu_w_str and psu_w_str:
            # Magia Pura: Extraemos solo los números de textos como "750W" o "750 W"
            gpu_w = int(re.sub(r'\D', '', gpu_w_str) or 0)
            psu_w = int(re.sub(r'\D', '', psu_w_str) or 0)

            if psu_w > 0 and gpu_w > 0 and psu_w < gpu_w:
                self.psu_id = False
                errores.append(f"⚡ ENERGÍA: La RTX exige {gpu_w}W, pero tu fuente solo da {psu_w}W. ¡El PC se apagará jugando!")

        # Si el array de errores tiene algo, disparamos la alerta general
        if errores:
            mensaje_completo = "\n\n".join(errores)
            return {
                'warning': {
                    'title': "⚠️ CONFLICTOS DE HARDWARE DETECTADOS",
                    'message': mensaje_completo
                }
            }