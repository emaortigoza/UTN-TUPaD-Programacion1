""" 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario """

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Ingrese un número entero positivo: "))
for i in range(1, num + 1):
    print(f"El factorial de {i} es {factorial(i)}")


""" 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique. """

def fibonacci(n):
     if n <= 0:
          return 0
     elif n == 1:
          return 1
     else:
          return fibonacci(n - 1) + fibonacci(n - 2)
     
pos = int(input("Ingrese la posición hasta la cual desea ver la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(pos):
    print(fibonacci(i), end=" ")


""" 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
algoritmo general. """

def potencia(base, exponente):
     if exponente == 0:
          return 1
     else:
          return base * potencia(base, exponente - 1)
     
b = float(input("Ingrese la base: "))
e = int(input("Ingrese el exponente (entero no negativo): "))

print(f"{b} elevado a la {e} es {potencia(b, e)}")


""" 4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto """

def decimal_a_binario(n):
     if n < 2:
          return str(n)
     else:
          return decimal_a_binario(n // 2) + str(n % 2)
     
num_decimal = int(input("Ingrese un número entero positivo en base decimal: "))
binario = decimal_a_binario(num_decimal)
print(f"La representación binaria de {num_decimal} es {binario}")



