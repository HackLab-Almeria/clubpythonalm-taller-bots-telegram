#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: Leer Noticias RSS en Telegram (I)
	Libreria: pyTelegramBotAPI 1.4.2 [ok]
	Libreria: pyTelegramBotAPI 2.0 [ok]
	Python: 3.5.1
"""

import telebot
import time
import sys
import signal
import feedparser
import time
import datetime

try:
	if sys.version_info.major < 3:
		raise Exception ("Python 3.x mejor")
except Exception:
		print ("Ejecutar en Python 3, mejor")

# Leer las últimas noticias del Ideal Almería
url =  "http://www.ideal.es/almeria/rss/atom?seccion=ultima-hora" 
rss = feedparser.parse(url)


fecha = datetime.datetime.now()
servicio="-> Servicio del Bot de Telegram"
inicio_servicio="-- Iniciando..."
print (inicio_servicio)
print (- Presionar Ctrl+C para detener el servicio....")
TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN entre comillas'
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
chatID=0

def Control_C(signal, frame):
	print ('\n*** Fin del servicio ***')
	sys.exit(0)


def listener(messages):

	for m in messages:
		chatID = m.chat.id
		
		if m.content_type == 'text':
			telegram.send_message(chatID,"-Leyendo las Noticias-")
			#imagen_logo = open(logo, 'rb')
			#telegram.send_photo(chatID, open(logo, 'rb')) #imagen_logo)
			for noticia in rss.entries:
				'Se reciben los mensajes desde el Bot de Telegram.'
				if (noticia.updated_parsed[0] >= fecha.year): # anio
					if (noticia.updated_parsed[1] == fecha.month):
						if (noticia.updated_parsed[2] >= fecha.day): # dia
							#print (noticia.updated_parsed[0],noticia.updated_parsed[1],noticia.updated_parsed[2])
								#print (noticia.updated_parsed)	
							evento=noticia.title+"\n"+noticia.link		
							# print (evento)
							#print (noticia.link)
							telegram.send_message(chatID, evento)
								
					if (noticia.updated_parsed[1] > fecha.month):
						evento=noticia.title+"\n"+noticia.link		
						# print (evento)
						telegram.send_message(chatID, evento)

	return 0


try:
	info_api=telegram.get_me() # Comprobar si el bot está disponible
	print ("- Conectando con el Bot de Telegram... [OK]")
	telegram.set_update_listener(listener) # Actualizamos el escuchador (listener)
except Exception as e:
	print ("Conectando con Bot de Telegram -> ERROR")
	#print (e)
	sys.exit(1)
while True:
	signal.signal(signal.SIGINT, Control_C)
	telegram.polling(none_stop=True)

		
