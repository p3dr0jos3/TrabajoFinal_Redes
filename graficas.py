# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:44:54 2022

@author: Pedro Sánchez
"""

import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#requerimiento 0
def cargar_datos(ruta_archivo: str)->list:
    
    resultado = pd.read_csv(ruta_archivo)
    return resultado

#requerimiento 1
def diagrama_de_torta_segun_tipo_de_estacion(dataframe:pd.DataFrame)->None:
    
    estaciones = dataframe[['Nombre de la estación','Tipo de estación']].drop_duplicates()
    fijas=0
    indicativas=0

    for i in estaciones["Tipo de estación"]:
        if i == "Fija":
           fijas +=1
        elif i == "Indicativa":
             indicativas +=1
 
    tipos = 'Fija', 'Indicativa',
    sizes = [fijas,indicativas] 
    
    #Creamos el grafico
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=tipos, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.title("Distribución porcentual según tipo de estación")
    plt.show()
    return None

#requerimiento 2
def tendencia_medidas_por_rango_de_anios(dataframe:pd.DataFrame, anio_i:int, anio_f:int)->None:
    
    en_orden= dataframe.sort_values(by=["Anio"])
    anios_lista= {}
    for anio in en_orden["Anio"]:
        if anio in range(anio_i,anio_f+1):
           if anio in anios_lista:
               anios_lista[anio] +=1
           else:
                anios_lista[anio]= 1
    
    x= anios_lista.keys()
    y= anios_lista.values()
    
    #crear gráfica
    plt.plot(x,y, marker = 'o')
    plt.title("Tendencia de número de medidas de "+str(anio_i)+" a "+str(anio_f))
    plt.xlabel("Año")
    plt.ylabel("Número de medidas")
    plt.xticks(range(anio_i,anio_f+1))
    plt.show()
    return None

#requerimiento 3
def diagrama_de_barras_mediciones_o3_mayores_a(dataframe:pd.DataFrame,valor:float)->None:
    
    x=[]
    y=[]
    lista= {}
    for indice_fila, fila in dataframe.iterrows():
        if fila["Variable"] == "O3" and fila["Concentración"] > valor:
           if fila["Departamento"] in lista:
               lista[(fila["Departamento"])] +=1
           else:
               lista[(fila["Departamento"])]= 1
    
    for depto in sorted(lista, key=lista.get, reverse=False):
        x.append(depto)
        y.append(lista[depto])
     
    #crear gráfica
    plt.barh(x[-5:], y[-5:], color="steelblue")
    plt.ylabel('Departamentos')
    plt.xlabel('Número de medidas superiores a '+str(valor)+' ug/m^3')
    plt.title("Top 5 departamentos con mediciones de O^3 mayores a "+str(valor)+" ug/m^3")
    plt.show()
    
    return None


#requerimiento 4
def caja_y_bigotes_distribucion_concentraciones_CO_por_año(dataframe:pd.DataFrame,anio:int)->None:
    
    datos=[]
    for indice_fila, fila in dataframe.iterrows():
        if fila["Variable"] == "CO" and fila["Anio"] == anio and fila["Tiempo de exposición"] == 8:
           datos.append(fila["Concentración"])
           
    #crear gráfico
    plt.boxplot(datos)
    plt.xlabel("Concentración\n "+str(anio))
    plt.ylabel("Concentración")
    plt.grid(axis= 'y', color= 'gray', linestyle= 'dashed')
    plt.grid(axis= 'x', color= 'silver')
    plt.title("Distribución de medidas de CO por año")
    plt.show()
    return None

#requerimiento 5
def concentraciones_anuales_PM10_por_departamento(dataframe:pd.DataFrame,depto:str)->None:
    
    dept= depto.upper()
    lista= {}
    for indice_fila, fila in dataframe.iterrows():
        if fila["Variable"] == "PM10" and fila["Departamento"] == dept:
           if fila["Anio"] in lista:
                lista[fila["Anio"]].append(fila["Concentración"]) 
           else:
                lista[fila["Anio"]]= [(fila["Concentración"])]
    
    #promedio
    for anio in lista:
        lista[anio]= (sum(lista[anio]))/(len(lista[anio]))
    
    x= list(lista.keys())
    y= list(lista.values())
    dept= depto.capitalize()
    
    #crear gráfico
    fig, ax = plt.subplots()
    ax.bar(x,y)
    plt.title("Concentración promedio de material particulado menor a 10 micras por años en "+str(dept))
    plt.xlabel("Año")
    plt.ylabel("Concentración")
    plt.show()
    return None


#requerimiento 6
def crear_matriz(dataframe:pd.DataFrame)->tuple:
    
    ica= dataframe["ICA"].unique()
    depts= dataframe["Departamento"].unique()
    depts.sort()
    
    lista={}
    for departamento in depts:
        lista[departamento]= {"Aceptable":0,"Buena":0, "Dañina a la salud":0, "Dañina a la salud de grupos sensibles":0, "Muy dañina a la salud":0, "Peligrosa":0}
    for indice_fila, fila in dataframe.iterrows():
        lista[(fila["Departamento"])][(fila["ICA"])] +=1
        
    #Creación de la matriz
    matriz=[]
    for departamento in depts:
        a=[]
        valores= lista[departamento].values()
        valores= list(valores)
        for elemento in valores:
            a.append(elemento)
        matriz.append(a)
        
    #Esqueleto diccionarios
    ICAs =sorted(ica)
    #Diccionario con el nombre de las columnas (ICA)
    ICAs_dict = dict(list(enumerate(ICAs)))
    deptos = sorted(depts)
    #Diccionario con el nombre de las filas (Deptos)
    dept_dict = dict(list(enumerate(deptos)))
    
    return (matriz, dept_dict, ICAs_dict)

#requerimiento 7
def dar_departamento_con_mas_mediciones(tupla:tuple)->str:
    
    matriz,dept_dict, ICAs_dict= tupla
    
    mayor=0
    depto_mayor=""
    for i in range(0, len(matriz)):
        suma=0
        for j in range(0, len(matriz[0])):
            suma +=matriz[i][j]
            
            if suma > mayor:
               mayor= suma
               depto_mayor= dept_dict[i]
               
    return depto_mayor

#requerimiento 8
def contar_numero_de_mediciones_por_ica_dado(tupla:tuple, ica:str)->int:
    
    matriz,dept_dict, ICAs_dict= tupla
    
    suma=0
    corregido= ica.capitalize()
    for i in range(0, len(ICAs_dict)):
        for j in range(0, len(matriz)):
            if corregido == (ICAs_dict[i]):
               suma +=matriz[j][i]
                  
    return suma

#requerimiento 9
def mayores_mediciones_ica_y_departamento(tupla:tuple)->tuple:
    matriz= tupla[0]
    dept_dict= tupla[1]
    ICAs_dict= tupla[2]
    
    mayor=0
    for n in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if matriz[n][j] > mayor:
               mayor= matriz[n][j]
               ica= ICAs_dict[j]
               depto= dept_dict[n]
               
    return (depto,ica)

#requerimiento 10
def cargar_coordenadas(nombre_archivo:str)->dict:
    
    deptos = {}
    archivo = open(nombre_archivo, encoding="utf8")
    archivo.readline()
    linea = archivo.readline()
    while len(linea) > 0:
          linea = linea.strip()
          datos = linea.split(";")
          deptos[datos[0].upper()] = (int(datos[1]),int(datos[2]))
          linea = archivo.readline()
          
    return deptos

def departamentos_mapa(tupla:tuple)->None:
    
    matriz,dept_dict, ICAs_dict= tupla
    coords= cargar_coordenadas("coordenadas.txt")
    mapa = mpimg.imread("mapa.png").tolist()
    colores = {"Buena":[36/255,226/255,41/255], "Aceptable":[254/255,253/255,56/255], "Dañina a la salud de grupos sensibles":[252/255,102/255,33/255],"Dañina a la salud":[252/255,20/255,27/255], "Muy dañina a la salud":[127/255,15/255,126/255], "Peligrosa":[101/255, 51/255, 8/255]}
    
    lista={}
    for n in range(0,len(matriz)):
        mayor=0
        for j in range(0,len(matriz[0])):
            if matriz[n][j] > mayor:
               mayor= matriz[n][j]
               ica= ICAs_dict[j]
               depto= dept_dict[n]
               lista[depto]=ica
               
    #Pintar mapa
    for departo in lista:
        for departa in coords:
            departa.upper()
            if departo == departa:
               x= coords[departa][0]+6
               y= coords[departa][1]-6
              
               for i in range(0,14):
                   mapa[x][y] = colores[lista[departo]]
                   x-=i
                   for n in range(0,14):
                       y+=n
                       mapa[x][y] = colores[lista[departo]]  
                  
                       y-=n
                       mapa[x][y] = colores[lista[departo]]
                 
                   x+=i
                   for n in range(0,14):
                       y+=n
                       mapa[x][y] = colores[lista[departo]]
                      
                       y-=n
                       mapa[x][y] = colores[lista[departo]]
 
    #Configuraciones 
    legends = []
    for i in range(len(matriz[0])):
        legends.append(mpatches.Patch(color = colores[tupla[2][i]], label= tupla[2][i]))
    
    plt.legend(handles = legends, loc = 3, fontsize='x-small')
    plt.imshow(mapa)
    plt.show()
    return None
