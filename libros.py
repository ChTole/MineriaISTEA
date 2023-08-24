import os
import csv

class Libro:
    
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion
    
    def guardar_libro(self):
        lista_libros.append([self.titulo, self.autor, self.genero, self.puntuacion])
        with open('libros.csv', 'w', encoding='utf-8', newline='') as f:
            w = csv.writer(f)
            w.writerows(lista_libros)

# Auxiliares
def obtener_libros():
    try:
        with open('libros.csv', encoding='utf-8') as f:
            data = list(csv.reader(f, delimiter=','))
    except FileNotFoundError:
        data = []
    return data

def verificar_puntuacion(dato):
    while type(dato) != float:
        try: 
            return float(dato)
        except ValueError:
            dato = input('Ingrese puntuación numérica: ')

def crear_libro():
    titulo = input('Ingrese título: ')
    autor = input('Ingrese autor: ')
    genero = input('Ingrese género: ')
    puntuacion = input('Ingrese puntuación: ')
    puntuacion = verificar_puntuacion(puntuacion)
    libro = Libro(titulo, autor, genero, puntuacion)
    libro.guardar_libro()
    
    
def buscar_por_genero(lista):
    genero_buscado = input('Ingrese género a buscar: ')
    resultado = False
    for fila in lista:
        if fila[2].lower() == genero_buscado.lower():
            print(f'Libro: {fila[0]} - Autor: {fila[1]} - Puntuación: {fila[3]}')
            resultado = True
    if not resultado:
        print("No se encontraron coincidencias.")
    
def recomendar_por_genero(lista):
    genero_buscado = input('Ingrese género a buscar: ')
    resultado = ''
    puntuacion = 0
    for fila in lista:
        if fila[2].lower() == genero_buscado.lower():
            if float(fila[3]) > puntuacion:
                resultado = fila
    if resultado == '':
        print("No se encontraron coincidencias.")
    else:
        print(f'Libro: {resultado[0]} - Autor: {resultado[1]} - Puntuación: {resultado[3]}')
        
# Menú
opcion = ""

while opcion != '4':
    lista_libros = obtener_libros()
    os.system('cls')
    print('''
    ** Menú **
    1 - Agregar libro
    2 - Buscar libro
    3 - Recomendar por género
    4 - Salir
    ''')
    opcion = input('Su opción >>> ')
    if opcion == '1':
        crear_libro()
    elif opcion == '2':
        buscar_por_genero(lista_libros)
    elif opcion == '3':
        recomendar_por_genero(lista_libros)
    elif opcion == '4':
        print('Gracias por usar la app!')
    else:
        print('Opción inválida!')
    input('ENTER para continuar...')
        