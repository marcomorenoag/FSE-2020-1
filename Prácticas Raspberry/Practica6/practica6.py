# Se importan bibliotecas necesarias
import smbus, time, subprocess
import sys, os, glob

def createFile(data, creeFilaDatos):
    # Cambio de directorio a donde se montan por defecto las USBs en Linux
    os.chdir("/media/pi")

    # Se listan todos los nombres de USBs montadas
    for file in glob.glob("*"):
    	targetUSB = file # Se guarda el nombre de la USB objetivo

    targetPath = '/media/pi/' + str(targetUSB) # Se crea el Path final donde se guardará el archivo
    filepath = os.path.join(targetPath, str(sys.argv[1])) # Se concatena el argumento (nombre de archivo) para crear el archivo

    f = open(filepath, "a") # Se crea un archivo nuevo si no existe

    if(not creeFilaDatos):
        f.write("Segundos,Minutos,Horas,Día Semana,Día,Mes,Año\n")
        creeFilaDatos = True

    # Se itera en función del número pasado como segundo argumento al correr el programa
    for i in data:
        if(i == data[-1]):
            f.write(i)
        else:
            f.write(i + ",")
    f.write("\n")

    # Cierre de flujo de datos del archivo para finalizar
    f.close()

    return creeFilaDatos

def formatExit(timeList):
    for i in range(len(timeList)):
        timeList[i] = hex(timeList[i]).rstrip("L").lstrip("0x") or "0"
    return timeList

def i2cCommunication(creeFilaDatos):
    bus = smbus.SMBus(1)
    time.sleep(1) #wait here to avoid 121 IO Error

    DEVICE_ADDRESS = 0x68      #7 bit address (will be left shifted to add the read write bit)
    DEVICE_REG_MODE1 = 0x00

    # Read a single register
    try:
        b = bus.read_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 7)
        valor = createFile(formatExit(b), creeFilaDatos)
    except IOError:
        subprocess.call(['i2cdetect', '-y', '1'])

    bus.close()
    return valor


if __name__ == "__main__":
    creeFilaDatos = False
    while(True):
        creeFilaDatos = i2cCommunication(creeFilaDatos)

