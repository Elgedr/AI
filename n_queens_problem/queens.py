import random


class NQPosition:

    def __init__(self, N):
        self.board_size = N
        self.queens_coordinates = []  # queens coordinates
        while len(self.queens_coordinates) < self.board_size:
            row = random.randint(0, self.board_size - 1)
            column = random.randint(0, self.board_size - 1)
            if (row, column) not in self.queens_coordinates:
                self.queens_coordinates.append((row, column))
        print("Initial queens coordinates", self.queens_coordinates)

    def value(self):
        # calculate number of conflicts (queens that can capture each other)
        conflicts = []
        for queen in self.queens_coordinates:
            for other_queens_coord in range(self.board_size):
                first_queen_coord_row = queen[0]
                first_queen_coord_column = queen[1]
                second_queen_coord_row = self.queens_coordinates[other_queens_coord][0]
                second_queen_coord_column = self.queens_coordinates[other_queens_coord][1]
                if queen != (second_queen_coord_row, second_queen_coord_column):
                    if ((first_queen_coord_column == second_queen_coord_column) or (
                            first_queen_coord_row == second_queen_coord_row) or (
                            abs(first_queen_coord_row - second_queen_coord_row) == abs(
                        first_queen_coord_column - second_queen_coord_column))):
                        conflicts.append(((second_queen_coord_row, second_queen_coord_column),
                                          (first_queen_coord_row, first_queen_coord_column)))
        if len(conflicts) > 0:
            return len(conflicts) // 2
        return 0

    def draw(self):
        queen_map = []
        for y in range(self.board_size):
            queen_map.append([])
            for x in range(self.board_size):
                if (x, y) in self.queens_coordinates:
                    queen_map[y].append(1)
                else:
                    queen_map[y].append(0)
        return queen_map

    def best_move(self):
        # find the best move and the value function after making that move
        best_move_value = None  # ((row, column) - the queen's coordinates, which we want to move (row, column) mew queen coordinates where we move it)
        conflicts = self.value()
        equivalent_values = []
        for queen in self.queens_coordinates:
            for i in range(self.board_size):
                for j in range(self.board_size):
                    new_pos = (i, j)
                    if new_pos not in self.queens_coordinates:
                        move = (queen, new_pos)
                        self.make_move(move)
                        conflicts_with_new_movement = self.value()
                        if conflicts_with_new_movement < conflicts:
                            conflicts = conflicts_with_new_movement
                            best_move_value = move
                            equivalent_values.clear()
                            equivalent_values.append(move)
                        elif conflicts_with_new_movement == conflicts:
                            equivalent_values.append(move)
                        self.make_move((new_pos,
                                        queen))  # turning back previous coordinates of queens, because we moved them only for checking the conflicts. Real queens movement will be done in method hill_climbing
        if len(equivalent_values) != 0:
            chosen = random.randint(0,
                                    len(equivalent_values) - 1)  # if there are few possible movements we can perform, we choose the best randomly
            best_move_value = equivalent_values[chosen]
        return best_move_value, conflicts

    def make_move(self, move):
        # move is a ((r1, c1), (r2, c2)) , where the r1, c1 is a queens old coordinates and the r2, c2 is the queen's new coordinates
        queen = self.queens_coordinates.index(move[0])  # we find the index of a queen with current coordinates
        self.queens_coordinates[queen] = move[
            1]  # we move the particular queen's coordinates on the new one (performing a movement)


def hill_climbing(pos):
    curr_value = pos.value()
    while True:
        move, new_value = pos.best_move()
        if new_value == 0:
            pos.make_move(move)
            return pos, new_value
        elif new_value != 0 and new_value >= curr_value:
            return hill_climbing(NQPosition(pos.board_size))
        else:
            # position improves, keep searching
            curr_value = new_value
            pos.make_move(move)


if __name__ == '__main__':
    pos = NQPosition(6)  # test with the tiny 4x4 board first
    print("initial conflicts number", pos.value())
    best_pos, best_value = hill_climbing(pos)
    print("Final value", best_value)
    # if best_value is 0, we solved the problem
    mapp = best_pos.draw()
    for row in mapp:
        print(row)
