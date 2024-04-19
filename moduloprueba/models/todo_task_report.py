# -*- coding: utf-8 -*-

from odoo import models, fields

class TodoTaskReport(models.Model):
    _name = "todo.task.report"
    _description = "Todo Task Report"
    _auto = False
    _inherit = 'crm.claim.report'


    stage_id = fields.Many2one(
        comodel_name="todo.task.stage",
        string="Stage",
        readonly=True,
        domain="[('team_ids','=',team_id)]",
    )
    categ_id = fields.Many2one(
        comodel_name="todo.task.category", string="Category", readonly=True
    )

    def _select(self):
        select_str = """
            SELECT
            min(c.id) AS id,
            c.date AS claim_date,
            c.date_closed AS date_closed,
            c.date_deadline AS date_deadline,
            c.user_id,
            c.stage_id,
            c.team_id,
            c.partner_id,
            c.company_id,
            c.categ_id,
            c.name AS subject,
            count(*) AS nbr_claims,
            c.priority AS priority,
            c.type_action AS type_action,
            c.create_date AS create_date,
            avg(extract(
                'epoch' FROM (
                    c.date_closed-c.create_date)))/(3600*24)
                    AS delay_close,
            (
                SELECT count(id)
                FROM mail_message
                WHERE model='todo.task'
                AND res_id=c.id) AS email,
            extract(
                'epoch' FROM (
                    c.date_deadline - c.date_closed))/(3600*24)
                    AS delay_expected
        """
        return select_str

    
    def _from(self):
        from_str = """
            todo_task c
        """
        return from_str
