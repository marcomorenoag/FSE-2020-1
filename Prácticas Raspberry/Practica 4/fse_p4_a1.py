
import serial
import os, time

# Activa la comunicacion serial

port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=1)

for i in range(0,16):
	port.write(str(i) + ": FSE 2020-1 Comunicacion UART RPi - FSE\n\r")

