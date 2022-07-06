SI FALTA ALGUN TIPO DE PERMISO, PONER SUDO DELANTE



Ejecutar:
    $ docker run nombre-contenedor
    Descarga el contenedor si no está en el pc y luego lo ejecuta. 


Decargar:
    $ docker pull nombre-contenedor
    Descarga pero no ejecuta.


Mostrar imagenes:
    $ docker images 

Contenedores corriendo:
    $ docker ps

Los ultimos contenedore ejecutados:
    $ docker ps -a

Crear un contenedor:
    $ vim Dockerfile        #Con ese nombre 
    Una vez terminado, <esc> y escribimos :w para guardar y :q para salir

Hacer imagen:
    $ sudo docker build -t hola-php .

        """
        ---> e221b3dd3463
        Step 2/3 : COPY . /usr/src/myapp
        ---> 3ec8a8a3a8d2
        Step 3/3 : EXPOSE 80
        ---> Running in 0ff6320ec591
        Removing intermediate container 0ff6320ec591
        ---> 52377ab1309b
        Successfully built 52377ab1309b
        Successfully tagged hola-php:latest
        """

Correr imagen: 
    $ sudo docker run -p 80:80 hola-php
    El -p 80:80 es para poder acceder desde afuera del contenerdo al purto 80 oo cual quier otro puesto en EXPOSE


Ver imagenes guardadas:
    $ docker images
