print("Ingrese una caracter para saber si es o no una comilla: ")
char = input()

if char == "'":
    print("Es una comilla simple.")
elif char == '"':
    print("Es una comilla doble.")
else:
    print("NO es una comilla.")