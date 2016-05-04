#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Ejemplo: 10 - Enviar mensajes con HTML y MarkDown
   	Libreria: pyTelegramBotAPI 1.4.2 [ok]
   	Libreria: pyTelegramBotAPI 2.0 [ok]
	Python: 3.5.1
"""
import telebot
import sys

TOKEN='AQUÍ EL NUMERO DE VUESTRO TOKEN entre comillas' # Identificativo Único del Bot
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API
'El chatID se obtiene ejecutando 00-ChatID.py'

chatID=0000 # <- Aquí vuestro chatID

try:
	info_api=telegram.get_me() # Comprobar que el bot está activo
	print ("Conectando con el Bot de Telegram... [OK]")
	print ("Enviando datos HTML y Markdown...")
	#Enviar la dirección de un sitio de Internet
	url="http://hacklabalmeria.net/actividades/2016/02/20/fundacion-club-python-almeria.html\n"
	texto_html="<a href='https://core.telegram.org'>Telegram </a> y su <b>API</b>"
	html_elpais="<a href='http://elpais.com'>El Pais</a>"
	html_abc="<a href='http://www.abc.es/'>ABC</a>"
	# Enviar mensaje de con HTML
	# La versión del Api actual, 2.0.5 no soporta todas las etiquetas de un HTML estandar
	"Se incluyen parámetros especiales: 'parser_mode' para enviar código HTML"
	telegram.send_message(parse_mode='HTML', chat_id=chatID, text='<b>Negrita</b> <i> cursiva </i>')

	"La misma filosofía se sigue para enviar código Markdown sólo cambia el parámetro: 'parse_mode'."
	telegram.send_message(parse_mode='Markdown', chat_id=chatID, text='*Negrita* _cursiva_')

	telegram.send_message(chatID, url)
	telegram.send_message(parse_mode='HTML', chat_id=chatID,text=texto_html)
	telegram.send_message(parse_mode='HTML', chat_id=chatID,text=html_elpais)
	telegram.send_message(parse_mode='HTML', chat_id=chatID,text=html_abc)
	
	#Enviar mensaje con Markdown
	telegram.send_message(parse_mode='Markdown', chat_id=chatID, text='Markdown texto en *Negrita* _cursiva_')
	telegram.send_message(parse_mode='Markdown', chat_id=chatID, text="Markdown URL  [El Pais](http://elpais.es)")
	telegram.send_message(parse_mode='Markdown', chat_id=chatID, text="Markdown URL  [ABC](http://abc.es)")
	telegram.send_message(parse_mode='Markdown', chat_id=chatID, text="[Logo Club Python](http://hacklabalmeria.net/recursos/2016-02-20/logotipo-500x500.png)")

	sys.exit(0)
except telebot.apihelper.ApiException as e:
	print ("Conectando con Bot de Telegram -> ERROR")
	print (e) # Muestra el error de fallo de conexión del bot
	sys.exit(1)




