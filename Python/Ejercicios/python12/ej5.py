'''
Ejercicio 5: Añadir Texto a un Archivo Existente
Enunciado: Crea un archivo llamado diario.txt y escribe en él una breve entrada de diario (puedes hacerlo de forma manual). Luego, escribe un programa que pida al usuario que ingrese otra entrada de diario, abra diario.txt en modo de añadido (append), agregue la nueva entrada y luego cierre el archivo. Al finalizar, muestra el contenido completo del archivo en pantalla.
'''

def creararchivo():
    try:
        with open('diario.txt', 'w') as archivo:
            archivo.write("Esto es una breve entrada")

    except FileNotFoundError:
        print('El archivo no fue encontrado.')

#Creamos otra funcion para pedir al usuario que añada una nueva linea.
def añadirusuario():
    try:
        with open('diario.txt', 'a') as archivo:
            linea= input("Introduce una nueva linea en el diario: ")
            cadena = "\n" + linea
            archivo.write(cadena)
    except FileNotFoundError:
        print('El archivo no fue encontrado.')

#Esta funcion es para leer el archivo
def mostrar_contenido ():
    try:
        with open('diario.txt', 'r') as archivo:

            print(archivo.read())
    except FileNotFoundError:
            print('El archivo no fue encontrado.')

#Mostramos el resultado

def resultado():
    creararchivo()
    añadirusuario()
    mostrar_contenido()
resultado()