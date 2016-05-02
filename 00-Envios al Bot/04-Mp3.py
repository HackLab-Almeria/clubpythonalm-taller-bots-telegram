#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: 04 - Enviar Audio Mp3
   	Libreria: pyTelegramBotAPI 1.4.2
	Python: 3.5.1
"""
import telebot
import sys

TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN' #  Indentificador único del bot
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
'El chatID se obtiene ejecutando el ejercicio 00-ChatID.py'
chatID=0000 # <- Aquí el número de chatID para todos los ejercicios
try:
	telegram.get_me() # Comprobar que el bot está activo
	print ("Conectando con el Bot de Telegram... [OK]")
	saludo="Enviado un archivo de audio..." # Mensaje a enviar...
	telegram.send_message(chatID, saludo)
	#Enviar audio/mp3
	audio = open('.//mp3//Amorphis - Sky Is Mine.mp3', 'rb') # elegimos el archivo de audio
	telegram.send_audio(chatID, audio)
	sys.exit(0)
except Exception as e:
	print ("Conectando con Bot de Telegram -> ERROR")
	#print (e)
	sys.exit(1)





