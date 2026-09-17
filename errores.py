"""
try:
    numero = int(input("Ingrese un numero"))
    print(f"El numero ingresado es : {numero}")
except ValueError:
    print("Ingese un numero valido.")
"""

#Ciclo Infinito
"""
while True:
    print("Hola Mundo.")
"""
"""
edad =18
while edad >=18:

    try:
         edad =int(input("Ingrese su edad. "))
         print(f"Su edad es:{edad}")
    except ValueError:
         print("Menor de edad. Saliendo del Sistema")

print("Menor de edad. Saliendo del Sistema")
"""
"""
# Ejercicio 2: Division segura con ZeroDivisionError
try:
     dividiendo = float(input("Ingrese el dividendo: "))
     divisor    = float(input("Ingrese el divisor: "))
     resultado  = dividiendo / divisor
     print(f"Resultado: {dividiendo} / {divisor} = {resultado}")
except ZeroDivisionError:
     print("Error: no es posible dividir entre cero.")
except ValueError:
     print("Error: ingrese unicamente valores numericos.")
"""
"""
#Ejercicio 3
 
try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Erro: la edsd debe de se un numero entero")
else:
    print("Acceso denegado: debe de ser mayor de edad.")
finally:
    print("Verificacion finalizada.")
"""
"""
#Ejercicio 4 

while True:
    try:
        nota = float(input("Ingrese una nota entre 0.0 y 5.0"))
        if nota < 0.0 or nota > 5.0:
            raise ValueError("la nota debe estar 0.0 y 5.0.")
        break 
    except ValueError as e:
        print(f"Entrada invalida: {e}. Intente de nuevo.")

print(f"Nota registrada: {nota}")
"""
"""
# Ejercicio 5: 
def calcular_promedio(notas):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía.")
    return sum(notas) / len(notas)

try:
    n      = int(input("¿Cuántas notas va a ingresar? "))
    notas  = []
    for i in range(n):
        nota = float(input(f"  Nota {i + 1}: "))
        notas.append(nota)
    promedio = calcular_promedio(notas)
    print(f"Promedio: {round(promedio, 2)}")
except ValueError as e:
    print(f"Error: {e}")
"""