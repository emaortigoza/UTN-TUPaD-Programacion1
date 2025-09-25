

""" Enunciado
La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las
copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que
utilice listas paralelas (una para titulos[] y otra para ejemplares[]). Cada título debe estar
vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas.
Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario
elija salir.
NOTA PROHIBIDO USAR EXCEPCIONES, CLASES, DICCIONARIOS, FUNCIONES, ESTRUCTURAS DE
DATOS AVANZADAS, EN EL CASO QUE SE UTILICEN, SE CALIFICARÁ CON 10% (UNO) DE NOTA
MÁXIMA.
USAR: WHILE, ESTRUCTURA CASE PARA EL MENÚ, ESTRUCTURAS CONDICIONALES,
ESTRUCTURAS SECUENCIALES EL PYTHON, REALIZAR VALIDACIONES SOLICITADA """

titulos = []
ejemplares = []

while True:
     print("\nMenú de opciones:")
     print("1. Agregar titulos")
     print("2. Ingresar ejemplares")
     print("3. Mostrar catálogo")
     print("4. Consultar disponibilidad")
     print("5. Listar agotados")
     print("6. Agregar titulo")
     print("7. Actualizar ejemplares")
     print("8. Salir")

     opcion = input("Seleccione una opción (1-8): ")

     if opcion == '1':
          titulo = input("Ingrese el título del libro: ")
          if titulo in titulos:
               print("El título ya existe en el catálogo.")
          else:
               titulos.append(titulo)
               ejemplares.append(0)
               print(f'Título "{titulo}" agregado al catálogo con 0 ejemplares.')
     elif opcion == '2':
          titulo = input("Ingrese el título del libro para agregar ejemplares: ")
          if titulo in titulos:
               index = titulos.index(titulo)
               try:
                    cantidad = int(input("Ingrese la cantidad de ejemplares a agregar: "))
                    if cantidad > 0:
                         ejemplares[index] += cantidad
                         print(f'Se han agregado {cantidad} ejemplares al título "{titulo}".')
                    else:
                         print("La cantidad debe ser un número positivo.")
               except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
          else:
               print("El título no existe en el catálogo.")

     elif opcion == '3':
          print("\nCatálogo de libros:")
          for i in range(len(titulos)):
               print(f'Título: "{titulos[i]}", Ejemplares disponibles: {ejemplares[i]}')
     elif opcion == '4':
          titulo = input("Ingrese el título del libro para consultar disponibilidad: ")
          if titulo in titulos:
               index = titulos.index(titulo)
               print(f'Título: "{titulo}", Ejemplares disponibles: {ejemplares[index]}')
          else:
               print("El título no existe en el catálogo.")
     elif opcion == '5':
          print("\nLibros agotados:")
          agotados = False
          for i in range(len(titulos)):
               if ejemplares[i] == 0:
                    print(f'Título: "{titulos[i]}"')
                    agotados = True
          if not agotados:
               print("No hay libros agotados.")
     elif opcion == '6':
          titulo = input("Ingrese el título del libro a agregar: ")
          if titulo in titulos:
               print("El título ya existe en el catálogo.")
          else:
               titulos.append(titulo)
               ejemplares.append(0)
               print(f'Título "{titulo}" agregado al catálogo con 0 ejemplares.')

     elif opcion == '7':
          titulo = input("Ingrese el título del libro para actualizar ejemplares: ")
          if titulo in titulos:
               index = titulos.index(titulo)
               try:
                    cantidad = int(input("Ingrese la nueva cantidad de ejemplares: "))
                    if cantidad >= 0:
                         ejemplares[index] = cantidad
                         print(f'La cantidad de ejemplares para "{titulo}" ha sido actualizada a {cantidad}.')
                    else:
                         print("La cantidad debe ser un número no negativo.")
               except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
          else:
               print("El título no existe en el catálogo.")
     elif opcion == '8':
          print("Saliendo del programa. ¡Hasta luego!")
          break

     else:
          print("Opción inválida. Por favor, seleccione una opción del 1 al 8.")

