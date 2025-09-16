x = 10 > 5
y = 3 == 4
z = 7 <= 7

print(not(x or y))
print((x or y) and z)


import random
numero_correcto = random.randint(1, 100)
numero_usuario = int(input("Adivina el número entre 1 y 100: "))
if numero_usuario == numero_correcto:
     print("¡Felicidades! Has adivinado el número.")
elif numero_usuario < numero_correcto:
     print("El número es menor. Inténtalo de nuevo.")
else:
     print("El número es mayor. Inténtalo con un numero menor.")
