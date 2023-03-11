.. image:: https://raw.githubusercontent.com/Nekmo/mitmproxy-presentacion/master/logo.png
    :width: 100%

|

.. image:: https://img.shields.io/github/workflow/status/Nekmo/mitmproxy-presentacion/Build.svg?style=flat-square&maxAge=2592000
  :target: https://github.com/Nekmo/mitmproxy-presentacion/actions?query=workflow%3ABuild
  :alt: Latest CI build status


==================================
mitmproxy: ataques MitM con Python
==================================

Presentación para `Python Málaga <https://www.meetup.com/es-ES/python_malaga/>`_ el día *TBA*. Puedes
utilizar esta misma presentación, íntegra o con modificaciones para cualquiera de los usos descritos en la licencia
MIT adjunta en este proyecto.

La presentación está `disponible online <https://nekmo.github.io/mitmproxy-presentacion/>`_ ya compilada
para su visualización.

Para compilar desde el código fuente se requiere Python 3 instalado, estando probado sólo bajo Python 3.10. Se
recomienda ejecutar los siguientes pasos en un
`virtualenv <https://nekmo.com/es/blog/python-virtualenvs-y-virtualenvwrapper/>`_::

    # Clonar proyecto
    git clone https://github.com/Nekmo/mitmproxy-presentacion.git
    cd mitmproxy-presentacion
    # Instalar dependencias
    pip install -r requirements.txt
    # Compilar ficheros de estilos
    sassc _static/theme.scss _static/theme.css
    # Compilar presentación
    make revealjs

Tras la compilación puede verse los ficheros resultantes en el directorio ``_build``.


Copyright
=========
Licencia MIT. Ver fichero ``LICENSE.txt``.

Nekmo 2023.

