variable = 0
print(bool(variable)) # False

variable = "Hola mundo"
print(bool(variable)) # True

variable = ""
print(bool(variable)) # False

variable = []
print(bool(variable)) # False


a = True 
b = False
c = not a and b  
d = not (a and b) 
print(c) # False
print(d) # True
e = c or d and a or b
print (e) # True