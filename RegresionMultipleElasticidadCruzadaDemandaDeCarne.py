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
# ...