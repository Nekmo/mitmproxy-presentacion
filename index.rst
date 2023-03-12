

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

.. Hola a todos.


.. _saludo:

👋
==

.. Seguramente a muchos os llame la atención todo esto de la seguridad informática...




.. revealjs_break::
    :notitle:

.. En plan, como los *hackers* con sus capuchas negras. Aunque aquí hace demasiado calor para ponernosla.




.. _sobre-mi:

Sobre mí **Nekmo**
------------------

+------------------------------------+
|                                    |
| .. image:: images/cara.svg         |
|   :width: 200px                    |
|                                    |
| *Programando en Python desde 2006* |
|                                    |
+------------------------------------+

.. revealjs_section::
    :data-transition: concave


.. Pero antes dejadme que me presente. Soy Juan José, más conocido en redes como Nekmo, y llevo programando en
   Python más de media vida.


.. _hispasec

.. revealjs_break::
    :notitle:

.. Y todo esto de la seguridad no me es desconocido, gracias a que he trabajado casi 5 años en el sector, en una
   empresa malagueña llamada Hispasec.



mitmproxy
---------

.. Eso me ha permitido conocer herramientas como mitmproxy, utilizadas para realizar ataques mitm mediante un proxy.
   Pero antes de eso...


.. revealjs_section::
    :data-transition: concave

.. ¿Cuántos sabríais explicar qué es un proxy? ¿Y un ataque Man in the Middle? -- No os preocupéis, que vamos a verlos
   en detalle.



¿Qué son los proxies?
=====================

.. Lo primero, ¿qué son los proxies?


.. revealjs_break::
    :notitle:

.. Un servidor proxy es un dispositivo que hace de intermediario en las peticiones realizadas entre un cliente y un
   servidor.


.. revealjs_break::
    :notitle:

.. A muchos os sonarán porque se utilizan para saltarse restricciones regionales. Vamos, ver el Netflix de otro país.


.. revealjs_break::
    :notitle:

.. Así pues, el proxy toma una solicitud de un usuario, se la envía al servidor destino, y se lo entrega al usuario.


.. revealjs_break::
    :notitle:

.. Y puede que estéis pensando... ¿No puede ese servidor leer la solicitud? ¿No podría alterarla?


Ataques Man in the Middle **(MitM)**
====================================

.. Pues muy bien, un ataque Man in the Middle, consiste justamente en eso.


.. revealjs_break::
    :notitle:

.. Un ataque man in the middle, traducido como ataque de intermedario, es aquel en que un agente externo, el atacante,
   se encuentra de por medio en la comunicación.


.. revealjs_break::
    :notitle:

* Leer
* Añadir
* Modificar

.. Y puede leer, añadir o modificar a voluntad. Los proxies son sólo una de las técnicas que tienen los atacantes para
   realizar un ataque MitM.


mitmproxy
=========

.. Y ahora, sabiendo ambos conceptos, vamos a ver mitmproxy.


Versión consola
---------------

.. mitmproxy tiene una interfaz para ver y modificar las peticiones de nuestra víctima desde la consola.


Versión web
-----------

.. Además de una versión web muy resultona, pero que aún se encuentra en beta. *Como todo lo que desarrollo*


Python API
----------

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


.. Y finalmente una API para escribir en Python y realizar cambios, como modificar el servidor de destino o alterar
   la respuesta.

Demo
----

.. Pero dejadme que os lo enseñe, si es que funciona la demo, claro.


Casos de uso
============

.. Vale, y ahora os preguntaréis algunos. ¿Para qué me sirve? Pues no sólo es útil para los malos.


Sombrero blanco
---------------

* Depuración de programas
* Análisis de malware
* Tests de integración
* ... y más.

.. Los buenos, es decir, los sombreros blanco, además de los desarrolladorfes, pueden usarlo para varias cosas, como
   (leer puntos)


Sombrero negro
--------------

* Espionaje
* Robo de información
* Phishing
* ... y más.

.. Y los malos, claro está, pueden utilizarlo para hacer cosas de malos.


¿Estoy en peligro?
==================

