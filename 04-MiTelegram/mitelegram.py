#!/usr/bin/env python3
# -*- coding: utf-8-*-

import telebot
import sys

TOKEN = 'AQU� EL NUMERO DE VUESTRO TOKEN entre comillas' 
telegram = telebot.TeleBot(TOKEN) # Combinamos la declaraci�n del Token con la funci�n de la API
chatID=0000 # Cuando ya  teng�is vuestro chatID. Siempre AQU�
nombre_bot="Club_Python_Almeria"
nombre_usuario="Club_Python_Almeria_bot"
yo=" <- Tu Propia Alias -> \n" # Por si quieres usar un alias distinto al de Telegram

def alBot (mensaje):
	telegram.send_message(chatID,mensaje)
	
try:
	api_info=telegram.get_me() # Comprobar el API. Devuelve un objeto
except:
	print ("No se puede conectar al Club...")
	sys.exit(1)








