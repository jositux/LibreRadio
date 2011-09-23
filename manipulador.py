#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       manipulador.py
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
import string

class Manipulador:
	# Instancia mínima -> {Comunicador: Class Comunicador}
	
	def __init__(self):

		self.reproductor_principal = None
		self.comunicador_principal = None
		self.interprete_principal = None

		
		# Implementaciones para Mixer, fader
		self.reproductor_secundario = None
		self.comunicador_secundario = None
		self.interprete_secundario = None

		# Implementaciones para Horarias
		self.reproductor_horarias = None
		self.interprete_horarias = None
		self.comunicador_horarias = None
		
		

	def set_comunicador(self, comunicador_ext):
		self.comunicador_principal = comunicador_ext

	def set_reproductor(self, reproductor_ext):
		self.reproductor_principal = reproductor_ext

	def set_interprete(self, interprete_ext):
		self.interprete_principal = interprete_ext

	def set_comunicador_horarias(self,comunicador_ext):
		self.inter

	def get_comunicador(self):
		return (self.comunicador_principal)

	def get_reproductor(self):
		return (self.reproductor_principal)

	def get_reproductor_secundario(self):
		return (self.reproductor_secundario)

	def get_interprete(self):
		return (self.interprete_principal)




	def interact_nucleo(self, identificador_accion):
		if identificador_accion == 0:
			self.get_comunicador().estado(0)


	def analizar(self,comandos_ext):
		if len(comandos_ext) > 1:

			if (unicode("stop","utf-8") in comandos_ext[0]):
				self.get_reproductor().parar()
				#self.get_comunicador().estado(0)

			if (unicode("reproducir","utf-8") in comandos_ext[0]):
				self.get_reproductor().reproducir(comandos_ext[1])

			if (unicode("posicion","utf-8") in comandos_ext[0]):
				self.get_reproductor().get_tiempo()

			if (unicode("volumen","utf-8") in comandos_ext[0]):
				try:
					self.get_reproductor().volumen(float(comandos_ext[1])/10)
				except:
					pass

			if (unicode("pisar", "utf-8") in comandos_ext[0]):
				self.get_reproductor().pisar_thread()

			if (unicode("elevar", "utf-8") in comandos_ext[0]):
				self.get_reproductor().elevar_thread()

			if (unicode("cargar", "utf-8") in comandos_ext[0]):
				self.get_reproductor().cargar(comandos[1])

				



