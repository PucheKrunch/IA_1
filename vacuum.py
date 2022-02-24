class Vacuum:
    rooms_checked = []
    cost = 0

    def __init__(rooms_state,vacuum_pos):
        self.rooms_state = rooms_state
        self.vacuum_pos = vacuum_pos