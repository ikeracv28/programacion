'''
Ejercicio 3: Extraer una Columna de una Matriz
Enunciado: Crea una matriz de 4x4 con números enteros consecutivos, comenzando desde 1. Extrae y muestra la tercera columna de la matriz.
Ayuda:
Utiliza np.arange(1, 17).reshape((4, 4)) para crear la matriz de 4x4 con números consecutivos del 1 al 16.
Para extraer la tercera columna, usa la notación de índice: matriz[:, 2]. La notación : selecciona todas las filas, mientras que 2 selecciona la tercera columna.

'''

#Importamos a la libreria
import numpy as np

#creamos la matriz que nos pide
matriz =  np.arange(1, 17).reshape((4, 4))

#la mostramos
print( matriz[:, 2])