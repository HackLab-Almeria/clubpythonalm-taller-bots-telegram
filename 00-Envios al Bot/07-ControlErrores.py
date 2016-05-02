#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: 07 - Contro de Errores
    Libreria: pyTelegramBotAPI 1.4.2
	Python: 3.5.1
"""

import telebot
import sys

TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN entre comillas' # Identificador Erroneo para el ejercicio
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
'El chatID sólo se obtiene ejecutando el ejercicio 00-ChatID.py'
chatID=000 # <- Ese número se coloca aquí para todos los ejercicios

saludo="Hola Bot..."

#Control de errores. El bot podría no estar disponible
try:
	respuesta_telegram=telegram.get_me() # Comprobar que el bot está activo
	print ("Conectando con el Bot de Telegram... [OK]")
	saludo="Enviando video..." # Mensaje a enviar...
	telegram.send_message(chatID, saludo)
	#Enviar videos
	video = open('.//videos//show_toallas.mp4', 'rb')
	telegram.send_video(chatID, video)
	sys.exit(0)
except telebot.apihelper.ApiException as e: # Esta es la excepción del bot cuando no puede conectar
	print ("Conectando con Bot de Telegram -> ERROR")
	print (e)
	sys.exit(1)

