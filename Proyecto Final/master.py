import time
import serial
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT, initial=GPIO.HIGH)

send = serial.Serial(
#    port='/dev/serial0',
    port='/dev/ttyS0',
    baudrate = 115200,
#    parity=serial.PARITY_NONE,
#    stopbits=serial.STOPBITS_ONE,
#    bytesize=serial.EIGHTBITS,
#    timeout=1
)

# i = [0,10,45,90,135,180,135,90,45,10,0]
cadena = ""

while True:
	caracter = send.read()
	cadena += caracter
	if(caracter == chr(13)):
		print(cadena)
		cadena = ""
