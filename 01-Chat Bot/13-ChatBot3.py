#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: 13 - Comunicando con el bot (III)
	Librería: pyTelegramBotAPI: 1.4.2 [ok]
	Librería: pyTelegramBotAPI: 2.0 [ok]
	Python: 3.5.1
"""
import telebot
import sys

TOKEN = 'AQUÍ EL NUMERO DE VUESTRO TOKEN entre comillas' 
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API

nombre_bot="Taller_Python_Almeria"
nombre_usuario="Taller_Python_Almeria_bot"
info_bot="Nombre del bot:" +nombre_bot+"\n"+"Nombre de Usuario: "+nombre_usuario+"\n"+"Token: "+TOKEN+"\n"
saludo="Hola. Bienvenido al Taller de Python..."
ayuda= "/ayuda -> Muestra estos comandos\n"
inicio= "/start -> Reinicia el bot\n"
info="/info -> Muestra datos del bot\n"
imagenes="/imagen nombre_imagen . Ej. /imagen mapa.png"
comandos="Comandos:\n"+ayuda+inicio+info+imagenes

#Usamos el API de Telegram para respuestas del bot
@telegram.message_handler(commands=['start','ayuda'])
def bienvenido(mensaje_telegram):
	chatID = mensaje_telegram.chat.id # <------ ChatID para todos los ejercicios
	telegram.send_message(chatID, saludo)
	telegram.send_message(chatID,comandos)

@telegram.message_handler(commands=['imagen','foto'])
def envio_foto(mensaje_telegram):
	chatID = mensaje_telegram.chat.id
	
	if len(mensaje_telegram.text) < 9: # Sólo ha escrito /imagen no ha puesto que imágen
		telegram.send_message(chatID," Usa: /imagen nombre_imagen") # Envio mensaje ayuda
	else:
		orden,img=mensaje_telegram.text.split() # Divido el mensaje en 2 usando el espacio como divisor
		try: # Comprobar que la imagen están en imágenes
			imagen = open(".//imagenes//"+img, 'rb')
			telegram.send_photo(chatID, imagen)
		except FileNotFoundError:
			telegram.send_message(chatID,"No existe esa imágen") # Sino está, aviso con error
	return 0
	
#Enviar mensaje de texto
def listener(mensaje_telegram):
	nombre_bot="Taller_Python_Almeria"
	nombre_usuario="Taller_Python_Almeria_bot"
	info_bot="Nombre del bot:" +nombre_bot+"\n"+"Nombre de Usuario: "+nombre_usuario+"\n"+"Token: "+TOKEN+"\n"
	preguntas_nombre=("¿Cómo te llamas?".upper(),"Cómo te llamas?".upper())
	preguntas_nombre+=("¿Como te llamas?".upper(),"Como te llamas?".upper())
	preguntas_nombre+=("Como te llamas".upper(),"Cómo te llamas".upper())	


	for mensaje in mensaje_telegram:
		chatID = mensaje.chat.id
		if mensaje.content_type == 'text':
		
			if mensaje.text.upper()=='HOLA':
				telegram.send_message(chatID, saludo)
				
			if mensaje.text.upper()=="/INFO":
				info_bot +="Chat ID: "+str(chatID)
				telegram.send_message(chatID, info_bot)
				
			if mensaje.text.upper() in preguntas_nombre: #Establecemos una charla corta con el bot
				telegram.send_message(chatID,"Me llamo Botin. Estoy a su disposición. Encantado")
	
print ("----------------Conectado con el Bot ---------------------")

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




	
