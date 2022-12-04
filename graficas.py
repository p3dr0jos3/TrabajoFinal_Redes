# -*- coding: utf-8 -*-
"""
Created on Sat May 21 17:44:54 2022

@author: Pedro Sánchez
"""

import pandas as pd
import matplotlib.pyplot as plt
import statistics

dataframe = pd.read_csv("toma2.csv")

def tasa_transferencia_instantanea (dataframe: pd.DataFrame()) -> None:
    df= dataframe[["Time","Length"]]
    
    list_sec= []
    list_byte= []
    for i in range(len(dataframe)):
        list_sec.append(df.iloc[i]['Time'])
        list_byte.append(df.iloc[i]['Length'])
    
    tasa= []
    new_list= []
    tamano = 0
    iterativo0 = 0
    for i in range(2,len(list_sec)):
        delta= (list_sec[i])-(list_sec[i-1]) 
        if tamano == 0:
            tamano = (list_byte[i])+(list_byte[i-1])
        if delta == 0:
            iterativo0 = iterativo0 + 1
            tamano = tamano + (list_byte[i])
        else:
            tasa.append(tamano/((iterativo0 + 2) * delta * 1000000))
            new_list.append(list_sec[i])
            iterativo0 = 0
            tamano = 0
            
    x= new_list
    y= tasa
    #crear gráfica
    plt.plot(x,y)
    plt.title("Tasa de transferencia instantánea")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Tasa de transferencia (Mbps)")
    plt.show()
    
    prom= statistics.mean(tasa)
    print("La tasa de transferencia promedio durante la transmisión fue de "+ str(prom) +" Mbps.")

    return None
    
tasa_transferencia_instantanea(dataframe)
