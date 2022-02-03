import random, tabulate, os

def create_enviroment():

    room_id = []
    room_status = []
    os.system("cls")

    #Creación de habitaciones
    while(True):
        rooms = input("Introduce el número de habitaciones (2 a 6): ")
        if rooms.isdigit() and int(rooms) >= 2 and int(rooms) <= 6:
            rooms = int(rooms)
            vacuum = ["" for i in range(rooms)]
            break
        else:
            os.system("cls")
            print("Error, introduce un número entre 2 y 6")
    a = 65
    i = 0
    os.system("cls")

    #Configuración de habitaciones
    while(i < rooms):
        status = input(f"Introduce el estado de la habitación {chr(a)} (0 = limpia, 1 = sucia): ")
        if status.isdigit() and int(status) >= 0 and int(status) <= 1:
            if int(status) == 0:
                room_status.append("_____")
            else:
                room_status.append("xxxxx")
            room_id.append(chr(a))
            a += 1
            i += 1
        else:
            os.system("cls")
            print("Error, introduce un número entre 0 y 1")

    #Configuración de la posición de la aspiradora
    while(True):
        pos = input(f"Introduce la posición de la aspiradora ({room_id}): ")
        if pos.isalpha() and pos.upper() in room_id:
            vacuum[room_id.index(pos.upper())] = "_-_/|"
            break
        else:
            os.system("cls")
            print("Error, introduce una habitación válida")

    #Representación de la aspiradora
    os.system("cls")
    print("Configuración de la habitación:\n")
    print(tabulate.tabulate([room_id, vacuum, room_status], tablefmt='grid'))

create_enviroment()