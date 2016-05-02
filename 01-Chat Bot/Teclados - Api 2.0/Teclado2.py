#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: Teclado Virtual 2 (Api 2.0) con Emojis
	Libreria: pyTelegramBotAPI 1.4.2
	Python: 3.5.1
"""
import telebot
from telebot import types
import sys
import datetime
import time

TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN entre comillas' # Identificador único del bot
telegram = telebot.TeleBot(TOKEN) # Activamos el bot asociado al Token

'Esta es la revisión de creación del teclado para el API 2.0 de Telegram'
teclado_virtual = types.ReplyKeyboardMarkup() # Activamos el teclado virtual
tecla1 = types.KeyboardButton('\U000026C5') # Tecla con Emoji : nube-sol
tecla2 = types.KeyboardButton('\U0000231B') # Tecla con Emoji : reloj
tecla_ayuda= types.KeyboardButton("Ayuda")
teclado_virtual.add(tecla1,tecla2,tecla_ayuda)


opciones="Opciones:\n <b>1.</b>- El Tiempo\n <b>2.</b> - Hora Local"


# Los emojis son unicódigos de 8 dígitos que en Python se escriben como '\U' y completando
# con 0 después de la U y luego el unicódigo, hasta 8 dígitos. 
# En este sitio se pueden ver todos los códigos
# http://unicode.org/emoji/charts/full-emoji-list.html
# Ejemplo unicódigo de sol+nube es 26C5 se ponen delante 4 ceros y el código hasta completar 8 dígitos


def listener(mensaje_telegram):
	'Definimos la función que estará atenta a los mensajes que envíe el bot de Telegram.'
	
	
	for mensaje in mensaje_telegram:
		chatID = mensaje.chat.id # <--- Aquí se obtiene el chatID
		if mensaje.content_type == 'text':
			
			if mensaje.text=='\U000026C5' or mensaje.text=='1':  # Pulsa la nube y el sol o escribe 1
				"""En este ejemplo he incluido unos datos ya obtenidos con anterioridad para facilitar la explicación
						Los datos se puede obtener desde cualquier fuente: una web, un archivo, etc. Si es importante
						que, a poder ser, sea desde un archivo .xml
				"""
				telegram.send_message(chatID, "Almería Capital: 28ºC. \n Humedad: 64% \n Radiación UV 6 ('moderado')")
				
			if mensaje.text=='\U0000231B' or mensaje.text=='2': # Pulsa el reloj de arena o escribe 2
				telegram.send_message(chatID,time.strftime("Fecha: %d/%m/%y\nHora: %I:%M:%S"))
					
			if mensaje.text=='Ayuda': # Muestra menú de opciones
				telegram.send_message(chat_id=chatID,parse_mode="HTML",text=opciones)
	
	return 0

try:
	info_api=telegram.get_me() # Comprobar si el bot está disponible
	print ("Conectando con el Bot de Telegram... [OK]")
	print ("-CTR + C para detener el Bot -") # Para salir desde consola
	telegram.send_message(chat_id=chatID,parse_mode="HTML",text=opciones)
	telegram.send_message(chat_id=chatID,text="Elija una opción",reply_markup=teclado_virtual ) # Mandamos el teclado diseñado
	telegram.set_update_listener(listener) # Actualizamos el escuchador (listener)
	telegram.polling() # Activamos el bucle de sondeo de mensajes
	sys.exit(0)
except telebot.apihelper.ApiException:
	print ("Error conectando con el bot...")
