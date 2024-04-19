# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = 'crm.claim' 
    is_done = fields.Boolean(string='Done')
    active = fields.Boolean(string='Active', default=True)

    # name = fields.Char(string='Name', required=True)
    
    @api.depends
    def act_do_toggle_done(self):
        if self.user_id != self.env.user:
            raise Exception('Only the responsible can do this!')
        else:
            return super(TodoTask, self).do_toggle_done()
    
    @api.depends
    def act_do_clear_done(self):
        domain = [('is_done', '=', 'True'), '|', ('user_id','=', self.env.uid), ('user_id','=', False)]
        done_resc = self.search(domain)
        done_resc.write({'active': False})
        return True
    
    @api.model
    def _get_default_stage_id(self):
        """Gives default stage_id"""
        team_id = self.env["crm.team"]._get_default_team_id()
        return self.stage_find(team_id.id, [("sequence", "=", "1")])

    @api.model
    def _get_default_team(self):
        return self.env["crm.team"]._get_default_team_id()

    
    name = fields.Char(string="Information Claim", required=True)
    date_start = fields.Date(string="Start Done")
    date_stop = fields.Date(string="Stop Date")
    date_delay = fields.Integer(string="Delay (Days)")
    categ_id = fields.Many2one(comodel_name="todo.task.category", string="Category")
    stage_id = fields.Many2one(
        comodel_name="todo.task.stage",
        string="Stage",
        tracking=3,
        default=_get_default_stage_id,
        domain="['|', ('team_ids', '=', team_id), ('case_default', '=', True)]",
    )
    team_id = fields.Many2one(
        comodel_name="crm.team",
        string="Sales Team",
        index=True,
        default=_get_default_team,
        help="Responsible sales team. Define Responsible user and Email "
        "account for mail gateway.",
    )
    possible_solution = fields.Char(string="Possible solution")
    time_difference = fields.Integer(stierng="Time difference", readonly=True)
    partner_id = fields.Many2one(comodel_name="res.partner", string="Partner")


    