'''
Ejercicio 1: Guardar una Lista de Números en un Archivo y Leerla como un Array
Enunciado: Escribe un programa que genere un array de Numpy con 10 números enteros aleatorios entre 1 y 100. Guarda estos números en un archivo de texto llamado numeros.txt, escribiendo cada número en una nueva línea. Luego, escribe otro programa que abra el archivo numeros.txt, lea los números y los almacene en un array de Numpy. Muestra en pantalla el array leído.

'''

import numpy as np

# Genera un array de 10 números enteros aleatorios entre 1 y 100
numeros = np.random.randint(1, 101, size=10)

# Guarda cada número en una nueva línea en el archivo 'numeros.txt'
with open("numeros.txt", "w") as file:
    for numero in numeros:
        file.write(f"{numero}\n")
        
print("Números generados y guardados en 'numeros.txt':", numeros)

# Lee los números del archivo 'numeros.txt' y almacénalos en un array de numpy
with open("numeros.txt", "r") as file:
    numeros_leidos = np.array([int(line.strip()) for line in file])

print("Array leído desde el archivo 'numeros.txt':", numeros_leidos)







