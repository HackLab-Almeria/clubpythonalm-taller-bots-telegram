#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: 12 - Comunicando con el bot (II)
	Librería: pyTelegramBotAPI: 1.4.2 [ok]
	Librería: pyTelegramBotAPI: 2.0 [ok]
	Python: 3.5.1
"""
import telebot
import sys

TOKEN = 'AQUÍ EL NUMERO DE VUESTRO TOKEN' 
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API

# Para no repetir código de como se obtienen los datos del bot y como ya los conocemos
# los asignamos ya a sus variables
nombre_bot="Taller_Python_Almeria"
nombre_usuario="Taller_Python_Almeria_bot"
info_bot="Nombre del bot:" +nombre_bot+"\n"+"Nombre de Usuario: "+nombre_usuario+"\n"+"Token: "+TOKEN+"\n"
saludo="Hola. Bienvenido al Taller de Python..."
ayuda= "/ayuda -> Muestra estos comandos\n"
inicio= "/start -> Reinicia el bot\n"
info="/info -> Muestra datos del bot\n"
comandos="Comandos:\n"+ayuda+inicio+info
          
		   
# Este es código propio del API de Telegram para realizar sus respuestas
# La función va unida al gestor de comandos (handler)
@telegram.message_handler(commands=['start','ayuda'])
def bienvenido(mensaje_telegram):
	chatID = mensaje_telegram.chat.id # <--- ChatID para todos los ejercicios
	telegram.send_message(chatID, saludo)
	telegram.send_message(chatID,comandos)


#Enviar mensaje de texto
def listener(mensaje_telegram):
	nombre_bot="Taller_Python_Almeria"
	nombre_usuario="Taller_Python_Almeria_bot"
	info_bot="Nombre del bot:" +nombre_bot+"\n"+"Nombre de Usuario: "+nombre_usuario+"\n"+"Token: "+TOKEN+"\n"

	'Definimos la función que estará atenta a los mensajes que envíe el bot de Telegramensaje.'
	for mensaje in mensaje_telegram:
		chatID = mensaje.chat.id # <-- Este es el chatID que se obtiene para todos los ejercicios
		if mensaje.content_type == 'text':
			if mensaje.text.upper()=='HOLA':
				telegram.send_message(chatID, saludo)
				#telegram.reply_to(mensaje,saludo)
			if mensaje.text.upper()=="/INFO":
				info_bot +="Chat ID: "+str(chatID)
				telegram.send_message(chatID, info_bot)

print ("- Conectado con el Bot [OK] -> (Ctr+C para salir)") # Conectado y modo de detener el bot

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




	
