print("Ingrese una letra ara saber si es minuscula o mayuscula: ")
letter = input()

if letter >= "a" and letter <= "z":
    print("es miniscula.")
elif letter >= "A" and letter <= "Z":
    print("ES MAYUSCULA.")
else:
    print("NO es una letra.")