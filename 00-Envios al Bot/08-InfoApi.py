#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: 08 - Conociendo el API
 	Libreria: pyTelegramBotAPI 1.4.2
	Python: 3.5.1
"""

import telebot
import sys

TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN' # Identificador Erroneo para el ejercicio
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
'El chatID se obtiene ejecutando el ejercicio 00-ChatID.py'
chatID=000 # <- El número obtenido es válido para todos los ejercicios

try:
	info_api=telegram.get_me() # Comprobar que el bot está activo
	print ("Conectando con el Bot de Telegram... [OK]")
	print ("ID: ",info_api.id)
	print ("Nombre del bot: ",info_api.first_name)	
	print("Nombre de usuario: ",info_api.username)
	sys.exit(0)
except telebot.apihelper.ApiException as e:
	print ("Conectando con Bot de Telegram -> ERROR")
	#print (e)
	sys.exit(1)

