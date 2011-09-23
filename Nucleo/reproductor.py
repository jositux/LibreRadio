#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Nucleo.py
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


import sys, os, thread, time
import gobject
import gstreamer
import gst
import comunicador
import interprete
import manipulador

class Player:
	
	def __init__(self):
		self.player = gstreamer.GStreamer()

		self.dur_str = ""
		self.pos_str = ""
		self.comunicador_interno = None

		self.volumen_def = 1
		self.pisador_thread = None
		self.reproductor_tread = None

		# Implementaciones para Mixer, fader y reproductores para mezcla
		self.encolado = []
		self.reproductor_encolado_thread = None
		



	def reproducir(self, path_audio_ext):
		self.dur_str = ""
		self.pos_str = ""
		path_audio_ext = (path_audio_ext,)
		self.reproductor_tread = thread.start_new_thread(self.reproducir_thread, path_audio_ext)


	def cargar(self, path_archivo):
		self.encolado.append(path_archivo)

		
	def reproducir_thread(self, path_audio):
		if self.reproductor_encolado_thread == None:
			try:
				self.player.launch(path_audio)
				self.play_thread_id = thread.start_new_thread(self.play_thread, ())
			except:
				self.get_comunicador().terminado()
		else:
			print "Reproduciendo Cola de archivos"
			self.cargar(path_audio)
			self.get_comunicador().advertencia(1)
			
	def play_thread(self):
		play_thread_id = self.play_thread_id
		
		while play_thread_id == self.play_thread_id:
			try:
				time.sleep(0.2)
				dur_int = self.player.getplayer().query_duration(gst.FORMAT_TIME, None)[0]
				if dur_int == -1:
					continue
				dur_str = self.convert_ns(dur_int)
				break
			except:
				pass
				
		time.sleep(0.2)
		
		while play_thread_id == self.play_thread_id:
			try:
				pos_int = (self.player.getplayer()).query_position(gst.FORMAT_TIME)[0]
				pos_viejo = pos_int
				pos_str = self.convert_ns(pos_int)
				self.pos_str = str(pos_str)
				self.dur_str = str(dur_str)
				time.sleep(0.1)
				pos_int = (self.player.getplayer()).query_position(gst.FORMAT_TIME)[0]

				if play_thread_id == self.play_thread_id:
					
					if pos_int == pos_viejo:
						self.player.stop()
						self.play_thread_id = None
						self.get_comunicador().terminado()
						pos_str = ""
						print "Terminado"
				time.sleep(1)

			except:
				pass


	

			
			
	def convert_ns(self, t):
		# This method was submitted by Sam Mason.
		# It's much shorter than the original one.

		try:
			s,ns = divmod(t, 1000000000)
			m,s = divmod(s, 60)

			if m < 60:
				return "%02i:%02i" %(m,s)
			else:
				h,m = divmod(m, 60)
				return "%i:%02i:%02i" %(h,m,s)
		except:
			print "Problemas en la función"
			self.get_comunicador.error()

	def get_tiempo(self):
		try:
			self.get_comunicador().posicion(self.pos_str,self.dur_str)
		except:
			print "Sin comunicador de datos"



	def parar(self):
		try:
			self.player.stop()
			self.pos_str = ""
			self.dur_str = ""
		except:
			print "Problemas con el manejador GSTreamer"
			self.get_comunicador().error()

		self.play_thread_id = None
		

	def get_comunicador(self):
		try:
			return(self.comunicador_interno)
		except:
			print "Sin comunicador de datos"
			return (None)

	def set_comunicador(self,comunicador_interno_ext):
		self.comunicador_interno = comunicador_interno_ext


	def volumen(self, nivel_volumen):

		try:
			nivel_volumen = float(nivel_volumen)
			self.volumen_def = nivel_volumen
			self.player.volumen(nivel_volumen)
			print "- ------|- + "+str(self.volumen_def)
			
		except:
			print "Error al asignar volumen, valor erroneo"
			self.get_comunicador().error()


	def reproducir_cola_thread(self):
		self.reproductor_encolado_thread = thread.start_new_thread(self.reproducir_cola, ())
	
	def pisar_thread(self):
		if self.pisador_thread == None:
			self.pisador_thread = thread.start_new_thread(self.pisar, ())
		else:
			print "El pisador esta implementandose en este momento"

	def elevar_thread(self):
		if self.pisador_thread == None:
			self.pisador_thread = thread.start_new_thread(self.elevar, ())
		else:
			print "El pisador esta implementandose en este momento"


	def pisar(self):
		for i in range(1, 10):
			if self.volumen_def > 0.1:
				self.volumen_def = self.volumen_def - 0.09
				print "Pisador ->" + str(self.volumen_def)
				self.volumen(self.volumen_def)
				time.sleep(0.1)
			else:
				print "Mínimo volumen alcanzado, MCR 01"
				break
		self.pisador_thread = None
			

	def elevar(self):
		for i in range(1, 10):
			if self.volumen_def < 1:
				self.volumen_def = self.volumen_def + 0.09
				print "Pisador ->" + str(self.volumen_def)
				self.volumen(self.volumen_def)
				time.sleep(0.1)
			else:
				print "Maximo volumen alcanzado, MCA 01"
				break
		self.pisador_thread = None


		
	def reproducir_cola(self):
		if (len(self.encolado) > 0):
			for i in range(0, len(self.encolado)-1):
				reproducir(self.encolado[i])
				time.sleep(0.1)
				while (self.reproducir_thread != None) :
					time.sleep(0.2)
				self.encolado.remove(i)
			self.reproductor_encolado_thread = None
		else:
			self.get_comunicador.advertencia(2)
			print "Cola vacia"







		
		
# Main Loop!

if len(sys.argv) > 1:
	
	# Definimos los componentes
	reproductor = Player()
	reproductorMixer = Player()
	pasarela_principal = comunicador.Comunicador()
	pasarela_principal.conectar(sys.argv[1])
	interprete_principal = interprete.Interprete()

	reproductor.set_comunicador(pasarela_principal)


	# Pasamos el control al Manipulador Principal
	manipulador_principal = manipulador.Manipulador()
	manipulador_principal.set_reproductor(reproductor)
	manipulador_principal.set_interprete(interprete_principal)
	manipulador_principal.set_comunicador(pasarela_principal)


	while True:
		datas = (pasarela_principal.recibir(2048))
		try:
			ldata = len(datas)
			if ldata < 2:
				pass
				exit()
			else:
				comandos = interprete_principal.interpretar(datas)
				print comandos
				manipulador_principal.analizar(comandos)
				print "DEBUG::: "+str(len(datas))
			
		except:
			print "Oups! Tenemos un error al recibir datos del comunicador.\n El nucleo necesita un comunicador para recibir comandos y enviar datos."
			exit()
else:
	print "Oups! \n El nucleo necesita un comunicador para recibir comandos y enviar datos."
