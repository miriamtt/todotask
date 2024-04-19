from odoo import models, fields


class TodoTaskCategory(models.Model):
    _name = "todo.task.category"
    _description = "Todo Task Category"

    name = fields.Char(string='Name', required=True)
    team_id = fields.Many2one(comodel_name="crm.team", string="Sales Team")
    
