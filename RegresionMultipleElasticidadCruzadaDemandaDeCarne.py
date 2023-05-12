# -*- coding: utf-8 -*-
"""
Created on Thu May 11 23:05:47 2023

@author: nicol
"""

import pandas as pd
print(pd.__version__)

# Paso 1: cargar datos desde un archivo Excel ->
data = pd.read_excel(r'C:\\NICOLAS\\FACULTAD\UCALP\\MATERIAS\\Seminario\\TP FINAL\\ModeloEconometrico\\DatosLimpios.xlsx', sheet_name='Datos')

# Paso 2: realizar el procesamiento y análisis de los datos

# Obtener los nombres de las columnas
nombres_columnas = data.columns
# Imprimir los nombres de las columnas
print(nombres_columnas)


# tendria que dejar solo los datos de la elasticidad cruzada, que ya calculé en el Excel ->

#data.drop(columns=[
#    'Consumo carne bovina',
#    'Consumo carne aviar',
#    'Consumo carne porcina',
#    'Precio carne bovina',
#    'Precio carne aviar',
#    'Precio carne porcina'
#    ], inplace=True)

# elimino las dos primeras filas (para que no muestre el NaN) ->
data = data.drop(range(0, 5), axis=0)
#elimno los comentarios de abajo en el excel ->
data = data.drop(range(42, 49), axis=0)

print(data)
# ...

# Paso 3: ahora voy a hacer la división de los datos en un conjunto de entrenamiento y uno de prueba ->

# importo la biblioteca ->
from sklearn.model_selection import train_test_split

# dividir los datos en características (X) y variable objetivo (y):
X = data[['Precio carne aviar', 'Precio carne porcina']]  # Características (precio del pollo y del cerdo)
y = data['Consumo carne bovina']  # Variable objetivo (demanda de carne)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)

print('Dimensiones de X_train:', X_train.shape)
print('Dimensiones de X_test:', X_test.shape)
print('Dimensiones de y_train:', y_train.shape)
print('Dimensiones de y_test:', y_test.shape)

# ...

# Paso 4: Armar el modelo de Regresión múltiple ->
# ...




