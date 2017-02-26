# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'

from bs4 import BeautifulSoup
import requests

URL = "http://jarroba.com/"

# Realizamos la petición a la web
req = requests.get(URL)

# Comprobamos que la petición nos devuelve un Status Code = 200
status_code = req.status_code
if status_code == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text, "html.parser")

    # Obtenemos todos los divs donde estan las entradas
    entradas = html.find_all('div', {'class': 'col-md-4 col-xs-12'})

    # Recorremos todas las entradas para extraer el título, autor y fecha
    for i, entrada in enumerate(entradas):
        # Con el método "getText()" no nos devuelve el HTML
        titulo = entrada.find('span', {'class': 'tituloPost'}).getText()
        # Sino llamamos al método "getText()" nos devuelve también el HTML
        autor = entrada.find('span', {'class': 'autor'})
        fecha = entrada.find('span', {'class': 'fecha'}).getText()

        # Imprimo el Título, Autor y Fecha de las entradas
        print "%d - %s  |  %s  |  %s" % (i + 1, titulo, autor, fecha)

else:
    print "Status Code %d" % status_code
