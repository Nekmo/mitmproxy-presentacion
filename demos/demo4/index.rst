Demo4
=====
En esta otra demo se utiliza una Raspberry PI 3 (otros modelos pueden estar soportados) para conectar los dispositivos
de los usuarios para realizar una ataque mitm a los mismos.

Esta misma documentación se encuentra basada en: https://www.dinofizzotti.com/blog/2022-04-24-running-a-man-in-the-middle-proxy-on-a-raspberry-pi-4/
Ten en cuenta que según tu entorno, los cambios de la distribución y otros factores, tendrás que realizar cambios a lo
que se encuentra en esta documentación.

Requisitos
----------
Se necesitan los siguientes elementos para realizar esta demo:

* Una **Raspberry PI**. Se recomienda modelo 3B+ o superior.
* **Alimentador de corriente**. Se recomienda oficial para evitar inestabilidad y corrupción de la tarjeta.
* Tarjeta **microSD** para el sistema operativo con **raspbian** a la última versión.
* **Adaptador Wifi** USB adicional. No se requiere que tenga modo AP, pero mejor si lo tiene (si se quiere utilizar
  en lugar del incorporado para la víctima).

Aunque no es imprescindible, se recomienda:

* **Conexión alámbrica** a través de cable RJ45 para la configuración. La conexión puede realizarse usando ssh.
* **Conexión a monitor** a través de cable HDMI, para la depuración.
* **Teclado** para interactuar por si fuese necesario.

Preparación del sistema
-----------------------
Lo primero es actualizar el sistema e instalar los paquetes requeridos.

.. code-block:: bash

    ~ # apt update
    ~ # apt upgrade

Tras actualizar, se recomienda reiniciar el sistema. Después instalar los paquetes necesarios:

.. code-block:: bash

    ~ # apt install dhcpcd isc-dhcp-server hostapd iptables python3-pip python3-venv

Ten en cuenta que según el *adaptador wifi* que utilices necesitarás también instalar paquetes adicionales. En mi caso
con Realtek:

.. code-block:: bash

    ~ # apt install firmware-realtek

Entre los paquetes instalados encontramos:

* **dhcpcd:** será el cliente DHCP que usará el adaptador wifi que dará Internet a nuestra RPI.
* **isc-dhcp-server:** servidor DHCP que usará el adaptador wifi al que se conectará la víctima.
* **hostapd:** permite crear la red Access Point de las víctimas y su autenticación.
* **iptables:** permite el enrutamiento para que el adaptador wifi de la víctima pase por mitmproxy.
* **python3-pip:** instalador de paquetes de Python. Lo necesitaremos para instalar *mitmproxy*.
* **python3-venv:** creador de entornos virtuales de Python. Lo necesitaremos para crear el entorno de *mitmproxy*.

Establecer conectores inalámbricos
----------------------------------
Aunque es opcional, recomiendo definir los nombres de los identificadores wifi, ya que podrían intercambiarse los
nombres. Podemos ver estos usando:

.. code-block:: bash

~ # ip a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
        link/ether b8:27:eb:11:22:33 brd ff:ff:ff:ff:ff:ff
        inet 192.168.88.101/24 brd 192.168.88.255 scope global dynamic noprefixroute eth0
           valid_lft 506sec preferred_lft 431sec
        inet6 fe80::d629:bb3d:1122:3344/64 scope link
           valid_lft forever preferred_lft forever
    3: wlan1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
        link/ether 00:f5:05:11:22:33 brd ff:ff:ff:ff:ff:ff
    4: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
        link/ether b8:27:eb:11:22:33 brd ff:ff:ff:ff:ff:ff
        inet 192.168.42.1/24 brd 192.168.42.255 scope global noprefixroute wlan0
           valid_lft forever preferred_lft forever
        inet6 fe80::f415:7aac:1122:3344/64 scope link
           valid_lft forever preferred_lft forever

Para establecerlos creamos el fichero ``/etc/udev/rules.d/10-network.rules`` y los definimos::

    # /etc/udev/rules.d/10-network.rules
    SUBSYSTEM=="net", ACTION=="add", ATTR{address}=="b8:27:eb:11:22:33", NAME="wlan0"
    SUBSYSTEM=="net", ACTION=="add", ATTR{address}=="00:f5:05:11:22:33", NAME="wlan1"

