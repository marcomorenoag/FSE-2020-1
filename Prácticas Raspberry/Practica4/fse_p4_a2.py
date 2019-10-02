import re
import serial
import os, time

# Activa la comunicacion serial

port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=1)

cadena = ""
contenido = []

while True:
	#Leemos el caracter
	caracter = port.read()
	#Agregamos el caracter a la cadena actual
	cadena += caracter
	#Si encuentra el retorno de carro
	if(caracter == chr(13)):
		#Separamos el contenido de la cadena
		contenido = cadena.split(',',3)
		intNum = contenido[0]
		iniciales = contenido[1]
		bandera = contenido[2]
		voltaje = contenido[3]
		#Verificamos que el numero se encuentre enrte 0 y 4096
		print(intNum)
		if(int(intNum,10) >= 0 and int(intNum,10) <= 4096):
			print("Numero entero = " + intNum)
		else:
			print("Error no es un numero en el rango establecido")

		#Validacion de  las iniciales
		reResult = re.match("[a-zA-Z]+", iniciales)
		if(reResult is not None):
			print("Iniciales = " + iniciales)
		else:
			print("Error en las iniciales")

		#Validacion de bandera
		if(int(bandera, 10) == 1 or int(bandera, 10) == 0):
			print("Bandera = " + bandera)
		else:
			print("Error, no es una bandera valida")

		#Validacion de voltaje
		if(float(voltaje) >= 0.0 and float(voltaje) <= 3.3):
			print("Voltaje = " + voltaje)
		else:
			print("Voltaje invalido")

		print(cadena)
		print(contenido)
		cadena = ""

