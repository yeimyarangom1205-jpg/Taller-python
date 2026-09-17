"""
#crear listas vacias 
lista_nombres =[]

while True:
    variable_nombre =  input("Ingrese su nombre: ")

    if variable_nombre != "salir":
        lista_nombres.append(variable_nombre) 

    if variable_nombre =="salir":
        print("nombres guardados:")
        print(lista_nombres)
        break

    nombre = input("Ingrese nombre: ")
    print(f"Nombre en Mayuscula {nombre.upper()}")
    print(f"Nombre en minuscula {nombre.lower()}")

    if nombre.lower()=="yeimy":
       print("Hola yeimy")
    else:
        print("Tu no eres yeimy")
"""

lista_perros =[]
lista_gatos = []

while True:
    try:
        pregunta =int (int(""" 
        seleccione Opcion:
        1: Registrar perros
        2: Registrar gatos
        3: Mostrar listado de perros
        4: Mostrar listado de gatos
        5: Salir 
        """))

        #validar que opcion escogio el usuario 

        if pregunta ==1:  
            perro=input("Cual es el nombre del perro:")
            lista_perros.append(perro)

        elif pregunta ==2:
            gato=input("Cual es el nombre del gato:")
            lista_gatos.append(gato)

        elif pregunta ==3:
            print("listado de perros")
            print("lista_perros")

        elif pregunta ==4:
            print("listado de gatos")
            print("listado_gatos")

        elif pregunta ==5:
            print("saliedno del sistema")


    except ValueError:
        print("Ingrese una opcion valida")


        

