# Se importan bibliotecas necesarias
import sys
import os, glob

# Cambio de directorio a donde se montan por defecto las USBs en Linux
os.chdir("/media/pi")

# Se listan todos los nombres de USBs montadas
for file in glob.glob("*"):
	targetUSB = file # Se guarda el nombre de la USB objetivo

targetPath = '/media/pi/' + str(targetUSB) # Se crea el Path final donde se guardará el archivo
filepath = os.path.join(targetPath, str(sys.argv[1])) # Se concatena el argumento (nombre de archivo) para crear el archivo

f = open(filepath, "a") # Se crea un archivo nuevo si no existe

# Se itera en función del número pasado como segundo argumento al correr el programa
for i in range(int(sys.argv[2]) + 1):
	f.write(str(i) + ",Hola USB," + "data" + str(i) + "\n")

# Cierre de flujo de datos del archivo para finalizar
f.close()
