
class Cell:
    def __init__(self, letter, nb_seeds = 4):
        self.letter = str(letter)
        self.nb_seeds = int(nb_seeds)
    
    def display(self):
        print(f" {self.letter} \n({self.nb_seeds})")

class Board: 
    def __init__(self):
        self.cell_letters = [" A", "B", "C", "D", "E", "F", " G", "H", "I", "J", "K", "L"]
        self.cells = {}

        self.create_cells()

    def create_cells(self):
        for letter in self.cell_letters:
            self.cells[letter] = Cell(letter)

    def display_board(self):
        # for letter, cell in self.cells.items():
        #     cell.display()

        top_row = "  ".join(self.cell_letters[:6]) # de A à F
        bottom_row = "  ".join(self.cell_letters[6:]) # de G à L 
        top_seeds = "".join(f"({self.cells[letter].nb_seeds})" for letter in self.cell_letters[:6])
        bottom_seeds = "".join(f"({self.cells[letter].nb_seeds})" for letter in self.cell_letters[6:])

        print(top_row)
        print(top_seeds)
        print(bottom_seeds)
        print(bottom_row)


class Player:
    def __init__(self, name, cells):
        self.name = str(name)
        self.cells = list(cells)

    def display(self):
        print(f"{self.name} have cells {self.cells}")

    def sow(self):
        self.nb_seeds += 1

    def harvest(self):
        self.nb_seeds = 0
        return self.nb_seeds
    

# Initialisation du plateau
board = Board()
player1 = Player("Player 1", list(board.cells.values())[:6]) # Récupère un sous-ensemble du dictionnaire cells du Board
player2 = Player("Player 2", list(board.cells.values())[6:]) # Récupère un sous-ensemble du dictionnaire cells du Board

# Affichage du plateau
board.display_board()
player1.display()
player2.display()

