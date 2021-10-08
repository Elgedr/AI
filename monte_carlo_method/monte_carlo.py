from copy import deepcopy


def pure_mc(pos, N=200):
    # all moves from starting position
    my_side = pos["my variant"]
    initial_moves = moves(pos)
    # win counters per move
    win_counts = dict((move, 0) for move in initial_moves)

    for move in initial_moves:
        for i in range(N):
            # make random moves until the game is over
            res = simulate(pos, move, my_side)
            if res == "WIN":
                win_counts[move] += 1
            elif res == "DRAW":
                win_counts[move] += 0.5
        best_move = 0
        best_win_amount = 0
        for move, win_amount in win_counts.items():
            if win_amount > best_win_amount:
                best_move = move
                best_win_amount = win_amount
        return best_move

    # find the move with the highest number of wins, return it


def moves(pos):
    possible_moves_set = set()
    for move in range(6):
        for row in range(7):
            if pos["gameboard"][move][row] == " ":
                possible_moves_set.add(row)
    # print(possible_moves_set)
    return possible_moves_set


def make_move(pos, move, who_goes):
    if 0 <= move <= 6:
        for i in range(6):
            particular_cell = pos["gameboard"][-i - 1][move]
            if particular_cell == " ":
                pos["gameboard"][-i - 1][move] = who_goes
                return pos  # (x, y)
                # return "Your move was made"


def simulate(pos, move, my_side):
    board_copy = deepcopy(pos)
    # pos2, xy = make_move(pos2, move)
    # over = is_over(pos2, xy)
    # if over[2]:
    #     return "DRAW"
    # elif over[0] and not over[1]:
    #     return "WIN"
    # elif over[0] and over[1]:
    #     return "LOSE"
    # else:
    #     pos2["flag"] = "X"
    #     while True:
    #         random_move = random.randint(0, 6)
    #         pos2, xy = make_move(pos2, random_move)
    #         over = is_over(pos2, xy)
    #         if over[2]:
    #             return "DRAW"
    #         elif over[0] and not over[1]:
    #             return "WIN"
    #         elif over[0] and over[1]:
    #             return "LOSE"
    #         elif not over[0]:
    #             if pos2["flag"] == "0":
    #                 pos2["flag"] = "X"
    #             else:
    #                 pos2["flag"] = "0"


def dump_pos(pos):
    for row in pos["gameboard"]:
        print(row)
    print("{ 0    1    2    3    4    5    6 }")


def parse_move(movestr):
    possible_columns = range(7)
    users_input = int(movestr)
    if users_input in possible_columns:
        return users_input
    else:
        if_symbol_is_wrong = input("You can not make this move! Your move? ")
        return parse_move(if_symbol_is_wrong)


def is_over(pos):
    players_side = pos["my variant"]
    ai = pos["ai variant"]
    board = pos["gameboard"]

    # check diagonal
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

    for row in board:
        if " " in row:
            return False, "PLAY"
        return True, "DRAW"


def play_game(pos):
    playing = True
    who_goes = "X"
    while playing:
        if who_goes == "X":
            dump_pos(pos)
            movestr = input("Your move? ")
            # convert user input into the move format you are using internally
            move = parse_move(movestr)
            who_goes = pos["ai variant"]
            who_made_move = "X"
        else:
            move = pure_mc(pos)
            who_goes = pos["my variant"]
            who_made_move = "O"

        pos = make_move(pos, move, who_made_move)
        # check after each move
        is_game_over = is_over(pos)
        if is_game_over[0]:
            playing = False
            dump_pos(pos)
            print("Game Over!", is_game_over[1], "won!")


if __name__ == '__main__':
    starting_pos = {
        "my variant": "X",
        "ai variant": "O",
        "gameboard": [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]
        ]
    }
    play_game(starting_pos)
