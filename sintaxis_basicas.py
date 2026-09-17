Nombre = "Yeimy" # Variable de tipo string (cadena de texto)
documento = 1037778691 # Variable de tipo int (número entero)
direccion = "Medellin"  # Variable de tipo string (cadena de texto)
tiene_deudas = True        # Variable de tipo bool (booleano)

print(Nombre)

print("CONCATENACION USANDO +")
print("=" * 30)
print("Mi Nombre es: " + Nombre + " y mi documento es: " + str(documento))
print("\nCONCATENACON SANDO ,")
print("=" * 30)

      

print("Mi nombre es:", Nombre, "y mi documento es:", documento)



print("\nCONCATENACION USANDO F-STRINGS")
print("=" * 30)


print(f"Mi Nombre es: {Nombre} y mi documento es: {documento}")


print("\nMOSTRAR VARIAS VARIABLES CON F-STRINGS")
print("=" * 30)


print(f"""
Nombre:      {Nombre}
Documento:   {documento}
Dirreccion   {direccion}¿iene deudas?:{tiene_deudas}
""")


print("=" * 30)

print(f"""
Nombre:         {Nombre}
Documento:      {documento}
Direccin:      {direccion}¿Tiene deudas?: {tiene_deudas}
""")

print(f"\n Hola, Nombre!")

