'''
Ejercicio 3: Calcular el promedio de un array
Enunciado: Crea un array de Numpy con 10 números enteros de tu elección. Calcula el promedio de los elementos y muestra el resultado.
Motivo para usar arrays: Numpy permite calcular el promedio de los elementos de un array con la función np.mean() de forma rápida y eficiente, algo que con listas requeriría escribir más código.
'''
#Importamos la libreria numpy
import numpy as np

#creamos el array
array = np.array([1,2,3,4,5,6,7,8,12,15])

#Ahora calculamos el promedio
promedio = np.mean(array)

#por ultimo mostramos el promedio
print(promedio)