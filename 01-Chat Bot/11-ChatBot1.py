#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: 11 - Comunicando con el bot (I)
    Nombre del bot de Telegram: Taller_Python_Almeria
	Librería: pyTelegramBotAPI: 1.4.2 [ok]
	Librería: pyTelegramBotAPI: 2.0 [ok]
	Python: 3.5.1
"""
import telebot
import sys

TOKEN = 'AQUÍ EL NUMERO DE VUESTRO TOKEN entre comillas' 
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API

saludo="Hola. Bienvenido al Taller de Python..."
comandos="Ayuda:\n/info -> Muestra datos del bot\n/start -> Reinicia el bot\n"
servicio="- Servicio del Bot de Telegram ... "

#Enviar mensaje de texto
def listener(mensaje_telegram):
	'Definimos la función que estará atenta a los mensajes que envíe el bot de Telegram.'

	# Datos sobre el bot a modo de información
	nombre_bot=info_api.first_name
	nombre_usuario=info_api.username
	info_bot="Nombre del bot:" +nombre_bot+"\n"+"Nombre de Usuario: "+nombre_usuario+"\n"+"Token: "+TOKEN+"\n"
	

	for mensaje in mensaje_telegram:
		chatID = mensaje.chat.id # <---- chatID para todos los ejercicios
		
		if mensaje.content_type == 'text': # Esperamos un mensaje de texto
					
			if mensaje.text.upper()=="/START": #Siempre que se inicia un bot, envía /start
				telegram.send_message(chatID, saludo) # Saludo
				telegram.send_message(chatID,comandos) # Enviamos el menú de ayuda
				
			if mensaje.text.upper()=='HOLA': # Si nos saluda con Hola
				telegram.send_message(chatID, saludo) # Respondemos
				
			if mensaje.text.upper()=="/INFO": # Si pide información
				info_bot +="Chat ID: "+str(chatID) # Enviamos esta información del creación del bot
				telegram.send_message(chatID, info_bot)

try:
	info_api=telegram.get_me() # Comprobar si el bot está disponible
	print ("- Conectando con el Bot de Telegram... [OK]")
	print ("- Ctrl + C para detener el Bot -") # Para salir desde consola
	telegram.set_update_listener(listener) # Actualizamos el escuchador (listener)
	telegram.polling() # Activamos el bucle de sondeo de mensajes
except Exception as e:
	print ("Conectando con Bot de Telegram -> ERROR")
	print (e) # Muestra el error
	sys.exit(1)
