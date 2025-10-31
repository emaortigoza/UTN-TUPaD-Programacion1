import csv
import os

NOMBRE_ARCHIVO = "productos.csv"

def obtener_productos():
    
    productos = []

    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
            escritor.writeheader()
            return productos

    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            productos.append({"nombre": fila["nombre"], "precio": float(fila["precio"])})
    return productos
def agregarProducto(producto):
     with open(NOMBRE_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
          escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
          escritor.writerow(producto)
def guardarProductos(productos):
     with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
          escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio"])
          escritor.writeheader()
          escritor.writerows(productos)

def mostar_productos():
     print("---- Lista de Productos ----")
     productos = obtener_productos()
     print("Nombre --- Precio")
     for producto in productos:
         print(f"{producto['nombre']} --- ${producto['precio']:.2f}")

def existe_producto(nombre):
     productos = obtener_productos()
     for producto in productos:
         if producto["nombre"].lower() == nombre.strip().lower():
             return True
     
     return False
def validar_numero(precio):
     if precio.count(".") > 1:
         return False
     
     if not precio.replace(".", "").isdigit():
         return False
     
     return True
def agregar_producto():

     print("---- Agregar Nuevo Producto ----")
     nombre = input("Ingrese el nombre del producto: ").strip()

     if existe_producto(nombre):
         print("El producto ya existe. No se puede agregar.")
         return

     precio = input("Ingrese el precio del producto: ").strip()

     if not validar_numero(precio):
           print("Precio inválido. Debe ser un número valido.")
           return
     
     precio = float(precio)

     agregarProducto({"nombre": nombre, "precio": precio})

     print("Producto agregado exitosamente.")

def editar_producto():

     nombre = input("Ingrese el nombre del producto a editar: ").strip()
     if not nombre:
         print("El nombre no puede estar vacío.")
         return
     
     productos = obtener_productos()

     for producto in productos:
          if producto["nombre"].lower() == nombre.lower():
               precio = input("Ingrese el nuevo precio del producto: ").strip()

               if not validar_numero(precio):
                    print("Precio inválido. Debe ser un número valido.")
                    return
               
               producto["precio"] = float(precio)

               guardarProductos(productos)
               print("Producto actualizado exitosamente.")
               break
     else:
          print("Producto no encontrado.")
          return

def eliminar_producto():
     nombre = input("Ingrese el nombre del producto a editar: ").strip()
     if not nombre:
         print("El nombre no puede estar vacío.")
         return

     productos = obtener_productos()
     productos_filtrados = []

     for producto in productos:
          if nombre.lower() != producto["nombre"].lower():
               productos_filtrados.append(producto)

     if len(productos) == len(productos_filtrados):
          print("Producto no encontrado.")
          return
     
     guardarProductos(productos_filtrados)
     print("Producto eliminado exitosamente.")


def mostrar_menu():
    
    while True:
        print("*" * 30)
        print ("1. Mostrar productos")
        print ("2. Agregar producto")
        print ("3. Editar precio de producto")
        print ("4. Eliminar producto")
        print ("5. Salir")
        print("*" * 30)
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                    mostar_productos()
            case "2":
                    agregar_producto()
            case "3":
                    editar_producto()
            case "4":
                    eliminar_producto()
            case "5":
                       print("Saliendo del programa...")
                       break
            case _:
                    print("Opción no válida. Por favor, intente de nuevo.")

mostrar_menu()
