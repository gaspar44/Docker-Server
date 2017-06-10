# Importando módulos necesarios
import socketserver # Para tener del lado del servidor corriendo
import os  # Para trabajar con variables de entorno

def borrar_espacios(x):  # Funcion que carga una lista en un arreglo y quita el "\n"

	# Se carga un archivo de texto que contenga la información de la IP
	with open(x,'r') as f:
		datos = f.readlines()  # Almacenamos todos los datos del archivo aquí

	datos = datos[0]  # Tomamos lo que interesa
	datos = datos.replace("\n","")  # Reemplazamos el salto de línea por nada

	# Bucle para tomar la dirección IP del archivo
	for i in range(len(datos)):
		if datos[i] == ":":
			datos = datos[i+1:]  # Asigamos lo que está después de los dos puntos
			break  # Salimos ya que no interesa nada más

	return datos

# Creando la clase que se encargará de recibir las conexiones		
class TCPHandler(socketserver.BaseRequestHandler):  # Hereda de socket server
	def handle(self):
		self.oracion = str(self.request.recv(1024),'ascii')  # Es lo que recibe el servidor y recibe 1024 bytes
		self.size = str(len(self.oracion))  # Tomamos el tamaño de la palabra y lo convertimos a string

		# Salida de datos en el servidor
		print("la oración recibida es:",self.oracion,"y su tamaño es :",self.size)

		# Enviamos la salida al cliente
		self.request.send(bytes(self.size,'ascii'))  # Todo en bytes


# Inicio del servidor para uso local
host = borrar_espacios("IP.txt")  # Dirección IP. En el caso de correr en local, se usa localhost
puerto = os.getenv("PUERTO",9999)  # Toma la variable de entorno PUERTO y si es none asigna 9999

# Ajustamos el tipo de variable 
puerto = int(puerto)
servidor = socketserver.TCPServer((host,puerto),TCPHandler)  # Creamos el servidor con el manejador, la IP del servidor y el puerto a abrir

print("Servidor corriendo")

# Ejecutamos de forma permanente el servidor
servidor.serve_forever()