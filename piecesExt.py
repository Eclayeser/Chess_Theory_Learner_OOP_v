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
        if self.type == "rook" or self.type == "king":
            self.has_moved = -1


    def add_piece_toBoard(self, board):
        board.pieces.append(self)


    def setPos(self, pos, boardsize, pov):
        #place piece on a desired square or place off the board
        if pos != "offboard":
            letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
            numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
            if len(pos) == 2 and pos[0] in letters and pos[1] in numbers:
                self.position = str(pos)
            else:
                raise ValueError("Invalid piece position:", self.name)
        
            self.calc_coordinates(boardsize, boardsize, pov)

            #check for castling (intended to be used in PLAY mode)
            if self.type == "rook" or self.type == "king" and self.has_moved < 1:
                self.has_moved += 1

        else:
            self.position = "offboard"
        
    def calc_coordinates(self, board_w, board_h, pov):
        #calculate corrcet coords for a piece taking into account player's percpective
        if pov == "white":
            letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
            numbers = ["8", "7", "6", "5", "4", "3", "2", "1"]
        elif pov == "black":
            letters = ["h", "g", "f", "e", "d", "c", "b", "a"]
            numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
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
        #used to check if move legal (intended to be used in PLAY mode; incomplete) 
        if moveTo == None: #or whose_turn != self.colour:
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
            
        if self.type == "rook":
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
    
        if self.type == "bishop":
            #validate a move
            if abs(indLetF-indLetT) == abs(indNumF-indNumT):
                interval = abs(indLetF-indLetT)

                #right-down diagonal
                if indLetF-indLetT < 0 and indNumF-indNumT > 0:
                    for j in range(1, interval+1):
                        position_to_check = letters[indLetF+j]+numbers[indNumF-j]
                        if traceToFindPieces(piecesToTake, position_to_check) != None:
                            if j == interval:
                                if self.differentColour(piecesToTake, position_to_check):
                                    return True
                            return False

                #right-up diagonal        
                if indLetF-indLetT < 0 and indNumF-indNumT < 0:
                    for j in range(1, interval+1):
                        position_to_check = letters[indLetF+j]+numbers[indNumF+j]
                        if traceToFindPieces(piecesToTake, position_to_check) != None:
                            if j == interval:
                                if self.differentColour(piecesToTake, position_to_check):
                                    return True
                            return False

                #left-down diagonal        
                if indLetF-indLetT > 0 and indNumF-indNumT > 0:
                    for j in range(1, interval+1): 
                        position_to_check = letters[indLetF-j]+numbers[indNumF-j]
                        if traceToFindPieces(piecesToTake, position_to_check) != None:
                            if j == interval:
                                if self.differentColour(piecesToTake, position_to_check):
                                    return True
                            return False
                        
                #left-up diagonal        
                if indLetF-indLetT > 0 and indNumF-indNumT < 0:
                    for j in range(1, interval+1):
                        position_to_check = letters[indLetF-j]+numbers[indNumF+j]
                        if traceToFindPieces(piecesToTake, position_to_check) != None:
                            if j == interval:
                                if self.differentColour(piecesToTake, position_to_check):
                                    return True
                            return False


                return True
            
        if self.type == "queen":
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
                
            
            if abs(indLetF-indLetT) == abs(indNumF-indNumT):
                interval = abs(indLetF-indLetT)

                #right-down diagonal
                if indLetF-indLetT < 0 and indNumF-indNumT > 0:
                    for j in range(1, interval+1):
                        position_to_check = letters[indLetF+j]+numbers[indNumF-j]
                        if traceToFindPieces(piecesToTake, position_to_check) != None:
                            if j == interval:
                                if self.differentColour(piecesToTake, position_to_check):
                                    return True
                            return False

                #right-up diagonal        
                if indLetF-indLetT < 0 and indNumF-indNumT < 0:
                    for j in range(1, interval+1):
                        position_to_check = letters[indLetF+j]+numbers[indNumF+j]
                        if traceToFindPieces(piecesToTake, position_to_check) != None:
                            if j == interval:
                                if self.differentColour(piecesToTake, position_to_check):
                                    return True
                            return False

                #left-down diagonal        
                if indLetF-indLetT > 0 and indNumF-indNumT > 0:
                    for j in range(1, interval+1): 
                        position_to_check = letters[indLetF-j]+numbers[indNumF-j]
                        if traceToFindPieces(piecesToTake, position_to_check) != None:
                            if j == interval:
                                if self.differentColour(piecesToTake, position_to_check):
                                    return True
                            return False
                            
                #left-up diagonal        
                if indLetF-indLetT > 0 and indNumF-indNumT < 0:
                    for j in range(1, interval+1):
                        position_to_check = letters[indLetF-j]+numbers[indNumF+j]
                        if traceToFindPieces(piecesToTake, position_to_check) != None:
                            if j == interval:
                                if self.differentColour(piecesToTake, position_to_check):
                                    return True
                            return False


                return True

        if self.type == "king":
            #validate a move
            if abs(indLetF-indLetT) <= 1 and abs(indNumF-indNumT) <= 1:
                #check if hasn't moved
                if indLetF-indLetT == 0 and indNumF-indNumT == 0:
                    return False
                #check if a piece is present and if opposite colour - takeable
                else:
                    if self.differentColour(piecesToTake, moveTo):
                        return True
               
            if self.colour == "white": 
                #short castle white   
                if moveTo == "g1" and self.has_moved == 0:
                    rook_square = traceToFindPieces(piecesToTake, "h1")
                    if traceToFindPieces(piecesToTake, "f1") == None and traceToFindPieces(piecesToTake, "g1") == None and rook_square != None:
                        if rook_square.has_moved == 0:
                            rook_square.setPos("f1", 8*80)
                            return True
            
                #long castle white       
                if moveTo == "c1" and self.has_moved == 0:
                    rook_square = traceToFindPieces(piecesToTake, "a1")
                    if traceToFindPieces(piecesToTake, "b1") == None and traceToFindPieces(piecesToTake, "c1") == None and traceToFindPieces(piecesToTake, "d1") == None and rook_square != None:
                        if rook_square.has_moved == 0:
                            rook_square.setPos("d1", 8*80)
                            return True
                        
            if self.colour == "black": 
                #short castle black   
                if moveTo == "g8" and self.has_moved == 0:
                    rook_square = traceToFindPieces(piecesToTake, "h8")
                    if traceToFindPieces(piecesToTake, "f8") == None and traceToFindPieces(piecesToTake, "g8") == None and rook_square != None:
                        if rook_square.has_moved == 0:
                            rook_square.setPos("f8", 8*80)
                            return True
            
                #long castle black       
                if moveTo == "c8" and self.has_moved == 0:
                    rook_square = traceToFindPieces(piecesToTake, "a8")
                    if traceToFindPieces(piecesToTake, "b8") == None and traceToFindPieces(piecesToTake, "c8") == None and traceToFindPieces(piecesToTake, "d8") == None and rook_square != None:
                        if rook_square.has_moved == 0:
                            rook_square.setPos("d8", 8*80)
                            return True
                        
        if self.type == "pawn":
            if self.colour == "white":
                #forward
                if indNumF-indNumT == -1 and indLetF-indLetT == 0:
                    if traceToFindPieces(piecesToTake, moveTo) == None:
                        return True
                #take to left/right
                if indNumF-indNumT == -1 and abs(indLetF-indLetT) == 1:
                    if traceToFindPieces(piecesToTake, moveTo) != None:
                       if self.differentColour(piecesToTake, moveTo):
                            return True
                #double forward
                if indNumF-indNumT == -2 and indLetF-indLetT == 0:
                    if self.position[1] == "2":
                        if traceToFindPieces(piecesToTake, moveTo) == None:
                            return True
            
            elif self.colour == "black":
                #forward
                if indNumF-indNumT == 1 and indLetF-indLetT == 0:
                    if traceToFindPieces(piecesToTake, moveTo) == None:
                        return True
                #take to left/right
                if indNumF-indNumT == 1 and abs(indLetF-indLetT) == 1:
                    if traceToFindPieces(piecesToTake, moveTo) != None:
                       if self.differentColour(piecesToTake, moveTo):
                            return True
                #double forward
                if indNumF-indNumT == 2 and indLetF-indLetT == 0:
                    if self.position[1] == "7":
                        if traceToFindPieces(piecesToTake, moveTo) == None:
                            return True
                    



        return False
    
    def differentColour(self, pieces, to_sq):
        #assists checkMoveLegal function
        piece_on_to_sq = traceToFindPieces(pieces, to_sq)
        if piece_on_to_sq == None:
            return True
        elif piece_on_to_sq.colour != self.colour:
            return True 
        return False
    

def traceToFindPieces(pieces, to):
    #traverse pieces list to see if one exists
    for piece in pieces:
        if piece.position == to:
            return piece
    return None
    


    

    
