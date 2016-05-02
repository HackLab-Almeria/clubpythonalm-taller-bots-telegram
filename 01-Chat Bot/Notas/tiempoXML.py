#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-
from xml.dom import minidom

doc = minidom.parse("pronostico.xml")

pronostico = doc.getElementsByTagName("medidas")

for valor in pronostico:
        estacion= valor.getAttribute("estacion")
        hora_datos= valor.getElementsByTagName("hora_datos")[0]
        temperatura = valor.getElementsByTagName("temperatura")[0]
        cielo = valor.getElementsByTagName("cielo")[0]
        humedad = valor.getElementsByTagName("humedad")[0]
        presion = valor.getElementsByTagName("presion")[0]
        viento= valor.getElementsByTagName("viento")[0]
        dir_viento= valor.getElementsByTagName("dir_viento")[0]

        datos=("Estación: %s\nHora: %s\nTemperatura: %s\nCielo: %s\nHumedad: %s\nPresion: %s\nViento: %s\nDireccion: %s" %
				(estacion,\
				hora_datos.firstChild.data,\
				temperatura.firstChild.data,\
				cielo.firstChild.data,\
				humedad.firstChild.data,\
				presion.firstChild.data,\
				viento.firstChild.data,\
				dir_viento.firstChild.data))

print(datos)
