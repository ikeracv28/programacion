import numpy as np


matriz = np.random.randint(1, 11, size=(3, 3))


def crear_archivo_matriz():
    try:
        with open('matriz.txt', 'w') as archivo:
            for fila in matriz:
                archivo.write(','.join(map(str, fila)) + "\n")
    except FileNotFoundError:
        print('El archivo no fue encontrado.')


crear_archivo_matriz()


def leer_matriz():
    try:
        with open('matriz.txt', 'r') as archivo:
            # Leer cada línea, separar por comas y convertir los valores a enteros
            matriz = [list(map(int, linea.strip().split(','))) for linea in archivo]
            # Convertir la lista a un array bidimensional de Numpy
            array_matriz = np.array(matriz)
            return array_matriz
    except FileNotFoundError:
        print('El archivo no fue encontrado.')


array_matriz = leer_matriz()

if array_matriz is not None:
    print("Matriz leída desde el archivo:")
    print(array_matriz)

