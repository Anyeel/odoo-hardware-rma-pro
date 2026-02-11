from odoo import models, fields, api
from datetime import timedelta

class RMATicket(models.Model):
    _name = 'hardware.rma.ticket'
    _description = 'Ticket de Garantía y Reparación'
    _inherit = ['mail.thread', 'mail.activity.mixin'] # Esto añade el chat a la derecha

    # --- CAMPOS BÁSICOS ---
    name = fields.Char(string='Referencia', required=True, copy=False, readonly=True, default='Nuevo')
    subject = fields.Char(string='Asunto', required=True)
    description = fields.Text(string='Descripción del Problema')
    
    # --- RELACIONES (La potencia de Odoo) ---
    # Conectamos con la tabla de Clientes
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True, tracking=True)
    # Conectamos con la tabla de Productos
    product_id = fields.Many2one('product.product', string='Producto Afectado', required=True)
    
    # --- DATOS TÉCNICOS ---
    serial_number = fields.Char(string='Número de Serie (S/N)', tracking=True)
    purchase_date = fields.Date(string='Fecha de Compra')
    warranty_expired = fields.Boolean(string='Garantía Expirada', compute='_compute_warranty_status', store=True)

    # --- BARRA DE ESTADO (El proceso visual) ---
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
        ('diagnosis', 'En Diagnóstico'),
        ('repair', 'En Reparación'),
        ('done', 'Entregado'),
        ('cancel', 'Cancelado'),
    ], string='Estado', default='draft', tracking=True)

    # --- PRIORIDAD (Estrellas) ---
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Baja'),
        ('2', 'Alta'),
        ('3', 'Urgente'),
    ], string='Prioridad', default='0')

    # --- FLUJO DE TRABAJO (WORKFLOW) ---
    def action_confirm(self):
        """Pasa de Borrador a Confirmado"""
        self.state = 'confirmed'

    def action_start_diagnosis(self):
        """Empieza el diagnóstico"""
        self.state = 'diagnosis'

    def action_start_repair(self):
        """Empieza la reparación"""
        self.state = 'repair'

    def action_done(self):
        """Finaliza y BLOQUEA el ticket"""
        self.state = 'done'
        # Opcional: Aquí podrías añadir código para enviar un email automático al cliente
        
    def action_cancel(self):
        """Cancela el ticket"""
        self.state = 'cancel'

    def action_draft(self):
        """Devuelve a borrador si nos equivocamos"""
        self.state = 'draft'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Si el campo 'name' no existe o es 'Nuevo', pedimos un número a la secuencia
            if vals.get('name', 'Nuevo') == 'Nuevo':
                vals['name'] = self.env['ir.sequence'].next_by_code('hardware.rma.ticket') or 'Nuevo'
        
        # Llamamos al método original (super) para que guarde el registro en la base de datos
        return super().create(vals_list)
        
    # --- LÓGICA INTELIGENTE ---
    # Esto calcula automáticamente si la garantía vale o no
    @api.depends('purchase_date')
    def _compute_warranty_status(self):
        for record in self:
            if record.purchase_date:
                # Suponemos 2 años de garantía europea (730 días)
                expiration_date = record.purchase_date + timedelta(days=730)
                if expiration_date < fields.Date.today():
                    record.warranty_expired = True
                else:
                    record.warranty_expired = False
            else:
                record.warranty_expired = False