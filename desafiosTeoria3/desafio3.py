def alfabeticamente(cadena="ss"):
    lista = cadena.split()
    return sorted(lista, key=str.lower)
    #lista.sort(key=str.lower)
    #return lista

print(alfabeticamente("Hoy puede ser un gran dia. "))