.. Vale, puede esto os haya asustado un poco. Pero no os preocupéis. Contra los ataques Man in the Middle los buenos
   tenemos una solución.


SSL/TLS
-------

.. SSL/TLS. Por suerte, la mayoría del tráfico web actual está firmado y cifrado. Y esto significa que no pueden
   un ataque impunemente.


Aviso del navegador
-------------------

.. Si el tráfico está siendo interceptado y la web usa SSL/TLS, el navegador muestra una pantalla roja como esta.
   Tal vez alguna vez os haya salido porque el certificado no es válido.



¿Qué es el certificado?
-----------------------

.. Sin entrar en detalles, el certificado, es lo que demuestra que el servidor destino es quien dice ser. Y sólo el
   servidor destino tiene la clave privada que lo demuestra.


Certificado autofirmado
------------------------

.. El certificado de mitmproxy, es un certificado autofirmado que valida cualquier servidor. Permite suplantar cualquier
   sitio.


Sin confianza
-------------

.. Claro está, ese certificado no es de confianza. Y para que funcione requiere instalarse explícitamente en el equipo
   o navegador de la víctima. Ya no es tan sencillo...


Demo
----

.. Pero de nuevo, vamos a verlo con una demostración.


Conclusiones sobre el cifrado
=============================

* mitmproxy puede funcionar con sitios con cifrado SSL/TLS
* ... Pero debe aceptarse el certificado inválido,
    * ...o instalarse el certificado autofirmado en la máquina.


.. Por resumir un poco... (LEER).


¿Cómo se realiza el ataque entonces?
-------------------------------------

* Engañar a la víctima para que salte la pantalla en rojo.
* Engañarla para que instale el certificado autofirmado.
* Tomar posesión del dispositivo e instalar el certificado.

.. ¿Entonces qué prácticas puede realizar el atacante? Muchos ya lo habréis pensado tras estas conclusiones, pero en
   definitiva... (LEER)


¿Pero quedan sitios sin SSL/TLS?
--------------------------------

https://whynohttps.com/

.. Vale, y algunos pensaréis que esto dificulta mucho un ataque SSL/TLs. Pero muchas webs aún no lo implementan por
   defecto. Aquí tenéis un listado de sitios inseguros, entre los que destacan algunos tan importantes como baidu, el
   Google chino. Sí. Creedlo. En la web indicada tenéis el listado.


Códigos de ejemplo
==================

.. ¡Pero ahora, vamos a ver los códigos usados en el ejemplo anterior!


Demo: interceptar código WiFi
=============================

.. Y ahora, para terminar, vamos a ver un


¡Muchas gracias!
================

.. revealjs-fragments::

    **Referencias**


.. Y hasta aquí la presentación. Os agradezco a todos por venir, y aquí os dejo algunas referencias utilizadas en
   esta presentación.

¿Y la presentación?
-------------------

.. revealjs_section::
    :data-transition: zoom

`github:Nekmo/mitmproxy-presentacion <https://github.com/Nekmo/mitmproxy-presentacion>`_

.. Además de la presentación, por si queréis volver a verla.

.. revealjs_break::
    :data-background-color: #ffffff
    :data-background-size: contain
    :data-background-image: _static/qr.png
    :notitle:


.. Además aquí la tenéis en forma de QR por si os es más cómodo, para no tener ni que escribir.

Contactar
---------

* **Sitio web:** `nekmo.com <https://nekmo.com>`_
* **Email:** `contacto@nekmo.com <mailto:contacto@nekmo.com>`_
* **Twitter:** `@nekmocom <https://twitter.com/nekmocom>`_
* **Telegram:** `@nekmo <https://t.me/nekmo>`_
* **Jabber:** `nekmo@nekmo.org <xmpp://nekmo@nekmo.org>`_


.. Finalmente, también tenéis mi sitio web (ejem ejem spam) en esta diapositiva. Además de mi email. Y Twitter.
   Aunque apenas escriba en Twitter. Y ante todo, ¡muchas gracias a todos! ¿Alguna pregunta?
