""" Enunciado 
La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las 
copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que 
utilice listas paralelas (una para titulos[] y otra para ejemplares[]). Cada título debe estar 
vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas. 
Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario 
elija salir. """

""" Requerimientos del Menú 
1. Ingresar títulos → Para agregar los títulos iniciales de los libros, el usuario indica la 
cantidad inicial. 
2. Ingresar ejemplares → Para agregar una cantidad de copias para cada título. 
3. Mostrar catálogo → Muestra todos los libros y su stock actual. 
4. Consultar disponibilidad → Busca un título específico y muestra cuántos ejemplares 
hay. 
5. Listar agotados → Muestra los títulos que tienen 0 ejemplares. 
6. Agregar título → Permite añadir un nuevo libro y sus ejemplares disponibles al 
catálogo, respetando la sincronía de los índices en las listas. 
7. Actualizar ejemplares (préstamo/devolución) → Permite modificar el stock de un 
libro, elegido por el usuario, para registrar préstamos o devoluciones. 
- Préstamo -> Disminuye en 1 la cantidad de ejemplares del libro seleccionado, 
si hay unidades suficientes. 
- Devolución -> Aumenta en 1 la cantidad de ejemplares del libro seleccionado. 
8. Salir → Termina la ejecución del programa.  """

menu_principal = [
     "1. Mostrar catálogo",
     "2. Ingresar títulos",
     "3. Ingresar ejemplares",
     "4. Consultar disponibilidad",
     "5. Listar agotados",
     "6. Agregar título",
     "7. Actualizar ejemplares (préstamo/devolución)",
     "8. Salir"
]

titulos_libros =[]

ejemplares_libros = []

while True:
     print("---- Menú Biblioteca ----")

     for opcion in menu_principal:
          print(opcion)

     print("--------------------------")

     seleccion = input("Seleccione una opción (1-8): ")

     print("--------------------------")

     if seleccion == "1":

          if not titulos_libros:
               print("El catálogo está vacío. Por favor ingrese Titulos de libros primero.")
               print("--------------------------")
               continue

          print("---Catálogo de Libros---")
         

          for i, titulo in enumerate(titulos_libros):
               print(f"{i + 1}. {titulo} - Ejemplares disponibles: {ejemplares_libros[i]}")

          print("--------------------------")

     elif seleccion == "2":

          titulo = input("Ingrese el título del libro: ")

          while titulo in titulos_libros or titulo == "":

               print("****************")
               print("Error: Título ya existe o es inválido.")
               print("Ingrese nuevamente.")
               print("****************")

               titulo = input("Ingrese el título del libro: ")

          print(f'Título "{titulo}" agregado correctamente.')
          titulos_libros.append(titulo)
          posicion = titulos_libros.index(titulo)
          ejemplares_libros.insert(posicion, 0)

     elif seleccion == "3":

          if not titulos_libros:
               print("****************")
               print("No hay títulos en el catálogo. Por favor, ingrese títulos primero.")
               print("****************")
               continue

          for i, titulo in enumerate(titulos_libros):

               print(f"{i + 1}. {titulo}")

          posicion = int(input("Seleccione el número del título para agregar ejemplares: ")) - 1

          while posicion < 0 or posicion >= len(titulos_libros):
               print("****************")
               print("Error: Selección inválida.")
               print("Ingrese nuevamente.")
               print("****************")

               posicion = int(input("Seleccione el número del título para agregar ejemplares: ")) - 1

          cantidad = int(input("Ingrese la cantidad de ejemplares: "))
          ejemplares_libros[posicion] += cantidad
          print(f"Se han agregado {cantidad} ejemplares a '{titulos_libros[posicion]}'. Total ahora: {ejemplares_libros[posicion]}")

     elif seleccion == "4":

          if not titulos_libros:
               print("****************")
               print("No hay títulos en el catálogo. Por favor, ingrese títulos primero.")
               print("****************")
               continue

          consultar_titulo = input("Ingrese el título del libro a consultar: ")

          if consultar_titulo in titulos_libros:
               posicion = titulos_libros.index(consultar_titulo)
               print(f"El libro '{consultar_titulo}' tiene {ejemplares_libros[posicion]} ejemplares disponibles.")
          else:
               print(f"El libro '{consultar_titulo}' no se encuentra en el catálogo.")
               

               print("--------------------------")
          
     elif seleccion == "5":

          if not titulos_libros:
               print("****************")
               print("No hay títulos en el catálogo. Por favor, ingrese títulos primero.")
               print("****************")
               continue

          print("---Libros Agotados---")
          agotados = False

          for i, titulo in enumerate(titulos_libros):
               if ejemplares_libros[i] == 0:
                    print(f"--{titulo}--")
                    agotados = True

          if not agotados:
               print("No hay libros agotados.")

          print("--------------------------")

     elif seleccion == "6":

          nuevo_titulo = input("Ingrese el título del nuevo libro: ")

          while nuevo_titulo in titulos_libros or nuevo_titulo == "":

               print("****************")
               print("Error: Título ya existe o es inválido.")
               print("Ingrese nuevamente.")
               print("****************")

               nuevo_titulo = input("Ingrese el título del nuevo libro: ")

          cantidad_ejemplares = int(input("Ingrese la cantidad de ejemplares disponibles: "))
          titulos_libros.append(nuevo_titulo)
          ejemplares_libros.append(cantidad_ejemplares)
          print(f'Título "{nuevo_titulo}" con {cantidad_ejemplares} ejemplares agregado correctamente.')


     elif seleccion == "7":

          if not titulos_libros:
               print("****************")
               print("No hay títulos en el catálogo. Por favor, ingrese títulos primero.")
               print("****************")
               continue

          for i, titulo in enumerate(titulos_libros):

               print(f"{i + 1}. {titulo}")

          posicion = int(input("Seleccione el número del título para actualizar ejemplares: ")) - 1

          while posicion < 0 or posicion >= len(titulos_libros):
               print("****************")
               print("Error: Selección inválida.")
               print("Ingrese nuevamente.")
               print("****************")

               posicion = int(input("Seleccione el número del título para actualizar ejemplares: ")) - 1

          accion = input("Ingrese 'P' para préstamo o 'D' para devolución: ").upper()

          if accion == 'P':
               if ejemplares_libros[posicion] > 0:
                    ejemplares_libros[posicion] -= 1
                    print(f"Préstamo realizado. Ejemplares disponibles de '{titulos_libros[posicion]}': {ejemplares_libros[posicion]}")
               else:
                    print(f"No hay ejemplares disponibles para '{titulos_libros[posicion]}'.")

          elif accion == 'D':
               cantidad = int(input("Ingrese la cantidad de ejemplares a devolver: "))
               if cantidad <= 0:
                print ("La cantidad a devolver debe ser mayor a 0.")
               else:
                    ejemplares_libros[posicion] += cantidad
                    print(f"Devolución realizada. Ejemplares disponibles de '{titulos_libros[posicion]}': {ejemplares_libros[posicion]}")
          else:
               print("Acción inválida. Por favor, ingrese 'P' o 'D'.")

     elif seleccion == "8":
          print("Saliendo del programa ...")
          print("...")
          print("Gracias por usar el sistema de gestión de la biblioteca.")
          print("--------------------------")
          break