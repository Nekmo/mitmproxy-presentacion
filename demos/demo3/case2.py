#!/usr/bin/env python
import re

from mitmproxy import http
from bs4 import BeautifulSoup


def request(flow: http.HTTPFlow):
    # Se crea la respuesta con código 200, un código personalizado y Content-Type text/html
    flow.response = http.Response.make(
        200,  # (optional) status code
        b'<style>'
        b'h1 { animation: blinker 1s step-start infinite; color: red; font-size: 8em; text-align: center; }'
        b'@keyframes blinker { 50% { opacity: 0; } }'
        b'</style>'
        b'<h1>VIVA PHP!!!1</h1>',
        {"Content-Type": "text/html"},  # (optional) headers
    )
