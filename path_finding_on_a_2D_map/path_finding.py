from queue import Queue, PriorityQueue


def bfs(given_map, start_coordinates):
    # start - (y, x)

    frontier = Queue()
    frontier.put(start_coordinates)
    came_from = {
        start_coordinates: None}  # key: where we can go from current coordinate , value: our current coordinate
    finish = None
    path = []

    while not frontier.empty():
        current = frontier.get()
        neighbours = []
        row = given_map[current[1]]
        point = row[current[0]]
        columns_amount = len(row)
        rows_amount = len(given_map)
        row_nr = current[1]
        column_nr = current[0]

        if point == "D":  # if current point is the diamond we break the loop
            finish = current  # save diamond coordinates
            break

        elif point != "*":
            # here I add up and down coordinates

            if rows_amount == row_nr + 1:  # if we are on the last row, we cant check the row below us, so we add only
                # coordinate above us
                neighbours.append((column_nr, row_nr - 1))
            elif 0 == row_nr:  # if we are on the first row, we cant check the row above us, so we add only coordinates below
                neighbours.append((column_nr, row_nr + 1))
            else:
                neighbours.append((column_nr, row_nr - 1))  # otherwise we add both  - below and above coordinates
                neighbours.append((column_nr, row_nr + 1))

            # here I add left and right coordinates
            if columns_amount == column_nr + 1:  # if we are on the last column, we cant check the next column, so we add only back column coordinates
                neighbours.append((column_nr - 1, row_nr))
            elif 0 == column_nr:  # if we are on the first column, we cant check the back column, so we add only next column coordinates
                neighbours.append((column_nr + 1, row_nr))

            else:
                neighbours.append((column_nr - 1, row_nr))  # otherwise we add both  - left and right coordinates
                neighbours.append((column_nr + 1, row_nr))

        for neighbours_coordinates in neighbours:
            if neighbours_coordinates not in came_from.keys():  # if we were not on this coordinate, we ...
                frontier.put(neighbours_coordinates)  # move frontier to other coordinate
                came_from[
                    neighbours_coordinates] = current  # add neighbour coordinate as possible movement from the current coordinate

    where_i_am_now = finish  # saving diamond coordinates
    path.append(
        where_i_am_now)  # adding diamond coordinates as a start of the path (later I will reverse the path, so it will be the finish coordinate)
    while start_coordinates not in path:
        where_i_am_now = came_from.get(where_i_am_now)
        path.append(where_i_am_now)
    path.reverse()

    res = []
    for i in path:
        a = i[1]
        b = i[0]
        res.append((a, b))

    print(res)


def heuristic(goal, node):
    return abs(goal[0] - node[0]) + abs(goal[1] - node[1])


def greedy(given_map, start_coordinates, goal):
    frontier = PriorityQueue()
    frontier.put((0, start_coordinates))
    came_from = {
        start_coordinates: None}  # key: where we can go from current coordinate , value: our current coordinate
    finish = None
    path = []

    while not frontier.empty():
        current_first = frontier.get()
        current = current_first[1]
        neighbours = []
        row = given_map[current[1]]
        point = row[current[0]]
        columns_amount = len(row)
        rows_amount = len(given_map)
        row_nr = current[1]
        column_nr = current[0]

        if point == "D":  # if current point is the diamond we break the loop
            finish = current  # save diamond coordinates
            break

        elif point != "*":
            # here I add up and down coordinates

            if rows_amount == row_nr + 1:  # if we are on the last row, we cant check the row below us, so we add only
                # coordinate above us
                neighbours.append((column_nr, row_nr - 1))
            elif 0 == row_nr:  # if we are on the first row, we cant check the row above us, so we add only coordinates below
                neighbours.append((column_nr, row_nr + 1))
            else:
                neighbours.append((column_nr, row_nr - 1))  # otherwise we add both  - below and above coordinates
                neighbours.append((column_nr, row_nr + 1))

            # here I add left and right coordinates
            if columns_amount == column_nr + 1:  # if we are on the last column, we cant check the next column, so we add only back column coordinates
                neighbours.append((column_nr - 1, row_nr))
            elif 0 == column_nr:  # if we are on the first column, we cant check the back column, so we add only next column coordinates
                neighbours.append((column_nr + 1, row_nr))

            else:
                neighbours.append((column_nr - 1, row_nr))  # otherwise we add both  - left and right coordinates
                neighbours.append((column_nr + 1, row_nr))

        for neighbour_coordinate in neighbours:
            if neighbour_coordinate not in came_from.keys():  # if we were not on this coordinate, we ...
                priority = heuristic(goal, neighbour_coordinate)
                frontier.put((priority, neighbour_coordinate))  # move frontier to other coordinate
                came_from[
                    neighbour_coordinate] = current  # add neighbour coordinate as possible movement from the current coordinate

    where_i_am_now = finish  # saving diamond coordinates
    path.append(
        where_i_am_now)  # adding diamond coordinates as a start of the path (later I will reverse the path, so it will be the finish coordinate)
    while start_coordinates not in path:
        where_i_am_now = came_from.get(where_i_am_now)
        path.append(where_i_am_now)
    path.reverse()

    res = []
    for i in path:
        a = i[1]
        b = i[0]
        res.append((a, b))
    print(res)


