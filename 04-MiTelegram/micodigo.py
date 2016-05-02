#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Este ejercicio muestra como importar todo el código del Token y el ChatID
	sin tener que mostrarlo aquí. Y como enviar mensajes al bot desde cualquier
	otro programa en Python que estemos desarrollando. 
"""

from mitelegram import *

mi_codigo="Este mensaje se leerá en el bot"

telegram.send_message(chatID,mi_codigo)

alBot(yo+mi_codigo)



	
