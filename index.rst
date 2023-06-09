

.. toctree::
   :glob:
   :hidden:

   *


.. _intro:

======================================
**mitmproxy:** ataques MitM con Python
======================================

.. revealjs-section::
    :data-transition: zoom


.. image:: images/mitmproxy_logo.*
  :width: 200


.. revealjs-notes::

  Hola a todos.



.. _saludo:

👋
==

.. revealjs-section::
    :data-transition: convex

.. revealjs-notes::

  Seguramente a muchos os llame la atención todo esto de la seguridad informática...



.. revealjs-break::
    :data-background-color: #030303
    :notitle:

.. image:: images/hacker.*
  :width: 100%

.. revealjs-notes::

  En plan, como los *hackers* con sus capuchas negras. Aunque aquí hace demasiado calor para ponernosla.



.. _sobre-mi:

Sobre mí **Nekmo**
------------------

+------------------------------------+
|                                    |
| .. image:: images/cara.svg         |
|   :width: 200px                    |
|                                    |
| *Programador Python*               |
|                                    |
+------------------------------------+

.. revealjs-section::
    :data-transition: concave

.. revealjs-notes::

  Pero antes dejadme que me presente. Soy Juan José, más conocido en redes como Nekmo, y llevo programando en
  Python más de media vida.



.. revealjs-break::
    :notitle:

.. revealjs-section::
    :data-transition: fade

.. image:: images/hispasec.*
  :width: 100%


.. revealjs-notes::

  Y todo esto de la seguridad no me es desconocido, gracias a que he trabajado casi 5 años en el sector, en una
  empresa malagueña llamada Hispasec.



.. revealjs-break::
    :notitle:

.. image:: images/mitmproxy_full.*
  :width: 100%

.. revealjs-notes::

  Eso me ha permitido conocer herramientas como mitmproxy, utilizadas para realizar ataques mitm mediante un proxy.
  Pero antes de eso...


Qué son
-------

.. revealjs-fragments::

   * ¿Qué es un **proxy**?
   * ¿Y un ataque **Man in the Middle**?

.. revealjs-notes::

  ¿Cuántos sabríais explicar qué es un proxy? ¿Y un ataque Man in the Middle? -- No os preocupéis, que vamos a verlos
  en detalle.



¿Qué son los **proxies**?
=========================

.. revealjs-notes::

  Lo primero, ¿qué son los proxies?



.. revealjs-break::
    :notitle:

.. image:: images/proxy.drawio.*
  :width: 100%

.. revealjs-notes::

  Un servidor proxy es un dispositivo que hace de intermediario en las peticiones realizadas entre un cliente y un
  servidor.



.. revealjs-break::
    :notitle:

.. image:: images/world-proxies.*
  :width: 80%

.. revealjs-notes::

  A muchos os sonarán porque se utilizan para saltarse restricciones regionales. Vamos, ver el Netflix de otro país.



.. revealjs-break::
    :data-transition: fade
    :notitle:

.. image:: images/proxy2.drawio.*
  :width: 100%

.. revealjs-notes::

  Así pues, el proxy toma una solicitud de un usuario...



.. revealjs-break::
    :data-transition: fade
    :notitle:

.. image:: images/proxy3.drawio.*
  :width: 100%

.. revealjs-notes::

  ... se la envía al servidor destino...


.. revealjs-break::
    :data-transition: fade
    :notitle:

.. image:: images/proxy4.drawio.*
  :width: 100%

.. revealjs-notes::

  ...éste le da la respuesta al proxy...



.. revealjs-break::
    :data-transition: fade slide-out
    :notitle:

.. image:: images/proxy5.drawio.*
  :width: 100%

.. revealjs-notes::

  ...y se lo entrega al usuario.



.. revealjs-break::
    :notitle:
    :data-background-color: #000000
    :data-background-image: _static/thinking.gif

.. revealjs-notes::

  Y puede que estéis pensando... ¿No puede ese servidor leer la solicitud? ¿No podría alterarla...?


.. revealjs-break::
    :notitle:
    :data-background-color: #000000
    :data-background-image: _static/dicaprio.gif

.. revealjs-notes::

  Pues muy bien, eso que estáis pensando exactamente es un...


Ataques Man in the Middle **(MitM)**
====================================

.. revealjs-notes::

  ataque Man in the Middle.



.. revealjs-break::
    :notitle:

.. image:: images/mitm.drawio.*
  :width: 100%

.. revealjs-notes::

  Un ataque man in the middle, traducido como ataque de intermedario, es aquel en que un agente externo, el atacante,
  se encuentra de por medio en la comunicación.


