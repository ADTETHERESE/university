from odoo import fields, models, api


class UniversityClasse(models.Model):
    _name = 'university.classe'

    _rec_name='code'
    libellet = fields.Char(string='Libellet')
    code = fields.Char(string='Code')
    student_ids=fields.One2many(comodel_name="university.student",inverse_name='classe_id')
    female_student_ids = fields.One2many(
        comodel_name='university.student',
        inverse_name='classe_id',
        compute='check_female_student',
        required=False)
    effectif = fields.Integer(string='Effectif', compute='check_number_students')
    matiere_ids = fields.Many2many(comodel_name='university.matiere',related='')


    @api.multi
    def check_number_students(self):
        self.effectif = len(self.student_ids)

    @api.multi
    def check_female_student(self):
        student_list=self.env['university.student'].search([('nom','!=',False)])
        for elt in self:
            for stud in student_list:
                if stud.sexe != 'm' :
                    elt.female_student_ids += stud