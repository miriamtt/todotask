from odoo import fields, models


class TodoTaskStage(models.Model):
    """Model for claim stages. This models the main stages of a claim
    management flow. Main CRM objects (leads, opportunities, project
    issues, ...) will now use only stages, instead of state and stages.
    Stages are for example used to display the kanban view of records.
    """

    _name = "todo.task.stage"
    _description = "Estado de reclamación"
    _order = "sequence"

    name = fields.Char(string="Nombre estado", required=True)
    
    sequence = fields.Integer(default=1, help="Used to order stages.")
    user_id = fields.Many2one(comodel_name="res.users", string="User", readonly=True)
    team_id = fields.Many2one(comodel_name="todo.task", string="Team", readonly=True)
    
    company_id = fields.Many2one(   
        comodel_name="res.company", string="Company", readonly=True
    )
    name = fields.Char(string="Stage Name", required=True, translate=True)
    sequence = fields.Integer(default=1, help="Used to order stages. Lower is better.")
    team_ids = fields.Many2many(
        comodel_name="crm.team",
        relation="crm_team_claim_stage_rel2",
        column1="stage_id",
        column2="team_id",
        string="Teams",
        help="Link between stages and sales teams. When set, this limitate "
        "the current stage to the selected sales teams.",
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Partner", readonly=True
    )
    stage_id = fields.Many2one(
        comodel_name="todo.task.stage",
        string="Stage",
        readonly=True,
        domain="[('team_ids','=',team_id)]",
    )
    categ_id = fields.Many2one(
        comodel_name="todo.task.category", string="Category", readonly=True
    )
    priority = fields.Selection(
        selection=[("0", "Low"), ("1", "Normal"), ("2", "High")]
    )
    type_action = fields.Selection(
        selection=[
            ("correction", "Corrective Action"),
            ("prevention", "Preventive Action"),
        ],
        string="Action Type",
    )
    claim_date = fields.Datetime(readonly=True)

    date_closed = fields.Datetime(string="Close Date", readonly=True, index=True)
    date_deadline = fields.Date(string="Deadline", readonly=True, index=True)
    case_default = fields.Boolean(
        string="Common to All Teams",
        help="If you check this field, this stage will be proposed by default "
        "on each sales team. It will not assign this stage to existing "
        "teams.",
    )