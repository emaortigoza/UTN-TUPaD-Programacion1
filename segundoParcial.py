import csv
import os

NOMBRE_ARCHIVO = "catalogo.csv"


def obtener_catalogo():

     catalogo = []

     if not os.path.exists(NOMBRE_ARCHIVO):
          with open(NOMBRE_ARCHIVO, mode='w', newline='', encoding='utf-8') as archivo:
               escritor = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
               escritor.writeheader()
               return catalogo
          
     with open(NOMBRE_ARCHIVO, mode='r', newline='', encoding='utf-8') as archivo:
          lector = csv.DictReader(archivo)
          for fila in lector:
               titulo = fila["TITULO"].strip()
               cantidad = fila["CANTIDAD"].strip()
               cantidad = int(cantidad) if cantidad.isdigit() and int(cantidad) >= 0 else 0
               catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
     return catalogo

def guardar_catalogo(catalogo):
     with open(NOMBRE_ARCHIVO, mode='w', newline='', encoding='utf-8') as archivo:
          escritor = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
          escritor.writeheader()
          escritor.writerows(catalogo)


def existe_libro(titulo):

     catalogo = obtener_catalogo()
     for libro in catalogo:
          if libro["TITULO"].strip().lower() == titulo.strip().lower():
               return True
     return False

def mostrar_catalogo():
    
    catalogo = obtener_catalogo()
    if not catalogo:
        print("No hay libros en el catalogo.")
        return
    
    print("---- Catalogo de la Biblioteca ----")
    print("TITULO ----- CANTIDAD")
    for libro in catalogo:
        print(f"{libro['TITULO']} ----- {libro['CANTIDAD']}")
     
    print("-----------------------------------")

def ingresar_titulos():
     
     cantidad = input("Ingrese la cantidad de titulos a ingresar: ").strip()
     if not cantidad.isdigit() or int(cantidad) <= 0:
          print("Cantidad inválida.")
          return
     
     cantidad = int(cantidad)
     catalogo = obtener_catalogo()

     for i in range(cantidad):
          print(f"Ingresando titulo {i + 1} de {cantidad}:")
          titulo = input("Ingrese el título del libro: ").strip()
          if not titulo:
               print("El título no puede estar vacío. Intente nuevamente.")
               continue
          if existe_libro(titulo):
               print("El título ya existe en el catálogo. No se puede agregar.")
               continue

          ejemplares = input("Ingrese la cantidad de ejemplares a ingresar: ").strip()
          if not ejemplares.isdigit() or int(ejemplares) < 0:
               print("Cantidad inválida. Se asignará 0.")
               ejemplares = 0
          else:
               ejemplares = int(ejemplares)
          
          catalogo.append({"TITULO": titulo, "CANTIDAD": ejemplares})

     guardar_catalogo(catalogo)
     print(f"'{titulo}' con '{ejemplares}' ejemplares agregado exitosamente al catálogo.")

def ingresar_ejemplares():

     titulo = input("Ingrese el título del libro al que desea agregar ejemplares: ").strip()
     catalogo = obtener_catalogo()

     for libro in catalogo:
          if libro["TITULO"].strip().lower() == titulo.strip().lower():
               cantidad = input("Ingrese la cantidad de ejemplares a agregar: ").strip()
               if not cantidad.isdigit() or int(cantidad) <= 0:
                    print("Cantidad inválida")
                    return
               libro["CANTIDAD"] += int(cantidad)
               guardar_catalogo(catalogo)
               print(f"Se han agregado {cantidad} ejemplares a '{libro['TITULO']}'.")
               return
     print("El título no existe en el catálogo.")

def consultar_disponibilidad():

     titulo = input("Ingrese el título del libro a consultar: ").strip()
     catalogo = obtener_catalogo()

     for libro in catalogo:
          if libro["TITULO"].strip().lower() == titulo.strip().lower():
               print(f"El libro '{libro['TITULO']}' tiene {libro['CANTIDAD']} ejemplares disponibles.")
               return
     print("El título no encontrado.")

def listar_agotados():
     
     catalogo = obtener_catalogo()
     agotados = [libro for libro in catalogo if libro["CANTIDAD"] == 0]

     if not agotados:
          print("No hay libros agotados.")
          return

     print("---- Libros Agotados ----")
     for libro in agotados: 
          print(f"{libro['TITULO']}")
     print("-------------------------")     

def agregar_titulo():
     
     titulo = input("Ingrese el título del nuevo libro: ").strip()
     if not titulo:
          print("El título no puede estar vacío.")
          return
     if existe_libro(titulo):
          print("El título ya existe en el catálogo.")
          return
     
     cantidad = input("Ingrese la cantidad de ejemplares a agregar: ").strip()
     if not cantidad.isdigit() or int(cantidad) < 0:
          print("Cantidad inválida. Se asignará 0.")
          cantidad = 0
     else:
          cantidad = int(cantidad)

     catalogo = obtener_catalogo()
     catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
     guardar_catalogo(catalogo)
     print(f"'{titulo}' agregado exitosamente al catálogo.")

def actualizar_ejemplares():

     titulo = input("Ingrese el título del libro a actualizar: ").strip()
     catalogo = obtener_catalogo()

     for libro in catalogo:
          if libro["TITULO"].strip().lower() == titulo.strip().lower():
               accion = input("Ingrese 'P' para prestar o 'D' para devolver: ").strip().upper()
               if accion == 'P':
                    if libro["CANTIDAD"] <= 0:
                         print("No hay ejemplares disponibles para prestar.")
                         return
                    libro["CANTIDAD"] -= 1
                    print(f"Se ha prestado un ejemplar de '{libro['TITULO']}'.")
               elif accion == 'D':
                    libro["CANTIDAD"] += 1
                    print(f"Se ha devuelto un ejemplar de '{libro['TITULO']}'.")
               else:
                    print("Acción inválida.")
                    return
               guardar_catalogo(catalogo)
               return
     print("El título no existe en el catálogo.")



def mostrar_menu():
     while True:
          print("*" * 30)
          print("1. Ingresar titulos")
          print("2. Ingresar ejemplares ")
          print("3. Mostrar catalogo")
          print("4. Consultar disponibilidad")
          print("5. Listar agotados")
          print("6. Agregar titulo")
          print("7. Actualizar ejemplares")
          print("8. Salir")
          print("*" * 30)

          opcion = input("Seleccione una opción: ").strip()
     
          match opcion:
               case "1":
                    ingresar_titulos()
               case "2":
                    ingresar_ejemplares()
               case "3":
                    mostrar_catalogo()
               case "4":
                    consultar_disponibilidad()
               case "5":
                    listar_agotados()
               case "6":
                    agregar_titulo()
               case "7":
                    actualizar_ejemplares()
               case "8":
                    print("Saliendo del programa...")
                    break
               case _:
                    print("Opción no válida. Por favor, intente de nuevo.")

mostrar_menu()
