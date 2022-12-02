# -*- coding: utf-8 -*-
#%%
import socket
import os
from pythonping import *
import numpy as np
#%%

HOST = "157.253.230.90"  # Host Servidor
PORT = 21 # Puerto TCP
BUFFER_SIZE = "4096" #4096 a definir intenten con diferentes tamaños
SEPARATOR = ","
lista = []
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Creación del Socket
 



socket.bind(("0.0.0.0",45529)) #Nos permite digitar un puerto específico
socket.connect((HOST,PORT)) #Establecemos conexión con el HOST y PUERTO dados en las lineas 3 y 4
ruta = input("Ingrese el nombre del archivo: ") #Archivo que queremos descargar
enRuta = ruta.encode() #Encode de la ruta dada.
socket.send(enRuta)


#Manejo de excepciones
try:
    nuevo_archivo = r"C:\Users\Pedro Sánchez\Desktop"
    informacion = socket.recv(BUFFER_SIZE).decode() #Decode del tamaño del buffer, para dar con la información del archivo
    nom, tam = informacion.split(SEPARATOR)
    print("El nombre del archivo es: " + nom)
    print("El peso estimado del archivos: " + tam)
    pinglist = []
    with open(nuevo_archivo,"wb") as f: #Escritura/transferencia del archivo deseado

        while True: #Ciclo infinito transferencia del archivo
            print("Transfiriendo archivo...")
            pg = ping(HOST, size=1, count=1)

            bytes_read = socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break #Si no hay bytes que leer, se rompe el ciclo
                print("end")
            f.write(bytes_read) #Escritura de bytes del buffer
            pinglist.append(pg.rtt_avg_ms)
        

        
        print("Archivo recibido con éxito")
        delta_lat = np.diff(pinglist)
        jitter = abs((sum(delta_lat)/len(delta_lat)))
        print("El jitter fue de:", jitter, "ms")
        f.close()
        
#except socket.timeout as e:
    #print(e)
except:
    print("Archivo incorrecto")

socket.close()



