from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'university.matiere'
    _description = 'Matiere enseigné dans une classe'

    Libellet_matiere = fields.Char(String='Libellet')
    code_matiere = fields.Char(String='code')
    classe_ids= fields.Many2many(comodel_name='university.classe' ,string='Classes')

    @api.multi
    def name_get(self):
        result = []
        for elt in self :
            name= '[ ' + elt.Libellet_matiere + ' ] '+ elt.code_matiere
            result.append((elt.id,name))
        return result
