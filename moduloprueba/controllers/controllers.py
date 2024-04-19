# -*- coding: utf-8 -*-
from odoo import http
from odoo import models
import json
import ast


class ModuloPrueba(http.Controller):

    @http.route('/api/hello', auth='none', type='json', methods=['POST'])
    def myrequest_api(self, **kwargs):
        http_request = http.request.httprequest.data.decode('utf-8')
        datos_recibidos = json.loads(http_request)

        if not datos_recibidos:
            return {"No se recibieron datos JSON"}

        oblig = ['id', 'partner_id', 'responsible']

        for campo in oblig:
            if campo not in datos_recibidos:
                print("Formato incorrecto, ausencia de campos obligatorios")

        todotask = http.request.env['todo.task'].sudo().create(datos_recibidos)

        return {"success": "Registro de reclamación creado con éxito!"}