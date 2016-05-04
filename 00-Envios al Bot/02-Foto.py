#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: 02 - Evnviar foto al bot
   	Libreria: pyTelegramBotAPI 1.4.2 [ok]
   	Libreria: pyTelegramBotAPI 2.0 [ok]
	Python: 3.5.1
"""

import telebot # Librería del Api de los bots de Telegram.
import sys     # Importando la librería de sistema

TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN entre comillas' # Identificador único del bot
telegram = telebot.TeleBot(TOKEN) # Activamos el bot asociado al Token
'El chatID se obtiene al ejecutar el ejercicio 00-ChatID.py'
chatID=0 # <- Aquí vuestro chatID 

try:
	telegram.get_me() # Comprobar que el bot está activo
	print ("Conectando con el Bot de Telegram... [OK]")
	saludo="Enviado una imagen.." # Imágen a enviar...
	telegram.send_message(chatID, saludo)
	imagen = open('.//iconos//03.png', 'rb') # Podría producir excepción si no se encuentra el archivo
	telegram.send_photo(chatID, imagen)
	sys.exit(0)
except Exception as e: # Se recogen cualquier excepción de arriba
	print ("Conectando con Bot de Telegram -> ERROR")
	print (e) # mostrará el mensaje para cualquier error en el bloque del try
	sys.exit(1)






