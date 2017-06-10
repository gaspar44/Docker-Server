# Importando los módulos necesarios
import socket

# Definiendo las variables a usar
host = "localhost"
puerto = 9999

socket1 = socket.socket()  # Creamos el socket

# Conectamos con el servidor
socket1.connect((host,puerto))

oracion = input("Ingrese oración: ")

socket1.send(oracion.encode('ascii'))  # Enviamos al servidor nuestra solicitud, diciendole que está en modo ASCII

"""
Como ahora se tiene que recibir algo del servidor, se prepara una variable que va a recibir el contenido del mensaje.
Tiene que usar el parametro de recibir el tamaño de lo que se le va a pasar
"""
numero = str(socket1.recv(1024),'ascii')  # Recibimos y traducimos a modo ASCII

# Mostramos en pantalla 
print("El tamaño es: ",numero)

socket1.close()  # Cerramos el socket