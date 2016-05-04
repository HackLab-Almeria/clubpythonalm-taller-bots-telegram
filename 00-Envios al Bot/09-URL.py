#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: 09 - Enviando una URL (enlace de sitio web)
	Libreria: pyTelegramBotAPI 1.4.2 [ok]
	Libreria: pyTelegramBotAPI 2.0 [ok]
	Python: 3.5.1
"""
import telebot
import sys

TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN entre comillas' # Identificativo Único del Bot
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
'El chatID se obtiene ejecutando el ejercicio 00-ChatID.py'
chatID=000 # <- El chatID obtenido a ejecutar 00-ChatID.py se coloca aquí

try:
	info_api=telegram.get_me() # Comprobar que el bot está activo
	print ("Conectando con el Bot de Telegram... [OK]")
	url="https://telegram.org/"
	#Enviar la dirección de un sitio de Internet
	# Actualmente, la versión 2.0.5 del API no soporta todas las etiquetas de un HTML normal
	telegram.send_message(chatID, url)
	sys.exit(0)
except telebot.apihelper.ApiException as e:
	print ("Conectando con Bot de Telegram -> ERROR")
	print (e) # Error de excepción del API
	sys.exit(1)

