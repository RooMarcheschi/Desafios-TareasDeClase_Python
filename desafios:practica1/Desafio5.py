print("Ingrese la cadena de caracteres 1: ")
string1 = input()

print("Ingrese la cadena de caracteres 2: ")
string2 = input()

if len(string1) == len(string2):
    print("Las cadenas tienen la misma cantidad de caracteres.")
elif len(string1) > len(string2):
    print("La cadena con mayor caracteres es la 1.")
else:
    print("La cadena con mayor caracteres es la 2.")