#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2
from datetime import date

class LineaFactura:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.subtotal = cantidad * precio

class MainHandler(webapp2.RequestHandler):
    def post(self):
        jinja = jinja2.get_jinja2(app=self.app)

        fecha = date.today()

        # Datos del emisor
        e_nombre = self.request.get("e_nombre")
        e_cif = self.request.get("e_cif")
        e_direccion = self.request.get("e_direccion")
        e_poblacion = self.request.get("e_poblacion")
        e_provincia = self.request.get("e_provincia")
        e_cp = self.request.get("e_cp")
        e_pais = self.request.get("e_pais")
        e_contacto = self.request.get("e_contacto")
        e_email = self.request.get("e_email")
        e_telefono = self.request.get("e_telefono")

        # Datos del cliente
        c_nombre = self.request.get("c_nombre")
        c_cif = self.request.get("c_cif")
        c_direccion = self.request.get("c_direccion")
        c_poblacion = self.request.get("c_poblacion")
        c_provincia = self.request.get("c_provincia")
        c_cp = self.request.get("c_cp")
        c_pais = self.request.get("c_pais")
        c_contacto = self.request.get("c_contacto")
        c_email = self.request.get("c_email")
        c_telefono = self.request.get("c_telefono")

        # Datos factura
        nombres = self.request.get_all("nombre")
        cantidades = self.request.get_all("cantidad")
        precios = self.request.get_all("precio")

        lineas_factura = []

        for i in range(len(precios)):
            lineas_factura.append(LineaFactura(nombres[i], int(cantidades[i]), float(precios[i])))

        total = 0
        for linea in lineas_factura:
            total += linea.subtotal

        valores = {
            "fecha": fecha,

            "e_nombre" : e_nombre,
            "e_cif": e_cif,
            "e_direccion": e_direccion,
            "e_poblacion": e_poblacion,
            "e_provincia": e_provincia,
            "e_cp": e_cp,
            "e_pais": e_pais,
            "e_contacto": e_contacto,
            "e_email": e_email,
            "e_telefono": e_telefono,

            "c_nombre": c_nombre,
            "c_cif": c_cif,
            "c_direccion": c_direccion,
            "c_poblacion": c_poblacion,
            "c_provincia": c_provincia,
            "c_cp": c_cp,
            "c_pais": c_pais,
            "c_contacto": c_contacto,
            "c_email": c_email,
            "c_telefono": c_telefono,

            "lineas_factura": lineas_factura,
            "total": total
        }

        self.response.write(jinja.render_template("factura.html", **valores))

app = webapp2.WSGIApplication([
    ('/factura', MainHandler)
], debug=True)