Si hace falta reiniciaremos nuestra RPI para que los identificadores tengan los nombres correctos.

Configuración de red Internet
-----------------------------
Lo primero es conseguir Internet en nuestra RPI a través de la red inalámbrica que hayamos escogido que hará esta
función. En mi caso, será el adaptador inalámbrico USB, identificado como *wlan1*. Para ello creamos el fichero
``/etc/network/interfaces.d/wlan1``, dejando que el sistema (``network.service``) lo configure por nosotros::

    # /etc/network/interfaces.d/wlan1
    allow-hotplug wlan1
    iface wlan1 inet dhcp
            wpa-ssid <ssid móvil que nos proporciona Internet>
            wpa-psk <clave móvil que nos proporciona Internet>


Configuración de red atacante
-----------------------------
Este es el paso más complicado. Configuraremos la red del atacante, para lo cual tendremos que crear una red, poniendo
nuestro Wifi como un Access Point (AP). También necesitamos un servidor DHCP que dé dirección a nuestras víctimas.

Lo primero configuraremos la red. Para ello copiamos el fichero de ejemplo de *hostapd* y lo modificaremos:

.. code-block:: bash

    ~ # cp /usr/share/doc/hostapd/examples/hostapd.conf /etc/hostapd/
    ~ # nano /etc/hostapd/hostapd.conf

En el fichero descomentaremos las líneas que necesitemos para dejar los siguientes valores::

    interface=wlan0
    driver=nl80211
    ssid=<nombre de nuestra red atacante>
    country_code=ES
    hw_mode=g
    channel=6
    macaddr_acl=0
    auth_algs=1
    wmm_enabled=0
    wpa=2
    wpa_passphrase=<clave de nuestra red atacante>
    wpa_key_mgmt=WPA-PSK
    wpa_pairwise=TKIP
    rsn_pairwise=CCMP

Ahora modificaremos el fichero ``/etc/default/hostapd`` para establecer el fichero de configuración que debe usar::

    # /etc/default/hostapd
    DAEMON_CONF="/etc/hostapd/hostapd.conf"

El servicio *hostapd* no inicia por defecto porque está enmascarado. Deberemos quitarle la máscara y activarlo:

.. code-block:: bash

    ~ # systemctl unmask hostapd.service
    ~ # systemctl enable hostapd.service

Ahora configuraremos el servidor dhcp. Para ello modificamos el fichero ``/etc/dhcp/dhcpd.conf`` y descomentaremos la
línea que dice ``authoritative``::

    # /etc/dhcp/dhcpd.conf

    # If this DHCP server is the official DHCP server for the local
    # network, the authoritative directive should be uncommented.
    authoritative;

Después añadiremos justo después la configuración de la red::

    # /etc/dhcp/dhcpd.conf
    # If this DHCP server is the official DHCP server for the local
    # network, the authoritative directive should be uncommented.
    authoritative;

    subnet 192.168.42.0 netmask 255.255.255.0 {
            range 192.168.42.10 192.168.42.250;
            option broadcast-address 192.168.42.255;
            option routers 192.168.42.1;
            option domain-name "local";
            option domain-name-servers 8.8.8.8, 8.8.4.4;
    }

Tras guardar, cambiamos la interfaz en la que trabajará el servidor DHCP, comentando la interfaz IPv6, editando el
fichero ``/etc/default/isc-dhcp-server``::

    # /etc/default/isc-dhcp-server
    INTERFACESv4="wlan0"
    #INTERFACESv6=""

En mi caso, ha sido necesario forzar que reintente el inicio del servicio en caso de error, ya que durante el arranque
del sistema cuando se inicia este servicio aún no está disponible la interfaz de red. Para ello editamos el servicio:

.. code-block:: bash

   systemctl edit isc-dhcp-server

Y ponemos en el nuevo fichero::

    [Service]
    # Type=forking
    Restart=always

Mitmproxy
---------
Para utilizar mitmproxy no utilizaremos *root*, ya que se considera inseguro. Para ello crearemos un nuevo usuario:

.. code-block:: bash

    ~ # adduser pi

Tras configurarlo, accedemos al mismo y a su directorio de trabajo:

.. code-block:: bash

    ~ # su pi
    ~ $ cd

Ahora, creamos un *virtualenv* para **mitmproxy** llamado *env* y lo instalamos en el mismo.

