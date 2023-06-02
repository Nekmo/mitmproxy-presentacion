

.. toctree::
   :glob:
   :hidden:

   *


.. _intro:

======================================
**mitmproxy:** ataques MitM con Python
======================================

.. revealjs_section::
    :data-transition: zoom


.. image:: images/mitmproxy_logo.*
  :width: 200


.. revealjs-notes::

  Hola a todos.



.. _saludo:

👋
==

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

.. revealjs_section::
    :data-transition: concave

.. revealjs-notes::

  Pero antes dejadme que me presente. Soy Juan José, más conocido en redes como Nekmo, y llevo programando en
  Python más de media vida.



.. revealjs-break::
    :notitle:

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

  mitmproxy tiene una interfaz para ver y modificar las peticiones de nuestra víctima desde la consola.


Versión **web**
---------------

.. image:: images/mitmproxy_web.*
  :width: 100%

.. revealjs-notes::

  Además de una versión web muy resultona, pero que aún se encuentra en beta. *Como todo lo que desarrollo*


**Python** API
--------------

.. code-block:: python

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

  Y finalmente una API para escribir en Python y realizar cambios, como modificar el servidor de destino o alterar la respuesta.

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

* **Espionaje**.
* Robo de **información**.
* **Phishing**.
* ... y más.

.. revealjs-notes::

  Y ellos, claro está, también pueden utilizarlo para hacer sus cosas de malos, como (leer puntos).


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

   Vale, y algunos pensaréis que esto dificulta mucho un ataque SSL/TLs. Pero muchas webs aún no lo implementan por defecto...


Webs sin HTTPS
--------------

.. image:: images/why_not_https.*
  :width: 100%

**https://whynohttps.com/**

.. revealjs-notes::

   Vale, y algunos pensaréis que esto dificulta mucho un ataque SSL/TLs. Pero muchas webs aún no lo implementan por defecto. Aquí tenéis un listado de sitios inseguros, entre los que destacan algunos tan importantes como baidu, el Google chino. Sí. Creedlo. En la web indicada tenéis el listado.


Códigos de **ejemplo**
======================

.. revealjs-section::
    :data-background-color: #000000
    :data-background-image: _static/coding.gif

.. revealjs-notes::

  ¡Pero ahora, vamos a ver los códigos usados en el ejemplo anterior!


**Demo:** interceptar código WiFi
=================================

.. revealjs-section::
    :data-background-color: #000000
    :data-background-image: _static/demo3.gif

.. revealjs-notes::

   Y ahora, para terminar, vamos a ver un ejemplo en el que vosotros mismos podréis probar mitmproxy con vuestros mismos móviles, usando vuestra conexión WiFi. Vamos a analizar vuestro tráfico HTTP.

Accede a la **demo**
--------------------

**SSID: mitmproxy**

.. revealjs-section::
    :data-background-color: #030303


¡Muchas **gracias**!
====================

.. revealjs-fragments::

    **Referencias**

    * `mitmproxy.org <https://mitmproxy.org/>`_.
    * `mitmproxy.org <https://mitmproxy.org/>`_. TODO.

.. revealjs-notes::

   Y hasta aquí la presentación. Os agradezco a todos por venir, y aquí os dejo algunas referencias utilizadas en esta presentación.

¿Y la **presentación**?
-----------------------

.. revealjs_section::
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


.. Finalmente, también tenéis mi sitio web (ejem ejem spam) en esta diapositiva. Además de mi email. Y Twitter.
   Aunque apenas escriba en Twitter. Y ante todo, ¡muchas gracias a todos! ¿Alguna pregunta?
