# Ingresar notas
grades = []
summ = 0

grade = input("Enter the grade of the student (enter -1 to stop entering grades): ")
while int(grade) >= 0:
    grades.append(grade)
    summ = summ + int(grade)
    grade = input("Enter the grade of the student (enter -1 to stop entering grades): ")
    
# Calcular promedio
avarage = summ / len(grades)
print(f"The avarage grade is {avarage}.")

# Calcular cuantos alumnos tienen notas menores al promedio
cant = 0
for i in range(len(grades)):
    cant = cant + 1 if int(grades[i]) < avarage else cant

print(f"The amount of students with grades less than avarage is {cant}")