'''
"Caza de Monstruos de Halloween"
Descripción:
En este ejercicio, se pide desarrollar un programa para capturar monstruos de Halloween como vampiros, momias y brujas. Cada monstruo tiene un nivel de dificultad para ser capturado, y el jugador debe usar objetos (como estacas, pociones o hechizos) para intentar capturarlos. 
Deberán utilizarse listas para los monstruos y objetos, diccionarios para asignarles atributos y poder interactuar con ellos, y también deberán usar bucles, condicionales, funciones, y importación de librerías.
Instrucciones:
El programa debe importar la librería random para seleccionar monstruos y calcular probabilidades de captura.
Los monstruos deben estar almacenados en una lista, y cada monstruo debe tener un nivel de dificultad de captura (por ejemplo, entre 1 y 5). Los datos de los monstruos se deben almacenar en un diccionario.
El jugador puede elegir entre diferentes objetos para intentar capturar al monstruo (estaca, poción mágica, hechizo).
Cada intento de captura tiene una probabilidad de éxito basada en el nivel de dificultad del monstruo y el objeto elegido. Esta probabilidad debe ser generada con la librería random.
El jugador tiene tres intentos por cada monstruo antes de que el monstruo escape.
El programa debe terminar cuando el jugador capture un monstruo o se quede sin intentos.
Conceptos que practican:
Bucles: Para iterar sobre los intentos del jugador y la lista de monstruos.
Condicionales: Para determinar si el monstruo ha sido capturado o no.
Funciones: Para organizar el código en bloques como la selección de monstruos, el cálculo de probabilidad de captura, etc.
Listas y diccionarios: Para almacenar monstruos, objetos y sus atributos.
Importación de librerías: Para usar la librería random.
Listas de monstruos y objetos
# Lista de monstruos y sus niveles de dificultad 
monstruos = { 'vampiro': 3, 'momia': 2, 'bruja': 4, 'esqueleto': 1, 'fantasma': 5 } 
# Lista de objetos para capturar
'''

#creamos las listas que vamos a utilizar

monstruos = [
{"monstuo": "momia", "dificultad": "2"},
{"monstuo": "zombie", "dificultad": "5"},
{"monstuo": "vampiro", "dificultad": "4"},
{"monstuo": "hombre lobo", "dificultad": "3"},
{"monstuo": "bruja", "dificultad": "1"},
{"monstuo": "gargola", "dificultad": "3"},
{"monstuo": "frankestein", "dificultad": "4"},
]

objetos = ("estaca", "hechizo", "pocion magica", "ballesta", "hacha", "varita", "espada", "escopeta", "coctel molotov" )

intentos = 3

import random


monstruo_random = random.randint(1,7)
print(f"¡¡Bienvenido a la caza de monstruos de Halloween!! ")


print(f"te ha salido {monstruos[monstruo_random]}")