.. code-block:: bash

    ~ $ python3 -m venv env
    ~ $ ~/env/bin/pip install mitmproxy

Ahora volvemos al usuario *root*, ya sea escribiendo *exit* (y pulsando enter) en la terminal o pulsando *Ctrl+D*.
Crearemos el script que iniciará *mitmproxy* en ``/usr/local/bin/start_mitmweb.sh``:

.. code-block:: bash

    ~ # nano /usr/local/bin/start_mitmweb.sh

Pondremos como contenido::

    #!/bin/bash
    /home/pi/env/bin/mitmweb --mode transparent --web-port 9090 --web-host 0.0.0.0

Daremos permisos de ejecución al fichero usando:

.. code-block:: bash

    ~ # chmod +x /usr/local/bin/start_mitmweb.sh

Crearemos el servicio de systemd que iniciará este script en ``/etc/systemd/system/mitmweb.service``::

    # /etc/systemd/system/mitmweb.service

    [Unit]
    Description=mitmweb service
    After=network.target

    [Service]
    Type=simple
    User=pi
    ExecStart=/usr/local/bin/start_mitmweb.sh
    Restart=always
    RestartSec=5

    [Install]
    WantedBy=multi-user.target

Ahora lo habilitamos para que se inicie con el sistema:

.. code-block:: bash

    ~ # systemctl enable mitmweb.service

Iptables
--------
Podemos utilizar ``iptables-save`` y ``iptables-restore`` para guardar y restaurar las reglas, pero en mi caso por
sencillez he preferido crear un servicio de systemd que las añada cada vez, ya que así puedo editarlas más fácilmente.
Para ello crearemos el script que añadirá las reglas en ``/usr/local/bin/mitmproxy-iptables.sh``:

.. code-block:: bash

    ~ # nano /usr/local/bin/mitmproxy-iptables.sh

Pondremos como contenido::

    #!/usr/bin/env bash
    iptables -A FORWARD -i wlan1 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
    iptables -A FORWARD -i wlan0 -o wlan1 -j ACCEPT
    iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE
    iptables -t nat -A PREROUTING -i wlan0 -p tcp -m tcp --dport 80 -j REDIRECT --to-ports 8080
    iptables -t nat -A PREROUTING -i wlan0 -p tcp -m tcp --dport 443 -j REDIRECT --to-ports 8080

Estas reglas se encargan de enrutar el tráfico de *wlan0* a través de los puertos de *mitmproxy*. Después añadimos
permisos de ejecución al script:

.. code-block:: bash

    ~ # chmod +x /usr/local/bin/mitmproxy-iptables.sh

Crearemos el servicio de systemd que iniciará este script en ``/etc/systemd/system/mitmproxy-iptables.service``::

    # /etc/systemd/system/mitmproxy-iptables.service

    [Unit]
    Description=mitmproxy iptables service
    After=network.target

    [Service]
    Type=simple
    User=root
    ExecStart=/usr/local/bin/mitmproxy-iptables.sh
    Restart=no
    RestartSec=5

    [Install]
    WantedBy=multi-user.target

Ahora lo habilitamos para que se inicie con el sistema:

.. code-block:: bash

    ~ # systemctl enable mitmproxy-iptables.service

Por defecto nuestro sistema no permite redirigir el tráfico de una IP a otra, por lo que tendremos que habilitarlo en
el fichero ``/etc/sysctl.conf``::

    # /etc/sysctl.conf
    # Descomentar la siguiente línea para activar la redirección de paquetes para IPv4
    net.ipv4.ip_forward=1

Demo
----
Reiniciamos nuestra RPI y... si todo va bien, ¡deberíamos tenerlo funcionando! Recuerda tener previamente iniciada la
red Wifi que dará Internet a tu RPI. Para comprobar que funcione correctamente, con un dispositivo móvil que hará de
víctima, busca el nombre de red que has elegido y pon la contraseña.

Es probable que el móvil diga que dicha red tiene conectividad limitada. Debe ignorarse el aviso. Esto es porque
detecta que las conexiones HTTPS no están dando como respuesta un certificado válido. En el ordenador, el cual estará
conectado a la misma red que ofrece Internet a tu RPI, deberás poner la IP de esta (con la dirección que tiene en la
interfaz que da Internet) seguido del puerto "9090" en el navegador para ver las solicitudes::

    http://<ip RPI>:9090