opciones mitm
-------------

* 👁️ Leer
* ➕ Añadir
* ✏️ Modificar

.. revealjs-notes::

  Y puede leer, añadir o modificar a voluntad. Los proxies son sólo una de las técnicas que tienen los atacantes para
  realizar un ataque MitM.


.. revealjs-break::
    :notitle:

.. image:: images/mitmproxy_full.*
  :width: 100%

.. revealjs-notes::

  Y ahora, sabiendo ambos conceptos, vamos a ver mitmproxy.


Versión **consola**
-------------------

.. image:: images/mitmproxy_cli.*
  :width: 100%

.. revealjs-notes::

  mitmproxy tiene una interfaz para ver y modificar las peticiones de nuestra víctima desde la consola. Lo que a todas
  las pelis les gusta, una terminal resultona para aparentar ser un *"hacker"*.


Versión **web**
---------------

.. image:: images/mitmproxy_web.*
  :width: 100%

.. revealjs-notes::

  Además de una versión web muy resultona, pero que aún se encuentra en beta. *Vamos, Como todo lo que yo desarrollo*.


**Python** API
--------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-11|4-6|7-11|1-11

    from mitmproxy import http

    def request(flow: http.HTTPFlow):
        # redirect to different host
        if flow.request.pretty_host == "example.com":
            flow.request.host = "mitmproxy.org"
        # answer from proxy
        elif flow.request.path.endswith("/brew"):
            flow.response = http.Response.make(
                418, b"I'm a teapot",
            )


.. revealjs-notes::

  Y finalmente una API para escribir en Python y realizar cambios, como modificar el servidor de destino o
  alterar la respuesta. En esta demo tenemos (1) un código que altera el host de destino en función del host solicitado,
  (2) y otro fragmento que, en función del path, altera la respuesta. (3) Diría algo más, pero la API es tan sencilla
  como veis.

Demo
----

.. revealjs-section::
    :data-background-color: #000000
    :data-background-image: _static/demo1.gif

.. revealjs-notes::

  Pero dejadme que os lo enseñe. Si es que funciona la demo, claro.


Casos de **uso**
================

.. revealjs-section::
    :data-background-color: #8BB2BE

.. image:: images/cybersecurity.*
  :width: 100%

.. revealjs-notes::

  Vale, y ahora os preguntaréis algunos. ¿Para qué me sirve? Pues no sólo es útil para los malos.


Sombrero **blanco**
-------------------

.. revealjs-fragments::

    * **Depuración** de programas
    * Análisis de **malware**
    * **Tests** de integración
    * ... y más.

.. revealjs-notes::

  Los buenos, es decir, los sombreros blanco, además de los desarrolladores, pueden usarlo para varias cosas, como (leer puntos)


¡Y los malos!
-------------

.. revealjs-section::
    :data-background-color: #000000
    :data-background-image: _static/hacker.gif

.. revealjs-notes::

  ¡Y los malos!

Sombrero **negro**
------------------

.. revealjs-section::
    :data-background-color: #363636

.. revealjs-fragments::

    * **Espionaje**.
    * Robo de **información**.
    * **Phishing**.
    * ... y más.

.. revealjs-notes::

  Ellos, claro está, también pueden utilizarlo para hacer sus cosas de malos, como (leer puntos).


¿Estoy en peligro?
==================

.. revealjs-section::
    :data-background-color: #000000
    :data-background-image: _static/panic.gif

.. revealjs-notes::

  Vale, puede esto os haya asustado un poco. Pero no os preocupéis. Contra los ataques Man in the Middle los buenos tenemos una solución.


