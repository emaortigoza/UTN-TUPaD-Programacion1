elementos_quimicos = {"Oxigeno":"O", "Nitogeno":"N", "Sodio":"Na", "Hierro":"Fe"}
print(elementos_quimicos.values())


precios = {
     "Manzana": 3.5,
     "Banana": 2.0,
     "Naranja": 4.0,
}

precios["Banana"] = precios["Banana"] + 1
precios["Pera"] = 2.5

del precios["Naranja"]

print(precios)


stock = {
     "lapiz": 10,
     "cuaderno": 5,
     "goma": 3,
}

stock["cuaderno"] -= 2
stock["regla"] = stock.get("regla", 0) + 1
stock["goma"] = 0

print(stock)