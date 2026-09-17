
#Ciclo for = repite por la cantidad de veces 
"""
for i in range(10):
    print(f"{i} Hola mundo")

"""
"""
#Ciclo for = repite por la cantidad de veces

for i in range(10):
    print(f"{i} Hola mundo")

"""
for i in range(0, 100, 5):
    print(f"{i} Hola mundo")


    # adivina el numero secreto
    numero_secreto=9
    intentos=3

    for i in range (intentos):
        numero = int(input("adivina el numero secreto (1-10): "))

    if numero == numero_secreto :
        print(" felicidades ere super teso😂 ")
        break
    else:
        intentos_restantes = intentos - (i + 1)
        print(f"😶‍🌫️ te quedan {intentos_restantes} intentos")
                            #3 - (0 + 1) = 2
                            #3 - (1+1) = 1
                            #3 - (2+1) = 0
       #verificar si no le quedan intentos y mostrar el numero

     # Ejercicio 1: Mostrar la tabla de multiplicar de un número
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1, 11):          # recorre los valores del 1 al 10
    print(f"{numero} x {i} = {numero * i}")
