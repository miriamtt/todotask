# -*- coding: utf-8 -*-


from odoo import api, fields, models

class TodoTaskContacts(models.Model):
    _inherit = "res.partner"

    todotask_count = fields.Integer(string="# Reclamaciones", compute="_compute_todotask_count")
    todotask_ids = fields.One2many(comodel_name="todo.task", inverse_name="partner_id")
    
    @api.depends("todotask_ids", "child_ids", "child_ids.todotask_ids")
    def _compute_todotask_count(self):
        partners = self | self.mapped("child_ids")
        partner_data = self.env["todo.task"].read_group(
            [("partner_id", "in", partners.ids)], ["partner_id"], ["partner_id"]
        )
        mapped_data = {m["partner_id"][0]: m["partner_id_count"] for m in partner_data}
        for partner in self:
            partner.todotask_count = mapped_data.get(partner.id, 0)
            for child in partner.child_ids:
                partner.todotask_count += mapped_data.get(child.id, 0)
                



