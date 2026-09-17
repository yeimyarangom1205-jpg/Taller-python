# introduccion_git
Proyecto de práctica para aprender Git y GitHub.

## Archivos
- README.md
- calcularSalario.py

# calcularSalario.py

horas = float(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora: "))

salario_bruto = horas * valor_hora
descuento = salario_bruto * 0.08
salario_neto = salario_bruto - descuento

print("Salario bruto:", salario_bruto)
print("Descuento:", descuento)
print("Salario neto:", salario_neto)
