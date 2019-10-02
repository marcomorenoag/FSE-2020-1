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
		print(cadena)
		#Separamos el contenido de la cadena
		contenido = cadena.split(',',3)
		print(contenido[0] + "\n")
		print(contenido[1] + "\n")
		print(contenido[2] + "\n")

		voltage = contenido[0]
		celsius = contenido[1]
		kelvin = contenido[2]
		port.write("Voltage: " + voltage + "\n\r")
		port.write("Celsius: " + celsius + "\n\r")
		port.write("Kelvin: " + kelvin + "\n\n\r")

		contenido = []

		cadena = ""

