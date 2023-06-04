import random
import string

# Definir la longitud de las contraseñas
longitud1 = input("how many characters each string?: ")
longitud2 = input("how many random strings?: ")

# Definir los caracteres permitidos para las contraseñas
caracteres = string.ascii_letters + string.digits

# Generar 100 pares de strings aleatorios
for i in range(int(longitud2)):
    string1 = ''.join(random.choice(caracteres) for _ in range(int(longitud1)))
    string2 = ''.join(random.choice(caracteres) for _ in range(int(longitud2)))
    print(f"{string1}")
