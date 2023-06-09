Demo2
=====
Esta demo continúa la demo1. Ver primero los pasos de demo1. El objetivo es comprobar cómo al solicitar una web HTTPS
se muestra la pantalla de aviso de certificado inválido y cómo se resuelve. Pero esta vez iniciamos mitmproxy con el
siguiente comando:

.. code-block:: bash

    mitmweb

Esto iniciará mitmproxy en modo web, disponible en http://127.0.0.1:8081

Caso 1
------
Al acceder a https://nekmo.com/es/ se muestra la pantalla de aviso. Pero puede saltarse aceptando el certificado
erróneo. Podemos verlo después a través del modo web las peticiones realizadas.

Caso 2
-------
Para saltarnos la restricción de forma global, debemos instalar el certificado. Para ello vamos a *ajustes ->
privacidad y seguridad -> ver certificados...* y en la modal vamos a *"autoridades"*, donde pulsamos en el botón de
*importar* para elegir en la carpeta ``~/.mitmproxy`` el certificado ``mitmproxy-ca-cert.pem``. Aceptamos todo y luego
cerramos la modal. Si accedemos a cualquier otra web podremos acceder, incluido https://google.es



