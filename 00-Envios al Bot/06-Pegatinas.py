#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: 06 - Enviar Pegatinas (stickers) de Telegram
  	Libreria: pyTelegramBotAPI 1.4.2
	Python: 3.5.1
"""

import telebot

TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN' #  Identificador único del bot
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
'El chatID se obtiene al ejecutar el ejercicio 00-chatID.py'
chatID=000 # <- Ese número de chatID se coloca aquí para todos los ejercicios

saludo="Hola Bot..."
try:
	telegram.get_me() # Comprobar que el bot está activo
	print ("Conectando con el Bot de Telegram... [OK]")
	saludo="Enviando pegatina..." # Mensaje a enviar...
	telegram.send_message(chatID, saludo)
	#Enviar Pegatina (sticker)
	pegatina = open('.//pegatinas//jesus.webp', 'rb') # Elegimos la pegatina de Telegram
	telegram.send_sticker(chatID, pegatina)
	sys.exit(0)
except Exception as e:
	print ("Conectando con Bot de Telegram -> ERROR")
	#print (e)
	sys.exit(1)



