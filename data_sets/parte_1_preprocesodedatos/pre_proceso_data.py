#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 04:12:12 2019

@author: skull
"""
#Preprocesando del dato 

#Como importar librerias

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar el data set 
dataset = pd.read_csv('Data.csv')
#Con iloc se visualiza la informadion
#del dataset dependiendo de los deseado por columna o por fila
X= dataset.iloc[:, :-1].values
print(X)
Y =dataset.iloc[:,3].values
print(Y)

#Se desea realizar un tratamiento a los N/A

from sklearn.preprocessing import Imputer
# Crear objeto de la clase
#Con esta libreria vamos a reemplezar valores nan dependiendo
# de lo deseado: la opcion strategy de refiere a los que deseamos
#aplicar a los valores en este caso se usa el mean que se 
#relaciona a la media, la opcion axis se refiere a donde sea
#aplicarlo si por fila o por columna: Columna = 0 y Fila=1
  
imputer = Imputer (missing_values= "nan", strategy="mean",axis=0)
#se usa la matriz creada en la linea 20 con valor X
imputer=imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:,1:3])


