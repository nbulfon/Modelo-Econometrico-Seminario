# -*- coding: utf-8 -*-
"""
Created on Thu May 11 23:05:47 2023

@author: nicol
"""

import pandas as pd
print(pd.__version__)

# Cargar datos desde un archivo Excel
data = pd.read_excel(r'C:\\NICOLAS\\FACULTAD\UCALP\\MATERIAS\\Seminario\\TP FINAL\\ModeloEconometrico\\DatosLimpios.xlsx', sheet_name='Datos')

# Realizar el procesamiento y análisis de los datos

# Obtener los nombres de las columnas
nombres_columnas = data.columns
# Imprimir los nombres de las columnas
print(nombres_columnas)


# tendria que dejar solo los datos de la elasticidad cruzada, que ya calculé en el excel ->

data.drop(columns=[
    'Consumo carne bovina',
    'Consumo carne aviar',
    'Consumo carne porcina',
    'Precio carne bovina',
    'Precio carne aviar',
    'Precio carne porcina'
    ], inplace=True)

# elimino las dos primeras filas (para que no muestre el NaN) ->
data = data.drop(range(0, 5), axis=0)
#elimno los comentarios de abajo en el excel ->
data = data.drop(range(42, 49), axis=0)

print(data)
# ...