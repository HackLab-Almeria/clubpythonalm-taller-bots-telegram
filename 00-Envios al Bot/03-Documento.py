#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: 03 - Enviar documento al bot
 	Libreria: pyTelegramBotAPI 1.4.2
	Python: 3.5.1
"""
import telebot
import sys

TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN entre comillas' #  Identificativo único del bot
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
'El chatID se obtiene ejecutando el ejercicio 00-ChatID.py'
chatID=0 # El número obtenido aquí

try:
	telegram.get_me() # Comprobar que el bot está activo
	print ("Conectando con el Bot de Telegram... [OK]")
	saludo="Enviado un documento.." # Mensaje a enviar...
	telegram.send_message(chatID, saludo)
	#Enviar documentos. Ejemplo .pdf
	archivo_texto = open('.//documentos//nota.txt', 'r') # elegimos el documento a enviar
	telegram.send_document(chatID, archivo_texto)
	sys.exit(0)
except Exception as e:
	print ("Conectando con Bot de Telegram -> ERROR")
	#print (e)
	sys.exit(1)


