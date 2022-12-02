#%%
from ftplib import FTP, all_errors
import ftplib


import os #Se ingresó este módulo por facilidad en la hora de descargar el archivo


ftp = FTP("157.253.230.90")
usu1 = "grupo3"
#input("Por favor ingrese su usuario: ") #Se pide el usuario
pass1 = "grupo3"
#input("Por favor ingrese su contraseña: ") #Se pide la clave

try:
    ftp.login(user=usu1,passwd=pass1) #Inicio de sesión FTP mediante las credenciales dadas anteriormente

    print(ftp.getwelcome()) #Mensaje de bienvenida
    print("Se inició sesión correctamente en el cliente FTP")

    #ftp.cwd('/home/grupo3') #Se accede al directorio donde se encuentran los archivos a analizar
    #print("Ubicado exitosamente en la carpeta: "+ ftp.pwd())
    #ftp.retrlines("LIST")

    print("Se ingresó correctamente al directorio")

    os.chdir("home/grupo3") #Ruta para la descarga

    archivo = input("Por favor ingrese el nombre del archivo que desea descargar: ")
    ruta = input("Por favor ingrese la ruta de donde desee guardar el archivo: ")
    os.chdir(ruta)
    #Una vez identificado el archivo a descargar usamos el comando reservado try/except

    try:
        
        with open(archivo, "wb") as f: #Abrimos el archivo con el formato WB, write bytes.
            ftp.retrbinary("RETR " + archivo , f.write) #The method retrbinary() of the FTP class retrieves a file from the server to the local system in binary mode. 
                                                    #The method accepts a retrieval command such as RETR, and a callback function along with other paramaters.
                                                    #The method retrbinary() supports resumed FTP transfers. Using the parameter rest the position "1"
                                                    # from which the file transfer has to be made can be specified. "2"
                                                    
                                                    

            
        print("Transferencia completa con un peso estimado de: ",ftp.size(archivo), "bytes")


    except ftplib.all_errors as e: #Manejo de excepciones
        print("Errores: " +str(e))
        
except Exception as e: #Este except funciona, por ejemplo, en caso que las credenciales dadas sean incorrectas
    print("No se pudo iniciar sesión: "+str(e))
    

ftp.close()

# %%
