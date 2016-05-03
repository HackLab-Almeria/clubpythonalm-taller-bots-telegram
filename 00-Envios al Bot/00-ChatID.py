#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-
""" 
	Ejemplo: Obtener el Chat ID
   	Libreria: pyTelegramBotAPI 1.4.2
   	Libreria: pyTelegramBotAPI 2.0.4
	Python: 3.5.1
"""

import telebot
import sys

servicio="- Servicio del Bot de Telegram ... "

TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN entre comillas'
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API

def listener(mensaje_telegram):
	for mensaje in mensaje_telegram:
		chatID = mensaje.chat.id # <---- chatID - PONER ESTE NUMERO EN TODOS LOS EJERCICIOS DE ENVIOS AL BOT
		print ("- Chat ID = "+ str(chatID) + " ... [OK]")
		break
	sys.exit(0)

try:
	info_api=telegram.get_me() # Comprobar si el bot está disponible
	print ("- Conectando con el Bot de Telegram... [OK]")
	print ("- Ctrl + C para detener el Bot -") # Para salir desde consola
	print ("- Inicie su bot...")
	print ("- Esperando el Chat ID ... [OK]")
	telegram.set_update_listener(listener) # Actualizamos el escuchador (listener)
	telegram.polling() # Activamos el bucle de sondeo de mensajes
except Exception as e:
	print ("Conectando con Bot de Telegram -> ERROR")
	print (e)
	sys.exit(1)

