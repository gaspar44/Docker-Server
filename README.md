# Docker-Server
Aplicación sencilla cliente-servidor Python, usando docker como servidor

La idea es que exista una aplicación cliente en Python que envíe al sevidor una palabra y que el servidor retorne el tamaño de la palabra.

La aplicación servidor corre desde un contenedor Docker que se conecta al puerto 9999 del localhost.

Para su ejecución, se debe de hacer:docker build -t <nombre_de_la_imagen_deseado> <ruta_del_repositorio> ; docker run --rm -p 9999:9999 -d <nombre_de_la_imagen>
