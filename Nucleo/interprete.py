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

import string

class Interprete:
	def __init__(self):
		pass

	def interpretar(self,sentencia):
		
		sentencias = self.corregir(sentencia)
		sentencias = string.split(sentencia, "#")
		
		
		for i in range(0,(len(sentencias))):
			sentencias[i] = sentencias[i][1:(len(sentencias[i])-1)]
			
		return (sentencias)

	def corregir(self,d):
		sdata = ""
		for i in range(0,len(d)-1):
			if (d[i] in string.printable):
				sdata = sdata+d[i]
		return (sdata)


	def codificar(self,comandos):
		sentencia_retorno = None

		for i in range(0,(len(comandos)-1)):
			comandos[i] = "[" + comandos[i] + "]"

		for i in range(1, len(comando)-2):
			comandos[i] = comandos[i]+"#"
			sentencia_retorno += comandos[i]

		return(sentencia_retorno)
