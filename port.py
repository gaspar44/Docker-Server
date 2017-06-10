# Importando modulos necesarios
import socket  # Para poder trabajar con puertos

# Creando el socket
sock = socket.socket()
# Definiendo las función que verifica
def escaner(servidor,puerto):
	try:
		sock.connect((servidor,puerto))  # Conectamos al servidor y a su puerto
		return True  # Si se conecta con exito, devolvemos True

	except ConnectionRefusedError:
		return False # En caso de error devolvemos False

for i in range(23,50):
	if escaner("localhost",i):
		print("El puerto: ",i," está abierto")
	else:
		print("El puerto: ",i," está cerrado :(")