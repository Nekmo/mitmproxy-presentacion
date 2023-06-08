#!/usr/bin/env python
import re

from mitmproxy import http
from bs4 import BeautifulSoup


def response(flow: http.HTTPFlow):
    # Si la web encuentra "php" como parámetro query
    if "php" in flow.request.query:
        # Obtenemos el texto de la respuesta
        text = flow.response.text
        # Lo parseamos con beautifulsoup
        soup = BeautifulSoup(text, "html.parser")
        # Obtenemos todos los elementos que tienen texto
        for element in soup.find_all(re.compile(".+"), text=True):
            # Reemplazamos todas las palabras por PHP
            element.string = re.sub(r"\w+", "PHP", element.string)
        # Volvemos a establecer la respuesta teniendo como texto el soup alterado.
        flow.response.text = str(soup)
