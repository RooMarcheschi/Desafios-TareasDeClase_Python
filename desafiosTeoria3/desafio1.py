def imprimo(*args):
    """Esta funcion imprime los argumentos junto con su tipo"""
    for arg in args:
        print(f"{arg} es de tipo {type(arg)}")

imprimo(4,"dos",[1,4],"Ro")