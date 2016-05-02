#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: El bot en grupo
	Libreria: pyTelegramBotAPI 2.0.4 (ok)
	Libreria: pyTelegramBotAPI 1.4.2 (ok)
	Python: 3.5.1
"""
import telebot
import sys

TOKEN = 'Tu TOKEN aquí entre comillas' 
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
""" Agregar el bot a un grupo como un usuario más
	Al estar en el grupo responderá, desde éste, a los comandos '/' u otros, que hayamos programado
	Cada usuario del grupo tiene que 'presentarse' ante el bot. Para ello cada usuario lo tiene que activar
	fuera del grupo. Hacemos un programa para que nos captura el chatID de cada 1 de los miembros
	Ejemplo: Se prepara un menú que ponga en el grupo esto:
	Para recibir mensajes de tal o tal..., activa el bot para tu uso privado...
	Envía /activar al bot. En nuestro bot tenemos preparado recibir esa palabra y para obtener el chatID privado
	Y así con todos los usuarios. De ese modo tenemos todos los chatID de todos los miembros
	Los que no activen el bot, sólo reciben mensajes de grupo, no privados.
"""
chatID= 0 # <- El chatID del vuestro bot
"""
	Los números de los ChatID los tiene que gestionar el administrador del bot
	Para ello tiene que enviar al grupo un mensaje para que lo activen en privado
	No he puesto aquí el código porque es necesario poner todos los datos privados
	de cada usuario y los chatID. Sólo comento como se hace.
	Se puede enviar cualquier mensaje a un usuario una vez que se tiene su chatID
"""
chatIDUsuario1= 0000 # Número obtenido para el usuario 1
chatIDUsuario2= 0000 # Número obtenido para el usuario 2
"""
	Cuando se envía cualquier mensaje desde el grupo se obtiene
	el chatIDGrupo. Es un número negativo
	Podemos usar el programa 00-ChatID.py para obtener todos los ChatID
	tanto de los usuarios como del grupo. 
"""
chatIDGrupo= 0 # <- Colocar aquí el chatID del grupo. Es un número negativo
saludo="Hola. Bienvenido al Taller de Python..."
comandos="Ayuda:\n/info -> Muestra datos del bot\n/start -> Reinicia el bot\n"
servicio="- Servicio del Bot de Telegram ... "
chatActivado=0

#Enviar mensaje de texto
def listener(mensaje_telegram):
	'Definimos la función que estará atenta a los mensajes que envíe el bot de Telegram.'

	# Datos sobre el bot a modo de información
	nombre_bot=info_api.first_name
	nombre_usuario=info_api.username
	info_bot="Nombre del bot:" +nombre_bot+"\n"+"Nombre de Usuario: "+nombre_usuario+"\n"

	
	for mensaje in mensaje_telegram:
	
		chatID = mensaje.chat.id # 
		
		if mensaje.content_type == 'text': # Esperamos un mensaje de texto
			' Estas opciones se han visto en los ejercicios de 01-Chat Bot. Revisar como funcionan'

			if mensaje.text.upper()=="/START" or mensaje.text=="/start@nombre_nuestro_bot": #con upper siempre recibe bien lo que escriba
				'Si los miembros usan la opción del menú desde el bot, se envía el comando@nombre_bot'

				chatID=mensaje.chat.id
				if chatID==chatIDGrupo: # Esto se podría enviar con peridiocidad para recordar como información
					telegram.send_message(chatIDGrupo,"¡HOLA GRUPO!")
					telegram.send_message(chatIDGrupo,comandos)
					telegram.send_message(chatID,"Activa tu bot en privado, envía /activar")
				else:
					telegram.send_message(chatID,comandos)
					telegram.send_message(chatID,"/activar -> Activa el bot para uso privado")
			
			if mensaje.text.upper()=="/INFO" or mensaje.text=="/info@nombre_nuestro_bot": # Si pide información
				chatID=mensaje.chat.id
				print (mensaje.chat.username,"ChatID -> ",chatID)
				telegram.reply_to(mensaje, info_bot)
			
			if mensaje.text.upper()=="/ACTIVAR":  # Si pide información
				chatID=mensaje.chat.id
				if not chatID==chatIDGrupo: 
					# Sólo registra el chatID cuando no es el del grupo
					#Hay que hacer una rutina para que sólo se registre 1 vez y una base de datos con cada uno de los chatID de usuario
					# Del modo diccionario miembros={alias:chatUsuario1,....}
					# Y pasarlo a un fichero en disco
					chatActivo=1
					chatIDUsuario1=mensaje.chat.id
					telegram.send_message(chatIDUsuario1,comandos)
					print (mensaje.chat.username,"ChatID -> ",chatID)
					if chatActivo:
						telegram.reply_to(mensaje, "Bot activado.Gracias")
						chatActivo=0



try:
	info_api=telegram.get_me() # Comprobar si el bot está disponible
	print ("- Conectando con el Bot de Telegram... [OK]")
	print ("- Ctrl + C para detener el Bot -") # Para salir desde consola
	telegram.set_update_listener(listener) # Actualizamos el escuchador (listener)
	telegram.polling() # Activamos el bucle de sondeo de mensajes
except Exception as e:
	print ("Conectando con Bot de Telegram -> ERROR")
	print (e) # <- Muestra el error del API en caso de no conectar...
	sys.exit(1)
