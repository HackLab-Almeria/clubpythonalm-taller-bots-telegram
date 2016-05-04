#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: 08 - Conociendo el API
 	Libreria: pyTelegramBotAPI 1.4.2 [ok]
 	Libreria: pyTelegramBotAPI 2.0 [ok]
	Python: 3.5.1
"""

import telebot
import sys

TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN' # Identificador Erroneo para el ejercicio
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
'El chatID se obtiene ejecutando el ejercicio 00-ChatID.py'
chatID=0 # <- El número obtenido es válido para todos los ejercicios

try:
	info_api=telegram.get_me() # Comprobar que el bot está activo
	print ("Conectando con el Bot de Telegram... [OK]")
	'Algunos de los datos extraidos del API'
	print ("ID: ",info_api.id)
	print ("Nombre del bot: ",info_api.first_name)	
	print("Nombre de usuario: ",info_api.username)
	# print (info_api) # Muestra todos los datos proporcionados por el API
	sys.exit(0)
except telebot.apihelper.ApiException as e:
	print ("Conectando con Bot de Telegram -> ERROR")
	print (e) # Muestra información del error de excepción
	sys.exit(1)

