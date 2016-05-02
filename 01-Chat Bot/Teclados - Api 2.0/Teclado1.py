#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: Teclado Virtual 1 (Api 2.0)
	Libreria: pyTelegramBotAPI 1.4.2
	Python: 3.5.1
"""

from telebot import types # Importamos el API correspondiente para usar teclados virtuales
import telebot
import sys


TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN' # Identificador único del bot
telegram = telebot.TeleBot(TOKEN) # Activamos el bot asociado al Token

# Preparamos un menú de instrucciones
instrucciones="Instrucciones:\n 1.- Saludar \n 2.- Despedirse\n 3.- Ayuda"
'Esta es la revisión de creación del teclado para el API 2.0 de Telegram'
teclado_virtual = types.ReplyKeyboardMarkup() # Activamos el teclado virtual
tecla1 = types.KeyboardButton('1')
tecla2 = types.KeyboardButton('2')
tecla_ayuda= types.KeyboardButton("Ayuda")
teclado_virtual.add(tecla1,tecla2,tecla_ayuda)

def listener(mensaje_telegram):
	'Definimos la función que estará atenta a los mensajes que envíe el bot de Telegram.'
	
	nombre_bot="Taller_Python_Almeria"
	nombre_usuario="Taller_Python_Almeria_bot"
	info_bot="Nombre del bot:" +nombre_bot+"\n"+"Nombre de Usuario: "+nombre_usuario+"\n"+"Token: "+TOKEN+"\n"

	for mensaje in mensaje_telegram: # Bucle de captura de los mensajes que envía el bot
		chatID = mensaje.chat.id # Identificativo del chat. IMPRESCINDIBLE para enviar mensajes
		
		if mensaje.content_type == 'text': #Esperamos mensajes de texto
			
			if mensaje.text=='1': # Si es el 1
					telegram.send_message(chatID, "Hola") # Saludamos
				
			if mensaje.text=='2': # Si es el 2
					telegram.send_message(chatID, "Adiós") # Nos despedimos
				
			if mensaje.text=="Ayuda": # Pulsa 'Ayuda' y mostramos el menú de instrucciones
					telegram.send_message(chatID,instrucciones)
				
	return 0 # Fin de la función y su valor de retorno


try:
	info_api=telegram.get_me() # Comprobar que el bot está activo
	print ("Conectando con el Bot de Telegram... [OK]")
	print ("-CTR + C para detener el Bot -") # Para salir desde consola
	telegram.send_message(chat_id=chatID,text=instrucciones,reply_markup=teclado_virtual ) # Mandamos el teclado diseñado
	telegram.set_update_listener(listener) # Actualizamos el escuchador (listener)
	telegram.polling() # Activamos el bucle de sondeo de mensajes
	sys.exit(0)
except Exception as e:
	print ("Conectando con Bot de Telegram -> ERROR")
	print (e)
	sys.exit(1)