def astar(given_map, start_coordinates, goal):
    frontier = PriorityQueue()
    frontier.put((0, start_coordinates))
    came_from = {
        start_coordinates: None}  # key: where we can go from current coordinate , value: our current coordinate
    finish = None
    path = []
    cost_so_far = {start: 0}

    while not frontier.empty():
        current_first = frontier.get()
        current = current_first[1]
        neighbours = []
        row = given_map[current[1]]
        point = row[current[0]]
        columns_amount = len(row)
        rows_amount = len(given_map)
        row_nr = current[1]
        column_nr = current[0]

        if point == "D":  # if current point is the diamond we break the loop
            finish = current  # save diamond coordinates
            break

        elif point != "*":
            # here I add up and down coordinates

            if rows_amount == row_nr + 1:  # if we are on the last row, we cant check the row below us, so we add only
                # coordinate above us
                neighbours.append((column_nr, row_nr - 1))
            elif 0 == row_nr:  # if we are on the first row, we cant check the row above us, so we add only coordinates below
                neighbours.append((column_nr, row_nr + 1))
            else:
                neighbours.append((column_nr, row_nr - 1))  # otherwise we add both  - below and above coordinates
                neighbours.append((column_nr, row_nr + 1))

            # here I add left and right coordinates
            if columns_amount == column_nr + 1:  # if we are on the last column, we cant check the next column, so we add only back column coordinates
                neighbours.append((column_nr - 1, row_nr))
            elif 0 == column_nr:  # if we are on the first column, we cant check the back column, so we add only next column coordinates
                neighbours.append((column_nr + 1, row_nr))

            else:
                neighbours.append((column_nr - 1, row_nr))  # otherwise we add both  - left and right coordinates
                neighbours.append((column_nr + 1, row_nr))

        for neighbour_coordinate in neighbours:
            updated_cost = cost_so_far[current] + 1  # next cost increased by 1
            if neighbour_coordinate not in cost_so_far or updated_cost < cost_so_far[
                neighbour_coordinate]:  # if increased cost is smaller than current coordinate cost
                cost_so_far[neighbour_coordinate] = updated_cost  # add a coordinates and its cost
                priority = heuristic(goal, neighbour_coordinate) + updated_cost
                frontier.put((priority, neighbour_coordinate))  # move frontier to other coordinate
                came_from[
                    neighbour_coordinate] = current  # add neighbour coordinate as possible movement from the current coordinate

    print(cost_so_far)
    where_i_am_now = finish  # saving diamond coordinates
    path.append(
        where_i_am_now)  # adding diamond coordinates as a start of the path (later I will reverse the path, so it will be the finish coordinate)
    while start_coordinates not in path:
        where_i_am_now = came_from.get(where_i_am_now)
        path.append(where_i_am_now)
    path.reverse()

    res = []
    for i in path:
        a = i[1]
        b = i[0]
        res.append((a, b))
    print(res)


if __name__ == '__main__':
    # start = (16, 14)
    # lava_map1 = [
    #     "     **********************    ",
    #     "   *******   D    **********   ",
    #     "   *******                     ",
    #     " ****************    **********",
    #     "***********          ********  ",
    #     "            *******************",
    #     " ********    ******************",
    #     "********                   ****",
    #     "*****       ************       ",
    #     "***               *********    ",
    #     "*      ******      ************",
    #     "*****************       *******",
    #     "***      ****            ***** ",
    #     "                               ",
    #     "                s              ",
    # ]
    # bfs(lava_map1, start)
    start = (2, 2)
    with open("../../AppData/Roaming/JetBrains/PyCharm2021.2/scratches/cave300x300") as f:
        map_data3 = [line.strip() for line in f.readlines() if len(line) > 1]

    astar(map_data3, start, (257, 295))  # (column, row)
