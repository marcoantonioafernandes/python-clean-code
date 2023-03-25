class Cell:
    def __init__(self, coord_x, coord_y, is_flagged):
        self.__coord_x = coord_x
        self.__coord_y = coord_y
        self.__is_flagged = is_flagged

    def is_flagged(self):
        return self.__is_flagged
    
class Minesweeper:
    def __init__(self, rows, cols):
        self.game_board = self.__generate_game_board(rows, cols)

    def __generate_game_board(self, rows, cols):
        game_board = list()
        for coord_x in range(rows):
            for coord_y in range(cols):
                cell = Cell(coord_x, coord_y, random.randint(0,1))
                game_board.append(cell)
        return game_board
    
    def get_flagged_cells(self) -> list:
        flagged_cells = list()
        for cell in self.game_board:
            if cell.is_flagged():
                flagged_cells.append(cell)
        return flagged_cells

if __name__ == '__main__':
    rows, cols = 3,3
    game_board = Minesweeper(rows, cols)
    flagged_cells = game_board.get_flagged_cells()
