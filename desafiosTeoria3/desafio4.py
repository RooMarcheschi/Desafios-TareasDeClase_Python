
def ordeno3(usuarios):
    """ Usamos sorted con una expresión lambda"""
    return sorted(usuarios, key=lambda usuario: usuario[0])

usuarios = [
    ('JonY BoY', 'Nivel3', 15),
    ('1962', 'Nivel1', 12),
    ('caike', 'Nivel2', 1020),
    ('Straka^', 'Nivel2', 1020),
]

print(ordeno3(usuarios))