from tabulate import tabulate
from copy import deepcopy

class Vacuum:
    rooms_checked = []
    path = []
    # move = 1, check = 2, clean = 3
    cost = 0
    left = ["Izquierda"]
    right = ["Derecha"]

    def __init__(self, rooms_status, vacuum_pos):
        self.rooms_status = rooms_status
        self.vacuum_pos = vacuum_pos

    def solve(self):
        print("Problema incial:")
        self.draw_vacuum()
        print("Solución comenzando a la derecha:")
        self.solve_right()
        print("Solución comenzando a la izquierda:")
        self.solve_left()
        print(f"La mejor solución es {self.left[0] if self.left[1] < self.right[1] else self.right[0]} con un costo de {self.left[1] if self.left[1] < self.right[1] else self.right[1]}")

    def solve_right(self):
        # Primero se hace la solución con el movimiento hacia la derecha
        vacuum_solve_right = deepcopy(self)
        # Revisa su posición inicial y se mueve a la derecha
        # Revisando y limpiando en caso de ser necesario
        last_pos = self.vacuum_pos
        for i in range(vacuum_solve_right.vacuum_pos, len(vacuum_solve_right.rooms_status)):
            if i not in vacuum_solve_right.rooms_checked:
                if vacuum_solve_right.rooms_status[i] == False:
                    #Aspiramos
                    vacuum_solve_right.rooms_status[i] = True
                    vacuum_solve_right.cost += 3
                #Si está limpia, solo se agrega a la lista de habitaciones revisadas
                vacuum_solve_right.rooms_checked.append(i)
                vacuum_solve_right.cost += 2
            #Si ya está revisada, solo se mueve
            vacuum_solve_right.cost += 1
            last_pos = i

        vacuum_solve_right.vacuum_pos = last_pos
        vacuum_solve_right.cost -= 1

        # En caso de que haya empezado en la habitación A, se llegó a la solución
        if len(vacuum_solve_right.rooms_checked) == len(vacuum_solve_right.rooms_status):
            print("Costo:", vacuum_solve_right.cost)
            vacuum_solve_right.draw_vacuum()
        # En el caso contrario se devuelve a la función con el movimiento hacia la izquierda
        else:
            for i in range(vacuum_solve_right.vacuum_pos, -1, -1):
                if i not in vacuum_solve_right.rooms_checked:
                    if vacuum_solve_right.rooms_status[i] == False:
                        #Aspiramos
                        vacuum_solve_right.rooms_status[i] = True
                        vacuum_solve_right.cost += 3
                    #Si está limpia, solo se agrega a la lista de habitaciones revisadas
                    vacuum_solve_right.rooms_checked.append(i)
                    vacuum_solve_right.cost += 2
                #Si ya está revisada, solo se mueve
                vacuum_solve_right.cost += 1
                last_pos = i
            vacuum_solve_right.vacuum_pos = last_pos
            vacuum_solve_right.cost -= 1
            print("Costo:", vacuum_solve_right.cost)
            vacuum_solve_right.draw_vacuum()
        self.right.append(vacuum_solve_right.cost)

    def solve_left(self):
        # Ahora haremos lo mismo pero comenzando por la izquierda
        vacuum_solve_left = deepcopy(self)
        vacuum_solve_left.rooms_checked = []
        last_pos = self.vacuum_pos
        for i in range(vacuum_solve_left.vacuum_pos, -1, -1):
            if i not in vacuum_solve_left.rooms_checked:
                if vacuum_solve_left.rooms_status[i] == False:
                    #Aspiramos
                    vacuum_solve_left.rooms_status[i] = True
                    vacuum_solve_left.cost += 3
                #Si está limpia, solo se agrega a la lista de habitaciones revisadas
                vacuum_solve_left.rooms_checked.append(i)
                vacuum_solve_left.cost += 2
            #Si ya está revisada, solo se mueve
            vacuum_solve_left.cost += 1
            last_pos = i
        
        vacuum_solve_left.vacuum_pos = last_pos
        vacuum_solve_left.cost -= 1

        # En caso de que haya empezado en la última habitación, se llegó a la solución
        if len(vacuum_solve_left.rooms_checked) == len(vacuum_solve_left.rooms_status):
            print("Costo:", vacuum_solve_left.cost)
            vacuum_solve_left.draw_vacuum()
        # En el caso contrario se devuelve a la función con el movimiento hacia la derecha
        else:
            for i in range(vacuum_solve_left.vacuum_pos, len(vacuum_solve_left.rooms_status)):
                if i not in vacuum_solve_left.rooms_checked:
                    if vacuum_solve_left.rooms_status[i] == False:
                        #Aspiramos
                        vacuum_solve_left.rooms_status[i] = True
                        vacuum_solve_left.cost += 3
                    #Si está limpia, solo se agrega a la lista de habitaciones revisadas
                    vacuum_solve_left.rooms_checked.append(i)
                    vacuum_solve_left.cost += 2
                #Si ya está revisada, solo se mueve
                vacuum_solve_left.cost += 1
                last_pos = i
            vacuum_solve_left.vacuum_pos = last_pos
            vacuum_solve_left.cost -= 1
            print("Costo:", vacuum_solve_left.cost)
            vacuum_solve_left.draw_vacuum()
        self.left.append(vacuum_solve_left.cost)

    def draw_vacuum(self):
        vacuum = [ "" for i in range(len(self.rooms_status)) ]
        vacuum[self.vacuum_pos] = "_-_/|"
        dirty = [ "_____" if room else "XXXXX" for room in self.rooms_status ]
        print(tabulate([[chr(i+65) for i in range(len(self.rooms_status))], vacuum, dirty], tablefmt='grid'))

vacuum = Vacuum([False,False,True,True,True], 3)
vacuum.solve()