import random, tabulate
from vacuum import Vacuum

def create_enviroment():

    room_id = []
    rooms_status = []

    #Creación de habitaciones
    while(True):
        rooms = input("Introduce el número de habitaciones (2 a 26): ")
        if rooms.isdigit() and int(rooms) >= 2 and int(rooms) <= 26:
            rooms = int(rooms)
            vacuum = ["" for i in range(rooms)]
            break
        else:
            print("Error, introduce un número entre 2 y 26")
    a = 65
    i = 0

    #Configuración de habitaciones
    while(i < rooms):
        status = input(f"Introduce el estado de la habitación {chr(a)} (0 = limpia, 1 = sucia): ")
        if status.isdigit() and int(status) >= 0 and int(status) <= 1:
            # Room status es una lista
            # True si la habitación está limpia y False si está sucia
            if int(status) == 0:
                rooms_status.append(True)
            else:
                rooms_status.append(False)
            room_id.append(chr(a))
            a += 1
            i += 1
        else:
            print("Error, introduce un número entre 0 y 1")

    #Configuración de la posición de la aspiradora
    while(True):
        pos = input(f"Introduce la posición de la aspiradora ({room_id}): ")
        if pos.isalpha() and pos.upper() in room_id:
            vacuum = Vacuum(rooms_status, int(ord(pos.upper())-65))
            break
        else:
            print("Error, introduce una habitación válida")

    #Representación de la aspiradora
    vacuum.solve()

create_enviroment()