Demo 1
======
En esta demo se muestra el funcionamiento de mitmproxy con una webs HTTP (sin cifrado).

Instalación
-----------
En la consola:

.. code-block:: bash

    $ pip install mitmproxy

Configuración
-------------
En el navegador establecemos la configuración del proxy. En el caso de Firefox: *Ajustes -> configuración de red ->
configuración* y después *Configuración manual del proxy*. En HTTP ponemos *localhost* con puerto *8080*. Marcamos la
opción de utilizar también para HTTPS.

Iniciar
-------

Para ejecutar mitmproxy en el terminal:

.. code-block:: bash

    $ mitmproxy

Ejemplos de sitios HTTP
-----------------------

* http://www.example.com/
* http://eu.httpbin.org/
