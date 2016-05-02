#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-
""" Ejemplo: Leer Noticias RSS en Telegram (III)
	Libreria: pyTelegramBotAPI 1.4.2
	Python: 3.5.1
"""

import telebot
import sys
import feedparser


url =  "http://blog.bricogeek.com/noticias/arduino/rss/" 
rss = feedparser.parse(url)


servicio="Servicio del Bot de Telegram"
inicio_servicio="Iniciando..."+servicio
print (inicio_servicio),
TOKEN = 'AQUÍ EL NUMERO DE VUESTRO TOKEN' #Ponemos nuestro TOKEN generado con el @BotFather
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API


def listener(messages):
	for m in messages:
		chatID = m.chat.id
	if m.content_type == 'text':
			for noticia in rss.entries:
				evento=noticia.title+"\n"+noticia.link		
				telegram.send_message(chatID, evento)			

try:
	telegram.get_me() # Comprobar el API. Devuelve un objeto
	print ("-> OK")
	print ("Token: "+TOKEN)
	print ("- Presionar Ctrl+C para parar el servicio...")
	telegram.set_update_listener(listener)
except Exception as e:
	print ("-> ERROR")
	print (e)
	sys.exit(0)

telegram.polling(none_stop=False) # Interval setup. Sleep 3 secs between request new message.
telegram.polling(interval=3)
telegram.polling()

try:
	while True:
		pass
except KeyboardInterrupt:
	print ("Programa Finalizado...")
	sys.exit(0)
	
