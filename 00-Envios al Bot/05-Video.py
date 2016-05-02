#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: 05 - Enviar un video
    Libreria: pyTelegramBotAPI 1.4.2
	Python: 3.5.1
"""

import telebot
import sys

TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN' #  Identificador único del bot
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
'El chatID se obtiene al ejecutar el ejercicio 00-chatID.py'
chatID= 0  # Aquí el número de chatID obtenido
try:
	telegram.get_me() # Comprobar que el bot está activo
	print ("Conectando con el Bot de Telegram... [OK]")
	saludo="Enviando video..." # Mensaje a enviar...
	telegram.send_message(chatID, saludo)
	#Enviar videos
	video = open('.//videos//show_toallas.mp4', 'rb')
	telegram.send_video(chatID, video)
	sys.exit(0)
except Exception as e:
	print ("Conectando con Bot de Telegram -> ERROR")
	#print (e)
	sys.exit(1)


