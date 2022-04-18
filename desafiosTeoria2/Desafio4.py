# Ingresar notas y nombres de los estudiantes
nombre = input("Ingresa un nombre (<FIN> para finalizar): ")
dicci = {}
suma = 0

while nombre != "FIN":
    nota = int(input(f"Ingresa la nota de {nombre}: "))
    dicci[nombre] = nota
    suma = suma + nota
    nombre = input("Ingresa un nombre (<FIN> para finalizar): ")

# Calcular promedio
promedio = suma / len(dicci)
print(f"La nota promedio de todos los estudiantes es: {promedio}.")

# Imprimir que alumnos estan debajo del promedio
for elem in dicci:
    if dicci[elem] < promedio:
        print(elem)