#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       comunicador.py
#       
#       Copyright 2011 José Pezzarini <jose2190@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import socket

class Comunicador:

	def __init__(self):
		self.comunicador = socket.socket(1,1)
		self.path_server = None
		self.pasarela_datos = None

	def conectar(self, path_server_ext):
		self.path_server = path_server_ext
		try:
			self.comunicador.connect(self.path_server)
			self.pasarela_datos = self.comunicador
		except:
			print "Error al conectar comunicador de datos, problemas con socket"

	def error(self):
		self.pasarela_datos.send("[error]#[1]")

	

	def estado(self, estado_reproducion):
		try:
			self.pasarela_datos.send("[estado]#[" + estado_reproducion + "]")
		except:
			print "Error en pasarela de datos"


	def terminado(self):
		try:
			self.pasarela_datos.send("[estado]#[0]")
		except:
			print "Error en pasarela de datos, funcion "


	def posicion(self, estado_posicion, estado_total):
		try:
			self.pasarela_datos.send("[posicion]#[" + str(estado_posicion) + "]#[" + str(estado_total) + "]")
		except:
			print "Error en pasarela de datos"


	def recibir(self, buffer_datos):
		try:
			return(self.pasarela_datos.recv(buffer_datos))
		except:
			print "Error al recibir datos en comunicador de datos"

	def advertencia(self, cod_advertencia):
		if cod_advertencia == 1:
			self.pasarela_datos.send("[advertencia]#[rep_cola]")
		else:
			pass
