'''
Ejercicio 2: Cargar Datos de un Archivo y Calcular Estadísticas
Enunciado: Crea un archivo llamado temperaturas.txt y escribe manualmente 12 temperaturas (en grados Celsius) correspondientes a los meses de un año, cada una en una línea. Escribe un programa que lea las temperaturas del archivo y las almacene en un array de Numpy. Luego, calcula y muestra la temperatura promedio, la temperatura más alta y la más baja del año.

'''

import numpy as np

def creamosarchivo():
    try:
        with open('Temperaturas.txt', 'r') as archivo:
            archivo.write(11)
    except FileNotFoundError:
        print('El archivo no fue encontrado.')