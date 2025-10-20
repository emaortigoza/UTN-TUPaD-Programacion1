""" 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300 """

precios_frutas = {
     'Banana': 1200, 
     'Ananá': 2500, 
     'Melón': 3000, 
     'Uva': 1450
     }

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

""" 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800 """

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

""" 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios. """

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)


""" 4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe. """

agenda_telefonica = {}
for _ in range(2):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    agenda_telefonica[nombre] = numero
    
consulta = input("Ingrese el nombre del contacto a consultar: ")
if consulta in agenda_telefonica:
    print(f"El número de {consulta} es {agenda_telefonica[consulta]}")
else:
    print(f"No existe un contacto con el nombre {consulta}")

print(agenda_telefonica)


""" 5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra. """

frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print("Cantidad de veces que aparece cada palabra:", contador_palabras)


""" 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno. """

alumnos_notas = {}
for _ in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1} de {nombre}: "))
        notas.append(nota)
    alumnos_notas[nombre] = tuple(notas)
for alumno, notas in alumnos_notas.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es {promedio:.2f}")


"""     7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). """

parcial_1 = {10, 2, 3, 10, 5}
parcial_2 = {4, 10, 10, 7, 8}

aprobados_ambos = parcial_1.intersection(parcial_2)
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)
aprobados_solo_uno = parcial_1.symmetric_difference(parcial_2)
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno)
aprobados_al_menos_uno = parcial_1.union(parcial_2)
print("Estudiantes que aprobaron al menos un parcial:", aprobados_al_menos_uno)



""" 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe """

stock_productos = {}
while True:
     accion = input("Ingrese 'consultar', 'agregar' o 'salir': ").lower()
     if accion == 'salir':
          break
     elif accion == 'consultar':
          producto = input("Ingrese el nombre del producto a consultar: ")
          if producto in stock_productos:
               print(f"El stock de {producto} es {stock_productos[producto]}")
          else:
               print(f"{producto} no existe en el stock.")
     elif accion == 'agregar':
          producto = input("Ingrese el nombre del producto a agregar o actualizar: ")
          cantidad = int(input("Ingrese la cantidad a agregar: "))
          if producto in stock_productos:
               stock_productos[producto] += cantidad
          else:
               stock_productos[producto] = cantidad
          print(f"Stock actualizado: {producto} tiene ahora {stock_productos[producto]} unidades.")
     else:
          print("Acción no reconocida. Por favor, intente de nuevo.")
print("Stock final de productos:", stock_productos)


""" 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora. """

agenda_eventos = {
     ("Lunes", "10:00"): "Reunión de equipo",
     ("Martes", "14:00"): "Clase de yoga",
     ("Miércoles", "09:00"): "Cita con el dentista",
}

dia = input("Ingrese el día del evento a consultar: ")
hora = input("Ingrese la hora del evento a consultar (formato HH:MM): ")
evento = agenda_eventos.get((dia, hora), "No hay ningún evento programado para ese día y hora.")
print(evento)


""" 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores. """

paises_capitales = {
     "Argentina": "Buenos Aires",
     "Brasil": "Brasilia",
     "Chile": "Santiago",
     "Perú": "Lima",
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print(capitales_paises)

