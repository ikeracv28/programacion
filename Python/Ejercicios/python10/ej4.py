'''
Ejercicio 4: Calcular el Promedio de Cada Fila
Enunciado: Crea una matriz de 3x4 con valores enteros de tu elección. Calcula y muestra el promedio de los valores en cada fila de la matriz.
Ayuda:
Puedes crear la matriz con np.array([[..], [..], [..]]).
Para calcular el promedio de cada fila, utiliza np.mean(matriz, axis=1), donde axis=1 especifica que queremos el promedio por fila.
'''

#Importamos a la libreria
import numpy as np

#creamos la matriz que nos pide
matriz =  np.array([[1,2,3,4], [4,5,6,7], [8,9,10,11]])

#calculamos el promedio
promedio =  np.mean(matriz, axis=1)

#mostramos el promedio
print(promedio)