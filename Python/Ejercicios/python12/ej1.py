'''
Ejercicio 1: Crear y Escribir en un Archivo de Texto
Enunciado: Escribe un programa que cree un archivo de texto llamado saludo.txt y escriba en él la frase "¡Hola, bienvenidos al curso de Python!". Luego, cierra el archivo.
'''
#creamos la funcion para crear y abrir el archivo
def crearyescribirarchivotexto ():

    #usamos 'with open' para abrir el archivo en modo escritura (w). Si no existe, se creará automáticamente.
    #si el archivo ya existe, se sobrescribirá.
    with open('saludo.txt', 'w') as archivo:
        archivo.write('¡Hola, bienvenidos al curso de Python!')
        archivo.close()

#creamos la funcion para leer el archivo
def leerarchivo():
    #abrimos el archimo en modo lectura (r)
    archivo = open('saludo.txt', 'r')
    #con esto leemos el archivo
    contenido = archivo.read()
    print(contenido)
    #esto se pone siempre para cerrar el archivo
    archivo.close()

#función principal donde ejecutamos las funciones de crear, escribir y leer el archivo
def main():
    crearyescribirarchivotexto()
    leerarchivo()

#llamamos a la funcion
main()