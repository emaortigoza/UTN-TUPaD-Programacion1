import os

FILENAME = "productos.txt"

def productos_desde_archivo():

     productos = []

     if not os.path.exists(FILENAME):
          print(f"El archivo {FILENAME} no existe.")
          return productos
     
     with open(FILENAME, "r", encoding="utf-8") as file:

          for line in file:

               line = line.strip()
               
               if not line:
                    continue

               partes = line.split(",")

               if len(partes) != 3:

                    print(f"Línea malformada: {line}")
                    continue

               nombre = partes[0].strip()

               try:
                    precio = float(partes[1])
               except ValueError:
                    precio = 0.0
               try:
                    cantidad = int(partes[2])
               except ValueError:
                    cantidad = 0
               productos.append ({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
               })
     return productos

def mostrar_productos(productos):

     if not productos:
          print("No hay productos para mostrar.")
          return

     for producto in productos:
          print(f"Poducto : {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")

def agregar_producto(productos):

    print("\n--- Agregar nuevo producto: ---")

    nombre = input("Ingrese el nombre del producto: ").strip()

    if not nombre: 
          print("El nombre del producto no puede estar vacío.")
          return
    try:
          precio = float(input("Ingrese el precio del producto: "))
    except ValueError:
         precio = 0.0
    try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
    except ValueError:
               cantidad = 0
    productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
      })
    print(f"Producto '{nombre}' agregado exitosamente.")

def guardar_productos_en_archivo(productos):

     with open(FILENAME, "w", encoding="utf-8") as file:

          for producto in productos:

               file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
          print(f"Archivo''{FILENAME}'' actualizado con {len(productos)} productos.")

def buscar_producto(productos, termino):

     termino = termino.strip().lower()
     encontrados = [p for p in productos if termino in p['nombre'].lower()]
     return encontrados

def menu():

     productos = productos_desde_archivo()
     if not productos:
          print("No se cargaron productos desde el archivo.")
          return  # Salir del menú si no hay productos

     while True:

          print("\n--- Menú de Gestión de Productos ---")
          print("1. Mostrar productos")
          print("2. Agregar producto")
          print("3. Buscar producto")
          print("4. Guardar y salir")
          print("5. Salir sin guardar")

          opcion = input("Seleccione una opción (1-5): ").strip()

          if opcion == "1":
               mostrar_productos(productos)
          elif opcion == "2":
               agregar_producto(productos)
          elif opcion == "3":
               termino = input("Ingrese el término de búsqueda: ")
               encontrados = buscar_producto(productos, termino)
               if encontrados:
                    print(f"Productos encontrados para '{termino}':")
                    mostrar_productos(encontrados)
               else:
                    print(f"No se encontraron productos para '{termino}'.")
          elif opcion == "4":
               guardar_productos_en_archivo(productos)
          elif opcion == "5":
               print("Deseas guardar los cambios antes de salir? (s/n)")
               if input().strip().lower() == 's':
                    guardar_productos_en_archivo(productos)
               print("Saliendo sin guardar.")
               break
          else:
               print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
     menu()