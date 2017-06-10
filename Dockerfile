# Descargamos la versión de python3 para poder trabajar
FROM python:3.3.6

# Ajustamos el directorio de trabajo al home
WORKDIR /root

# Copiamos el script
COPY Socket2.py .

# Instalamos varias net-tools para poder conseguir la IP del docker
RUN apt-get update && apt-get install net-tools

# Conseguimos la IP y la guardamos en un archivo de texto
RUN ifconfig eth0 | grep 172.17.0.* | awk '{ print $2 }' >> IP.txt

# Ajustamos las variables de entorno
ENV PUERTO 9999

# Ejecutamos el servidor
CMD ["python","Socket2.py"]