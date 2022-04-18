#Solución
import csv
accesos = open('BBB_nuevo.csv','r')

def es_grabacion(acceso):
    """Esta funcion retorna si un acceso es una grabacion vista o no)"""
    if (acceso[2] == "Grabación vista"):
        return True
    else:
        return False

def mas_grabaciones():
    """Esta funcion retorna la fecha con mas grabaciones vistas"""
    accesos_reader = csv.reader(accesos)
    filas = []
    for fila in accesos_reader:
        filas.append(fila)
    filas = [l for l in filas if es_grabacion(l)] #guardamos en filas solo aquellas que sean accesos de grabaciones vistas
    fechas = [f[0].split(' ')[0] for f in filas] #creamos una lista de las fechas de cada una de las filas(accesos) 
    return max(set(fechas), key=fechas.count) #retornamos la fecha que mas veces aparece en la lista fechas

print("La fecha con mas grabaciones vistas es: ", mas_grabaciones())
