#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: 01  - Saludando al bot
	Libreria: pyTelegramBotAPI 1.4.2 [ok]
	Libreria: pyTelegramBotAPI 2.0 [ok]
	Python: 3.5.1
"""
import telebot
import sys

TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN entre comillas' # Identificativo Único del Bot
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
'El chatID se obtiene al ejecutar el ejercicio 00-ChatID.py'
chatID=0 # <- Aquí vuestro chatID 

try:
	telegram.get_me() # Comprobar que el bot está activo
	print ("Conectando con el Bot de Telegram... [OK]")
	print ("Enviando mensaje...")
	saludo="Hola Bot..." # Mensaje a enviar...
	telegram.send_message(chatID, saludo)
	sys.exit(0)
except Exception as e:
	print ("Conectando con Bot de Telegram -> ERROR")
	#print (e)
	sys.exit(1)