SSL/**TLS**
-----------

.. image:: images/certificado-ssl.*
  :width: 100%

.. revealjs-notes::

  SSL/TLS. Por suerte, la mayoría del tráfico web actual está firmado y cifrado. Y esto significa que no pueden realizar un ataque impunemente.


**Aviso** del navegador
-----------------------

.. image:: images/ssl-error.*
  :width: 100%

.. revealjs-notes::

  Si el tráfico está siendo interceptado y la web usa SSL/TLS, el navegador muestra una pantalla de peligro como esta. Tal vez alguna vez os haya salido porque el certificado no es válido.



¿Qué es el **certificado**?
---------------------------

.. image:: images/certificate.*
  :width: 40%

.. revealjs-notes::

  Sin entrar en detalles, el certificado, es lo que demuestra que el servidor destino es quien dice ser. Y sólo el servidor destino tiene la clave privada que lo demuestra.


Certificado **autofirmado**
---------------------------

.. image:: images/padlock-broken.*
  :width: 50%

.. revealjs-notes::

  El certificado de mitmproxy, es un certificado autofirmado que valida cualquier servidor. Permite suplantar cualquier sitio.


Sin **confianza**
-----------------

.. image:: images/no_handshake.*
  :width: 50%

.. revealjs-notes::

  Claro está, ese certificado no es de confianza. Y para que funcione requiere instalarse explícitamente en el equipo o navegador de la víctima. Ya no es tan sencillo para los malos...


Demo
----

.. revealjs-section::
    :data-background-color: #000000
    :data-background-video: _static/demo2.mp4
    :data-background-video-loop:

.. revealjs-notes::

  Pero de nuevo, vamos a verlo con una demostración.


Conclusiones sobre el **cifrado**
=================================

.. revealjs-fragments::

    * mitmproxy **puede funcionar** con sitios **con cifrado SSL/TLS**.
    * ... Pero **debe aceptarse** el certificado inválido,
    * ... **o instalarse** el certificado autofirmado en la máquina.


.. revealjs-notes::

  Por resumir un poco... (LEER).


¿**Cómo se realiza** el ataque entonces?
----------------------------------------

.. revealjs-fragments::

    * Engañar a la víctima para que salte la **pantalla advertencia**.
    * Engañarla para que **instale el certificado autofirmado**.
    * **Tomar posesión** del dispositivo e instalar el certificado.

.. revealjs-notes::

    ¿Entonces qué prácticas puede realizar el atacante? Muchos ya lo habréis pensado tras estas conclusiones, pero en definitiva... (LEER)


¿Pero quedan sitios sin **SSL/TLS**?
------------------------------------

.. revealjs-notes::

   Vale, y algunos pensaréis que esto dificulta mucho un ataque SSL/TLS. Pero muchas webs aún no lo implementan por defecto...


Webs sin HTTPS
--------------

.. image:: images/why_not_https.*
  :width: 100%

**https://whynohttps.com/**

.. revealjs-notes::

   Aquí tenéis un listado de sitios inseguros, entre los que destacan algunos tan importantes como baidu, el Google chino. Sí. Creedlo. En la web indicada tenéis el listado.


Ejemplos de **código**
======================

.. revealjs-section::
    :data-background-color: #000000
    :data-background-image: _static/coding.gif

.. revealjs-notes::

  Pero bueno, he estado hablando mucho, ¡y apenas he enseñado código!

Caso **1**
----------

.. revealjs-section::
    :data-transition: convex

.. revealjs-code-block:: python
   :data-line-numbers: 1-11|5|6|7-8|9-10|11

    from mitmproxy import http
    from bs4 import BeautifulSoup


    def response(flow: http.HTTPFlow):
        if "php" in flow.request.query:
            text = flow.response.text
            soup = BeautifulSoup(text, "html.parser")
            for element in soup.find_all(re.compile(".+"), text=True):
                element.string = re.sub(r"\w+", "PHP", element.string)
            flow.response.text = str(soup)

.. revealjs-notes::

   Bueno, vamos a ver cómo funciona este ejemplo de código, el cual os sorprenderá por lo corto que es. (1) Lo primero
   estamos trabajando con la respuesta, por lo que usamos la función response. (2) Sólo aplicamos la transformación si
   en los parámetros GET de la petición se encuentra "php". (3) Obtenemos la respuesta y la leemos con Beautifulsoup.
   (4) por cada elemento con texto, reemplazamos cada palabra por PHP. (5) y finalmente escribimos el contenido alterado
   en la respuesta.

Caso **2**
----------

.. revealjs-code-block:: python
   :data-line-numbers: 1-15|6|7-15|8|9-13|14|1-15

    import re
    from mitmproxy import http
    from bs4 import BeautifulSoup


    def request(flow: http.HTTPFlow):
        flow.response = http.Response.make(
            200,  # (optional) status code
            b'<style>'
            b'h1 { animation: blinker 1s step-start infinite; color: red; font-size: 8em; text-align: center; }'
            b'@keyframes blinker { 50% { opacity: 0; } }'
            b'</style>'
            b'<h1>VIVA PHP!!!1</h1>',
            {"Content-Type": "text/html"},  # (optional) headers
        )

.. revealjs-notes::

   Este ejemplo es mucho más sencillo aunque sea más largo. (1) Lo aplicamos sólo para la petición, por eso usamos la
   función request. (2) Creamos una respuesta personalizada y la establecemos. (3) En esta respuesta ponemos como código
   200. (4) Ponemos este HTML como contenido. (5) definimos como cabecera Content-Type html.


**Demo:** interceptar código WiFi
=================================

.. revealjs-section::
    :data-transition: fade
    :data-background-color: #000000
    :data-background-image: _static/demo3.gif

.. revealjs-notes::

   Y ahora, para terminar, vamos a ver un ejemplo en el que vosotros mismos podréis probar mitmproxy con vuestros móviles, usando vuestra conexión WiFi. Vamos a analizar vuestro tráfico HTTP de vuestro terminal.

Accede a la **demo**
--------------------

**SSID: mitmdemo**

.. revealjs-section::
    :data-background-color: #030303

.. revealjs-notes::

   Para ello, este es el nombre de la red. La contraseña se la daré primero a una única víctima y luego abriré la demo
   a todos.

Cómo **funciona**
-----------------

.. image:: images/rpi1.drawio.*
  :width: 100%

.. revealjs-notes::

   Vale, ahora os preguntaréis cómo funciona. Para ello tenemos este diagrama que (leer). El asterisco que podéis ver
   en raspberry PI 3, es porque ahora explicaremos en detalle cómo funciona por dentro.

Cómo funciona RPI
-----------------

.. revealjs-section::
    :data-transition: convex

.. image:: images/rpi2.drawio.*
  :width: 100%

.. revealjs-notes::

   Dentro de la Raspberry PI 3 tenemos las siguientes partes (leer).


Componentes **clave**
---------------------

.. revealjs-fragments::

    * **dhcpcd:** cliente DHCP del adaptador Wifi para Internet.
    * **isc-dhcp-server:** servidor DHCP del adaptador Wifi para la víctima.
    * **hostapd:** permite crear la red Access Point para víctimas.
    * **iptables:** enrutamiento entre el adaptador wifi y mitmproxy.
    * **mitmproxy:** escucha de las peticiones de la víctima.

.. revealjs-notes::

   Vale, como sé que son muchas cosas, resumiré los componentes clave utilizados. Tenemos... (leer).

Código **demos**
================

.. revealjs-section::
    :data-transition: fade

.. image:: images/demo_codes.*
  :width: 100%

.. revealjs-notes::

   Si os interesa montar también vosotros una Raspberry PI como esta o cualquiera de las demos, tenéis el código e
   instrucciones en la presentación de Github.

¡Muchas **gracias**!
====================

.. revealjs-fragments::

    **Referencias**

    * `sitio web mitmproxy.org <https://mitmproxy.org/>`_.
    * `ejemplos de código mitmproxy.org <https://docs.mitmproxy.org/stable/addons-examples/>`_.
    * `blog dinofizzotti.com (demo RPI) <https://www.dinofizzotti.com/blog/2022-04-24-running-a-man-in-the-middle-proxy-on-a-raspberry-pi-4/>`_.

.. revealjs-notes::

   Y hasta aquí la presentación. Os agradezco a todos por venir, y aquí os dejo algunas referencias utilizadas en esta presentación.

¿Y la **presentación**?
-----------------------

.. revealjs-section::
    :data-transition: zoom

`github:Nekmo/mitmproxy-presentacion <https://github.com/Nekmo/mitmproxy-presentacion>`_

.. revealjs-notes::

   Además de la presentación, por si queréis volver a verla.

.. revealjs-break::
    :data-background-color: #ffffff
    :data-background-size: contain
    :data-background-image: _static/qr.png
    :notitle:

.. revealjs-notes::

   Además aquí la tenéis en forma de QR por si os es más cómodo, para no tener ni que escribir.

**Contactar**
-------------

* **Sitio web:** `nekmo.com <https://nekmo.com>`_
* **Email:** `contacto@nekmo.com <mailto:contacto@nekmo.com>`_
* **Twitter:** `@nekmocom <https://twitter.com/nekmocom>`_
* **Telegram:** `@nekmo <https://t.me/nekmo>`_
* **Jabber:** `nekmo@nekmo.org <xmpp://nekmo@nekmo.org>`_

.. revealjs-notes::

   Finalmente, también tenéis mi sitio web (ejem ejem spam) en esta diapositiva. Además de mi email. Y Twitter.
   Aunque apenas escriba en Twitter. Me podéis escribir ya sea por preguntas sobre Python, seguridad informática,
   contrataciones o lo que necesitéis. Mi correo está abierto. Pero ante todo, ¡muchas gracias a todos por venir!
   ¿Alguna pregunta?
