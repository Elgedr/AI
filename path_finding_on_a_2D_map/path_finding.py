class Pathfinder:

    def __init__(self):
        self.map_size = ()
        self.diamond_coordinates = ()
        self.map = []
        self.my_location = []
        self.path_to_diamond = []

    def count_map_sizes(self, map_exaple):
        map_rows = len(map_exaple)
        map_columns = len(map_exaple[0])
        self.map_size = (map_columns, map_rows)
        print(self.map_size)


if __name__ == '__main__':
    example = [
        "      **               **      ",
        "     ***     D        ***      ",
        "     ***                       ",
        "                      *****    ",
        "           ****      ********  ",
        "           ***          *******",
        " **                      ******",
        "*****             ****     *** ",
        "*****              **          ",
        "***                            ",
        "              **         ******",
        "**            ***       *******",
        "***                      ***** ",
        "                               ",
        "                s              ",
    ]
    pathfinder = Pathfinder()
    pathfinder.count_map_sizes(example)
