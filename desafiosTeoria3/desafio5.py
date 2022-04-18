def encripto(frase):
    nueva_frase = []
    frase = frase.split()
    for palabra in frase:
        for letra in palabra:
            letra = chr(ord(letra)-25) if letra.lower() == 'z' else chr(ord(letra) + 1)
            nueva_frase.append(letra)
    return(nueva_frase)

print(encripto("dia de enero"))
