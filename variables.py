print("Ejercici 1: Sumar dos numeros")
print("*"*20)

numero1=float(input("Por favor ingrese el primer numero : "))
numero2=float(input("Por favor ingrese el segundo numero : "))

suma = numero1 + numero2

print(f"La suma es: {suma}")

base   = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

area = base * altura   # fórmula: base × altura

print(f"El área del rectángulo es: {area}")

minutos_totales = int(input("Ingrese la cantidad de minutos: "))

horas   = minutos_totales // 60   # división entera → horas completas
minutos = minutos_totales % 60    # módulo → minutos restantes

print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos")

precio    = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

valor_descuento = precio * (descuento / 100) 
precio_final    = precio - valor_descuento     

print(f"El precio final a pagar es: {precio_final}")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valorde b: "))

auxiliar = a 
a = b 
b = auxiliar

print(f"Después del intercambio: a = {a} , b = {b}")






