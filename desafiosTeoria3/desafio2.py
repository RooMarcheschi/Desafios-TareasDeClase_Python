def imprimo_muchos_valores(mensaje_inicial, *en_otro_idioma, **en_detalle):
    print("Mensaje original")
    print(mensaje_inicial)
    print("\nEn otros idiomas")
    print("-" * 40)
    for val in en_otro_idioma:
        print(val)
    print("\nEn detalle")
    print("-" * 40)
    for clave in en_detalle:
        print(f"{clave}: {en_detalle[clave]}")
    print("\nFuente: traductor de Google. ")

imprimo_muchos_valores("Hola",
    "hello", "Hallo", "Aloha ", "Witam", "Kia ora",
    ingles= "hello",
    aleman="Hallo",
    hawaiano="Aloha",
    polaco="Witam",
    maori="Kia ora")