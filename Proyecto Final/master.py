import time
import serial
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=GPIO.HIGH)

# Activa la comunicacion serial
port = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)


cadena = ""
contenido = []

while True:
	caracter = port.read()
	cadena += caracter
	if(caracter == chr(13)):
		#Separamos el contenido de la cadena
		contenido = cadena.split(',', 3)
		print("Voltage: " + contenido[0])
		print("Celsius: " + contenido[1])
		print("Kelvin: " + contenido[2] + "\n")

		voltage = contenido[0]
		celsius = contenido[1]
		kelvin = contenido[2]

		contenido = []

		cadena = ""
