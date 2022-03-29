print("Ingrese un numero para saber si es multiplo de 2, 3 o 5: ")
nro = int(input())

# solo para saber si es multiplo de alguno de los 3 o no
if nro%2 == 0 or nro%3 == 0 or nro%5 == 0:
    print("El numero es multioplo de 2, 3 o 5.")
else:
    print("El numero NO es multioplo de 2, 3 o 5.")

# Para saber especificamente de que numero/s es multiplo
# res = "El numero ingresado "

# if nro%2 == 0:
#     res = res + "es multiplo de 2 "
#     #print("es multiplo de 2.")
# if nro%3 == 0:
#     res = res + "es multiplo de 3 "
#     #print("es multiplo de 3.")
# if nro%5 == 0:
#     res = res + "es multiplo de 5 "
#     #print("es multiplo de 5.")
    
# if (res == "El numero ingresado "):
#     res = res + "no es multiplo ni de 2, ni de 3, ni de 5. "
#     #print("no es multiplo ni de 2, ni de 3, ni de 5.")

# print(res)

