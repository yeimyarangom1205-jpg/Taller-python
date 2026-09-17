#solicitar variables
nombre = input("Ingrese su nombre: ")
edad   = int (input("Ingrese su edad: "))

if edad <0: #Validar si la edad en Negativo:
    print(f"Error: La edad {edad} es Invalidado ")  

    #validar si la edad es menor a 18 y calcular cuantos años le faltan 
else:
    faltan = 18 - edad
    print("Resultado: Es menos de edad.")    
    print("Le faltan",faltan, "años para cumplir la mayoria de edad")
    


 

nombre_ciudad = input("Ingrese nombre de la ciudad: ")
Temperatura = float(input("La temperatura en grados celsius (10° a 32°:)"))

if Temperatura >= 32:
    print("Muy caliente")
elif Temperatura >= 26:
    print("Caliente")
elif Temperatura >= 18:
    print("Templado")
elif Temperatura >= 10:
    print("Fria")
elif Temperatura <= 10:
    print("Muy fria")

if Temperatura <18:
    print(f"Temperatura baja: llevar abrigo")