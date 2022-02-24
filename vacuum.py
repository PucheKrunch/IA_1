from tabulate import tabulate
from copy import deepcopy

class Vacuum:
    rooms_checked = []
    # move = 1, check = 2, clean = 3
    cost = 0

    def __init__(self, rooms_status, vacuum_pos):
        self.rooms_status = rooms_status
        self.vacuum_pos = vacuum_pos

    def check_all(self):
        vacuum_solve = deepcopy(self)
        # Revisa su posición inicial y se mueve a la derecha
        # Revisando y limpiando en caso de ser necesario
        last_pos = self.vacuum_pos
        for i in range(vacuum_solve.vacuum_pos, len(vacuum_solve.rooms_status)):
            if i not in vacuum_solve.rooms_checked:
                if vacuum_solve.rooms_status[i] == False:
                    #Aspiramos
                    vacuum_solve.rooms_status[i] = True
                    vacuum_solve.cost += 3
                #Si está limpia, solo se agrega a la lista de habitaciones revisadas
                vacuum_solve.rooms_checked.append(i)
                vacuum_solve.cost += 2
            #Si ya está revisada, solo se mueve
            vacuum_solve.cost += 1
            last_pos = i
        vacuum_solve.vacuum_pos = last_pos
        vacuum_solve.cost -= 1
        print(f"Original (Coste -> {self.cost}):")
        self.draw_vacuum()
        print(f"\nSolución (Coste -> {vacuum_solve.cost}):")
        vacuum_solve.draw_vacuum()

    def draw_vacuum(self):
        vacuum = [ "" for i in range(len(self.rooms_status)) ]
        vacuum[self.vacuum_pos] = "_-_/|"
        dirty = [ "_____" if room else "XXXXX" for room in self.rooms_status ]
        print(tabulate([[chr(i+65) for i in range(len(self.rooms_status))], vacuum, dirty], tablefmt='grid'))

vacuum = Vacuum([True,False], 0)
vacuum.check_all()