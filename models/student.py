# -*- coding: utf-8 -*-

from odoo import models, fields, api


class university(models.Model):
    _name = 'university.student'
    _inherit = 'mail.thread'
    nom = fields.Char(string="Nom ", requited=True)
    prenom = fields.Char(string='Prenom')
    sexe = fields.Selection(
        string='Sexe',
        selection=[('m', 'Masculin'),
                   ('f', 'Female'), ],
        required=True, )
    classe_id = fields.Many2one(
        comodel_name='university.classe',
        string='Classe',
        required=True)
    date_naiss = fields.Date(string='Date de Naissance', required=True)
    matiere_ids = fields.Many2many(comodel_name='university.matiere', related='classe_id.matiere_ids')

    @api.multi

    def name_get(self):
        # value = fields.Integer()
        result = []
        # value2 = fields.Float(compute="_value_pc", store=True)
        for elt in self:
            name= '[ ' +elt.classe_id.code +' ] '+elt.nom +' '+ elt.prenom
            result.append((elt.id,name))
        return result
#         self.value2 = float(self.value) / 100
