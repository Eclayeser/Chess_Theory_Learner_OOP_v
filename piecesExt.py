import pygame

class ChessPiece(pygame.sprite.Sprite):
    def __init__(self, chessPieceImg, type, colour, board):
        super().__init__()
        self.display_piece_img = pygame.image.load(chessPieceImg)
        self.position = ""
        self.type = type
        self.colour = colour
        self.name = str(colour)+str(type)
        self.add_piece_toBoard(board)


    def add_piece_toBoard(self, board):
        board.pieces.append(self)


    def setPos(self, pos, boardsize):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
        if len(pos) == 2 and pos[0] in letters and pos[1] in numbers:
            self.position = str(pos)
        else:
            raise ValueError("Invalid piece position:", self.name)
        
        self.calc_coordinates(boardsize, boardsize)
        
    def calc_coordinates(self, board_w, board_h):
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        numbers = ["8", "7", "6", "5", "4", "3", "2", "1"]
        x_coor = 0
        y_coor = 0
        for i in letters:
            if self.position[0] == i:
                self.x_coor = x_coor
            x_coor += round(board_w/8)
        for j in numbers:
            if self.position[1] == j:
                self.y_coor = y_coor
            y_coor += round(board_h/8)

    
