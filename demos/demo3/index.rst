Demo3
=====
En esta demo se muestran ejemplos con código. Para ello ejecutar cada uno de los casos.

Caso 1
------
En este caso se muestra cómo en función de un parámetro de la solicitud alteramos el contenido de la página.

.. code-block::

    mitmproxy --anticache -s ./case1.py

En este ejemplo se modifica cada palabra por "PHP", intentando no romper el diseño de la página.

Caso 2
------
Este otro caso de ejemplo altera la respuesta sin llegar a realizarse solicitud al servidor de destino.

.. code-block::

    mitmproxy -s ./case2.py
