
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
8. Salir → Termina la ejecución del programa.  """""

opciones_menu = ["1. Ingresar títulos",
                 "2. Ingresar ejemplares disponibles",
                 "3. Mostrar catálogo",
                 "4. Consultar disponibilidad",
                 "5. Listar agotados",
                 "6. Agregar título",
                 "7. Actualizar ejemplares (préstamo/devolución)",
                 "8. Ver catalogo completo",
                 "9. Salir"]

titulos = []
ejemplares = []

while True:
     print("---- Menu Biblioteca ----")

     for opcion in opciones_menu:
          print(opcion)

     seleccion = input("Seleccione una opción (1-9): ")

     print("--------------------------")

     if seleccion == "1":

          titulo = input("Ingrese el título del libro: ")

          while titulo in titulos or titulo == "":

               print("****************")
               print("Error: Título ya existe o es inválido.")
               print("Ingrese nuevamente.")
               print("****************")

          print(f'Título "{titulo}" agregado correctamente.')
          titulos.append(titulo)
          posicion = titulos.index(titulo)
          ejemplares.insert(posicion, 0)

     elif seleccion == "2":
          
          if not titulos:
               print("No hay títulos en el catálogo. Por favor, ingrese títulos primero.")
               continue

          for i, titulo in enumerate(titulos):
               print(f"{i + 1}. {titulo}")

          posicion = int(input("Seleccione el número del título para agregar ejemplares: ")) - 1

          while posicion < 0 or posicion >= len(titulos):
               print("****************")
               print("Error: Selección inválida.")
               print("Ingrese nuevamente.")
               print("****************")
               posicion = int(input("Seleccione el número del título para agregar ejemplares: ")) - 1

          cantidad = int(input("Ingrese la cantidad de ejemplares: "))
          ejemplares[posicion] += cantidad
          print(f"Se han agregado {cantidad} ejemplares a '{titulos[posicion]}'. Total ahora: {ejemplares[posicion]}")

     elif seleccion == "3":
          
           if not titulos:
               print("No hay títulos en el catálogo. Por favor, ingrese títulos primero.")
               continue
           
           print("--Catálogo de libros --")
           for i, titulo in enumerate(titulos):
               print(f"{i + 1}. {titulo}")

     elif seleccion == "4":
          
          if not titulos:
               print("No hay títulos en el catálogo. Por favor, ingrese títulos primero.")
               continue

          titulo_consulta = input("Ingrese el título a consultar: ")

          while True:
               if titulo_consulta in titulos:
                    posicion = titulos.index(titulo_consulta)
                    print(f"El título '{titulo_consulta}' tiene {ejemplares[posicion]} ejemplares disponibles.")
                    break
               else:
                    print("****************")
                    print(f"Error: El Título : {titulo_consulta} no se encuentra en el catalogo.")
                    print("****************")
                    titulo_consulta = input("Desea consultar nuevamente? (s: vuelve a ingresar / n: vuelve al menu principal) ")

                    if input().lower() == 's':
                         titulo_consulta = input("Ingrese el título a consultar: ")
                    else:
                         break

     elif seleccion == "5":
          
          if not titulos:
               print("No hay títulos en el catálogo. Por favor, ingrese títulos primero.")
               continue

          print("-- Títulos agotados --")

          agotados = False

          for i in ejemplares:
               if i == 0:
                    agotados = True
                    break
               
          if  agotados:
               print("-----Los siguientes títulos están agotados: -----")
               for titulo in titulos:
                    posicion = titulos.index(titulo)
                    if ejemplares[posicion] == 0:
                         print(f"- {titulo}")

     elif seleccion == "6":
          
          nuevo_titulo = input("Ingrese nuevo título: ")
          if nuevo_titulo in titulos or nuevo_titulo == "":
               print("****************")
               print("Error: Título ya existe o es inválido.")
               print("Ingrese nuevamente.")
               print("****************")
          else:
               titulos.append(nuevo_titulo)
               cantidad = int(input(f"Ingrese la cantidad de ejemplares para '{nuevo_titulo}': "))
               posicion = titulos.index(nuevo_titulo)
               ejemplares.insert(posicion, cantidad)
               print(f'Título "{nuevo_titulo}" con {cantidad} ejemplares agregado correctamente.')

     elif seleccion == "7":
          
          if not titulos:
               print("No hay títulos en el catálogo. Por favor, ingrese títulos primero.")
               continue

          for i, titulo in enumerate(titulos):
               print(f"{i + 1}. {titulo}")

          posicion = int(input("Ingresar numero de libros: ")) - 1

          while posicion < 0 or posicion >= len(titulos):
               print("****************")
               print("Error: Selección inválida.")
               print("Ingrese nuevamente.")
               print("****************")
               posicion = int(input("Ingresar numero de libros: ")) - 1

          accion = input("¿Desea realizar un préstamo (p) o una devolución (d)? ").lower()

          if accion == 'p':
               if ejemplares[posicion] > 0:
                    ejemplares[posicion] -= 1
                    print(f"Préstamo realizado. Ejemplares restantes de '{titulos[posicion]}': {ejemplares[posicion]}")
               else:
                    print(f"No hay ejemplares disponibles para '{titulos[posicion]}'.")
          elif accion == 'd':
               ejemplares[posicion] += 1
               print("Devolución realizada")
          else:
               print("Acción inválida. Por favor, seleccione 'p' para préstamo o 'd' para devolución.")

     elif seleccion == "8":
          
          if not titulos:
               print("No hay títulos en el catálogo. Por favor, ingrese títulos primero.")
               continue
           
          contador = 1
          print("-- Catálogo Completo --")
          
          for titulo in titulos:
               posicion = titulos.index(titulo)
               print(f"-{contador}. {titulo}: {ejemplares[posicion]} ejemplares disponibles") 
               contador += 1
               
     elif seleccion == "9":
          print("Saliendo del programa...")
          break