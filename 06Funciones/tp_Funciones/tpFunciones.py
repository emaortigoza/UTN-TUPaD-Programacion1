""" 1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal """

def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

""" 2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario. """

def saludar_usuario(nombre):
    return "Hola " + nombre + "!"
nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

""" 3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
dir los datos al usuario y llamar a esta función con los valores in-
gresados. """

def informacion_personal(nombre, apellido, edad, residencia):
     print("Soy " + nombre + " " + apellido + ", tengo " + str(edad) + " años y vivo en " + residencia)

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

""" 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
dio como parámetro y devuelva el área del círculo. calcular_peri-
metro_circulo(radio) que reciba el radio como parámetro y devuel-
va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
bas funciones para mostrar los resultados. """

import math
def calcular_area_circulo(radio):
    return math.pi * radio * radio
def calcular_perimetro_circulo(radio):
     return 2 * math.pi * radio
radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print("El área del círculo es: " + str(area))
print("El perímetro del círculo es: " + str(perimetro))


""" 5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos-
trar el resultado usando esta función. """

def segundos_a_horas(segundos):
    return segundos / 3600
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print("La cantidad de horas es: " + str(horas))


""" 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun-
ción. """

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(str(numero) + " x " + str(i) + " = " + str(numero * i))
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)


""" 7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta-
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
sultados de forma clara. """

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido (no se puede dividir por cero)"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)
print("Resultados:")
print("Suma: " + str(resultados[0]))
print("Resta: " + str(resultados[1]))
print("Multiplicación: " + str(resultados[2]))
print("División: " + str(resultados[3]))


""" 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
ción para mostrar el resultado con dos decimales """

def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return round(imc, 2)
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print("Su índice de masa corporal (IMC) es: " + str(imc))


""" 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función. """

def celsius_a_fahrenheit(celsius):
     fahrenheit = (celsius * 9/5) + 32
     return round(fahrenheit, 2)
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print("La temperatura en grados Fahrenheit es: " + str(fahrenheit))


""" 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función. """

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return round(promedio, 2) 
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(a, b, c)
print("El promedio de los tres números es: " + str(promedio))

