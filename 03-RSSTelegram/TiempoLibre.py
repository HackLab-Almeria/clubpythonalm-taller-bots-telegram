#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
""" Ejemplo: Leer Noticias RSS en Telegram (II)
	Libreria: pyTelegramBotAPI 1.4.2
	Python: 3.5.1
""" 

import telebot
import time
import sys
import signal
import feedparser
import time
import datetime

url =  "http://www.weeky.es/feed/"        #'http://chicagotribune.feedsportal.com/c/34253/f/622872/index.rss'
rss = feedparser.parse(url)
fecha = datetime.datetime.now()
servicio="Servicio del Bot de Telegram"
inicio_servicio="Iniciando..."+servicio

print (inicio_servicio),

TOKEN = 'AQUÍ EL NUMERO DE VUESTRO TOKEN entre comillas' #Ponemos nuestro TOKEN generado con el @BotFather
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API


def listener(messages):
	for m in messages:
		chatID = m.chat.id
		print ("Chat ID "+ str(chatID) + "...OK")
		#telegram.send_message(chatID,"------ Próximas Actividades -------\n")

		#tb.send_message(chatid,"------------ Anterior(es) ------------")
		if m.content_type == 'text':
			#noticia = "Hola Bot"
			for noticia in rss.entries:
				telegram.send_message(chatID,noticia.title)
				telegram.send_message(chatID,noticia.link)

try:
	telegram.get_me() # Comprobar el API. Devuelve un objeto
	print ("-> OK")
	print ("Presionar Ctrl+C para parar el servicio...")
	telegram.set_update_listener(listener)
		
except Exception:
	print ("-> ERROR")
	sys.exit(0)

telegram.polling(none_stop=True)
telegram.polling(interval=1)
telegram.polling()
	
