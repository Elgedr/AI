import random
from copy import deepcopy


class GAME():
    player_side = "X"
    computer_side = "O"
    players_turn = True

    def __init__(self):
        self.board = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]
        ]

    def board_numbers(self):
        for row in self.board:
            print(row)
        print("[---------------------------------]")
        print("{ 0    1    2    3    4    5    6 }")

    def simulate(self, move):
        pos = deepcopy(self.board)
        turn = False
        pos = self.simulate_move(move, pos, turn)

        while self.is_over(pos)[0] is False:
            turn = True
            possible_moves = self.moves(pos)
            choose_move = random.choice(possible_moves)
            pos = self.simulate_move(choose_move, pos, turn)
            turn = False
            if self.is_over(pos)[0] is True:
                break
            choose_move = random.choice(self.moves(pos))
            pos = self.simulate_move(choose_move, pos, turn)
            if self.is_over(pos)[0] is True:
                break
        return self.is_over(pos)[1]

    def make_move(self, move):
        if 0 < move > 6:
            if_symbol_is_wrong = input("You can not make this move! Your move? ")
            return self.make_move(int(if_symbol_is_wrong))
        if 0 <= move <= 6:
            for i in range(6):
                cell = self.board[-i - 1][move]
                if cell == " ":

                    if self.players_turn is True:
                        self.players_turn = False
                        self.board[-i - 1][move] = self.player_side

                    else:
                        self.players_turn = True
                        self.board[-i - 1][move] = self.computer_side

                    break

    def moves(self, pos):
        possible_moves = set()
        for row in range(6):
            for column in range(7):
                if pos[row][column] == " ":
                    possible_moves.add(column)
        return list(possible_moves)

    def simulate_move(self, move, pos, turn):
        col = []
        for i in range(6):
            col.append(pos[i][move])
        for i in range(5, -1, -1):
            if " " in col[i]:
                if turn is False:
                    pos[i][move] = self.computer_side

                else:
                    pos[i][move] = self.player_side
                return pos
        return pos

    def pure_mc(self, n=200):
        initial_moves = self.moves(self.board)
        win_counts = dict((move, 0) for move in initial_moves)

        for move in initial_moves:
            for i in range(n):
                res = self.simulate(move)
                if res == "O":
                    win_counts[move] += 1
                elif res == "DRAW":
                    win_counts[move] += 0.5
        print()
        print(win_counts)

        best_move = 0
        best_value = 0
        for key, value in win_counts.items():
            if value > best_value:
                best_value = value
                best_move = key

        return best_move

    def parse_move(self, movestr):
        possible_columns = range(7)
        users_input = int(movestr)
        if users_input in possible_columns:
            return users_input
        else:
            if_symbol_is_wrong = input("You can not make this move! Your move? ")
            return self.parse_move(if_symbol_is_wrong)

    def is_over(self, pos):
        players_side = "O"
        ai = "X"
        board = pos

        for column in range(4):
            for row in range(3, 6):
                if ai in board[row][column] and ai in board[row - 1][column + 1] and ai in board[row - 2][
                    column + 2] and ai in \
                        board[row - 3][
                            column + 3]:
                    return True, ai
                if players_side in board[row][column] and players_side in board[row - 1][column + 1] and players_side in \
                        board[row - 2][column + 2] and players_side in board[row - 3][
                    column + 3]:
                    return True, players_side

        for column in range(4):
            for row in range(3):
                if ai in board[row][column] and ai in board[row + 1][column + 1] and ai in board[row + 2][
                    column + 2] and ai in \
                        board[row + 3][
                            column + 3]:
                    return True, ai
                if players_side in board[row][column] and players_side in board[row + 1][column + 1] and players_side in \
                        board[row + 2][column + 2] and players_side in board[row + 3][
                    column + 3]:
                    return True, players_side

        for col in range(7):
            player = 0
            pc = 0
            for row in range(6):
                if ai in board[row][col]:
                    pc += 1
                    player = 0
                    if pc == 4:
                        return True, ai
                if players_side in board[row][col]:
                    player += 1
                    pc = 0
                    if player == 4:
                        return True, players_side

        for row in range(6):
            player = 0
            pc = 0
            for col in range(7):
                if " " in board[row][col]:
                    player = 0
                    pc = 0
                if ai in board[row][col]:
                    pc += 1
                    player = 0
                    if pc == 4:
                        return True, ai
                if players_side in board[row][col]:
                    player += 1
                    pc = 0
                    if player == 4:
                        return True, players_side

        if len(self.moves(board)) == 0:
            return True, "DRAW"

        return False, "PLAY"


if __name__ == '__main__':
    game = GAME()
    game.board_numbers()
    playing = True
    while playing:
        if game.players_turn is True:
            turn = game.parse_move(input('Your move? '))
            move = int(turn)
        else:
            move = game.pure_mc()
            print()

        game.make_move(move)
        game.board_numbers()

        is_over, winner = game.is_over(game.board)
        if is_over is True:
            if "O" == winner:
                print("Game over! AI WON!")
            if 'X' == winner:
                print("Game over! YOU WON!")
            playing = False
