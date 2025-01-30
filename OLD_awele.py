
# Définition de la classe parent
class Board: 
    def __init__(self, nb_seeds, nb_cells = 12, cells = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]):
        self.__nb_seeds = int(nb_seeds)
        self.__nb_cells = nb_cells
        self.__cells = cells

    def display(self):
        print(f'Board contains {self.__nb_cells} and {self.__nb_seeds} seeds')
        for i in self.__cells:
            print(i)

    def isEmpty(self):
        if (self.__nb_seeds == 0):
            print("Board is empty")
            return True


class Cell(Board):
    def __init__(self, letter, nb_seeds = 4):
        self.__letter = str(letter)
        self.__nb_seeds = int(nb_seeds)

    def display(self):
        print(f' {self.__letter}\n({self.__nb_seeds})')

    def add_seed(self):
        self.__nb_seeds += 1

    def remove_seeds(self):
        self.__nb_seeds = 0
        return self.__nb_seeds


class Player(Board):
    def __init__(self,  name, cells):
        self.__name = str(name)
        self.__cells = cells

    def display_cells(self):
        print(f"{self.__name} owns {self.__cells} cells")


board = Board(48)
board.display()

player1 = Player("Player 1", ["A", "B", "C", "D", "E", "F"])
player1.display_cells()

cell_A = Cell("A")
cell_B = Cell("B")
cell_C = Cell("C")
cell_D = Cell("D")
cell_E = Cell("E")
cell_F = Cell("F")
cell_G = Cell("G")
cell_H = Cell("H")
cell_I = Cell("I")
cell_J = Cell("J")
cell_K = Cell("K")
cell_L = Cell("L")


cell_A.display()
cell_G.display()
