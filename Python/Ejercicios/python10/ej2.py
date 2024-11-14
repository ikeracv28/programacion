'''
Ejercicio 2: Sumar dos Matrices
Enunciado: Crea dos matrices de 2x3 con valores enteros de tu elección. Suma ambas matrices elemento por elemento y muestra el resultado.
Ayuda:
Usa np.array() para crear las matrices manualmente, por ejemplo, np.array([[1, 2, 3], [4, 5, 6]]).

'''
#Importamos a la libreria
import numpy as np

#creamos la matrices que nos pide
matriz1 = np.array([[1, 2, 3], [4, 5, 6]])
matriz2 = np.array([[8, 8, 9], [10, 11, 12]])

#hacemos la suma de nuestras matrices
suma = matriz1 + matriz2

#mostramos la suma
print(suma)