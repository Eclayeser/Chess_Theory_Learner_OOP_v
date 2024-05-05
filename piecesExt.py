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
        self.display = True
        self.taken = False


    def add_piece_toBoard(self, board):
        board.pieces.append(self)


    def setPos(self, pos, boardsize):
        if pos != "offboard":
            letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
            numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
            if len(pos) == 2 and pos[0] in letters and pos[1] in numbers:
                self.position = str(pos)
            else:
                raise ValueError("Invalid piece position:", self.name)
        
            self.calc_coordinates(boardsize, boardsize)

        else:
            self.position = "offboard"
        
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

    def checkMoveLegal(self, moveTo, piecesToTake):
        if moveTo == None:
            return False
        
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
        indLetF = letters.index(self.position[0])
        indNumF = numbers.index(self.position[1])
        indLetT = letters.index(moveTo[0])
        indNumT = numbers.index(moveTo[1])
        
        if self.type == "knight":
            #validate a move
            if (abs(indLetF-indLetT) == 1 and abs(indNumF-indNumT) == 2) or (abs(indLetF-indLetT) == 2 and abs(indNumF-indNumT) == 1):
                #check if a piece is present and if opposite colour - takeable   
                if self.differentColour(piecesToTake, moveTo):
                    return True
            
        elif self.type == "rook":
            #validates vertical moves
            if ((indLetF-indLetT) == 0 and (indNumF-indNumT) != 0):
                #checks if any pieces on the way if target square below
                if indNumF>indNumT:
                    for j in range(indNumT, indNumF):
                        position_to_check = moveTo[0]+numbers[j]
                        #if piece present checks if it is on the target square and opposite colour, else illegal move
                        if traceToFindPieces(piecesToTake, position_to_check) != None:
                            if j == indNumT:
                                if self.differentColour(piecesToTake, position_to_check):
                                    return True
                            return False
                        
                #checks if any pieces on the way if target square above
                elif indNumT>indNumF:       
                    for j in range(indNumF, indNumT):
                        position_to_check = moveTo[0]+numbers[j+1]
                        #if piece present checks if it is on the target square and opposite colour, else illegal move
                        if traceToFindPieces(piecesToTake, position_to_check) != None:
                            if j == indNumT-1:
                                if self.differentColour(piecesToTake, position_to_check):
                                    return True
                            return False
                        

                #no obstacles found, legal move
                return True 
            
            #validates horizontal moves similarly to vertical
            if ((indLetF-indLetT) != 0 and (indNumF-indNumT) == 0):
              
                if indLetF>indLetT:
                    for j in range(indLetT, indLetF):
                        position_to_check = letters[j]+moveTo[1]
                        if traceToFindPieces(piecesToTake, position_to_check) != None:
                            if j == indLetT:
                                if self.differentColour(piecesToTake, position_to_check):
                                    return True
                            return False
                elif indLetT>indLetF:       
                    for j in range(indLetF, indLetT):
                        position_to_check = letters[j+1]+moveTo[1]
                        if traceToFindPieces(piecesToTake, position_to_check) != None:
                            if j == indLetT-1:
                                if self.differentColour(piecesToTake, position_to_check):
                                    return True
                            return False
                return True
            
        return False
    
    def differentColour(self, pieces, to_sq):
        piece_on_to_sq = traceToFindPieces(pieces, to_sq)
        if piece_on_to_sq == None:
            return True
        elif piece_on_to_sq.colour != self.colour:
            return True 
        return False
    

def traceToFindPieces(pieces, to):
    for piece in pieces:
        if piece.position == to:
            return piece
    return None
    


    

    
