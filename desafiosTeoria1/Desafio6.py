print("Ingrese una cadena de caracteres: ")
string = input()
cant = 0

for char in string:
    if char == 'a':
        cant = cant + 1

print ("La cantidad de letras a en la cadena ingresada es de: ", cant)