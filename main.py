import pygame
import chessboardExt
import piecesExt
import button
import random
import filehandler

pygame.init()

#Initialise main variables and constants
openings_handler = filehandler.OpeningsFileHandler("openings.txt")
openings_list = openings_handler.separate_openings()
board_width = 8*80
board_height = board_width
screen = pygame.display.set_mode((board_width, board_height + 50))
pygame.display.set_caption("Chess Practicer")
clock = pygame.time.Clock()
run = True
scene = "main"
time_interval = 0
setup_scene = False

#colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


#fonts
text_font_arial_small = pygame.font.SysFont("Arial", 35, bold=True)

#pieces images
wPawnImg = "Assets/pawn_wh.png"
wKnightImg = "Assets/knight_wh.png"
wBishopImg = "Assets/bishop_wh.png"
wRookImg = "Assets/rook_wh.png"
wQueenImg = "Assets/queen_wh.png"
wKingImg = "Assets/king_wh.png"

bPawnImg = "Assets/pawn_bl.png"
bKnightImg = "Assets/knight_bl.png"
bBishopImg = "Assets/bishop_bl.png"
bRookImg = "Assets/rook_bl.png"
bQueenImg = "Assets/queen_bl.png"
bKingImg = "Assets/king_bl.png"


chess_board = chessboardExt.ChessBoard("chess_board.png", board_width, board_height)

#general buttons
play_btn = button.Button(pygame.image.load("Assets/play_btn_1.png"), pygame.image.load("Assets/play_btn_2.png"), 90, 100, 0.6)
openings_btn = button.Button(pygame.image.load("Assets/openings_btn_1.png"), pygame.image.load("Assets/openings_btn_2.png"), 90, 275, 0.6)
other_btn = button.Button(pygame.image.load("Assets/other_btn_1.png"), pygame.image.load("Assets/other_btn_2.png"), 90, 450, 0.6)
back_btn = button.Button(pygame.image.load("Assets/back_btn_1.png"), pygame.image.load("Assets/back_btn_2.png"), 20, 650, 0.2)
next_btn = button.Button(pygame.image.load("Assets/next_btn_1.png"), pygame.image.load("Assets/next_btn_2.png"), 550, 650, 0.2)


#buttons for openings and vars
birds_opening_btn = button.Button(pygame.image.load("Assets/Buttons_ops/birds_btn_1.png"), pygame.image.load("Assets/Buttons_ops/birds_btn_2.png"), 20, 20, 0.4)
froms_gambit_btn = button.Button(pygame.image.load("Assets/Buttons_ops/froms_btn_1.png"), pygame.image.load("Assets/Buttons_ops/froms_btn_2.png"), 20, 20, 0.4)
grunfeld_defense_btn = button.Button(pygame.image.load("Assets/Buttons_ops/grunfeld_btn_1.png"), pygame.image.load("Assets/Buttons_ops/grunfeld_btn_2.png"), 20, 80, 0.4)
early_h4_btn = button.Button(pygame.image.load("Assets/Buttons_ops/h4_btn_1.png"), pygame.image.load("Assets/Buttons_ops/h4_btn_2.png"), 20, 20, 0.4)

#create sprite groups
main_scene_sprite_group = pygame.sprite.Group()
openings_scene_sprite_group = pygame.sprite.Group()
main_vars_scene_sprite_group = pygame.sprite.Group()
practice_opening_scene_sprite_group = pygame.sprite.Group()

#add sprites to the groups
main_scene_sprite_group.add(play_btn, openings_btn, other_btn)
openings_scene_sprite_group.add(back_btn, birds_opening_btn, grunfeld_defense_btn)
main_vars_scene_sprite_group.add(back_btn)
practice_opening_scene_sprite_group.add(back_btn, next_btn)


#general functions
def default_pieces_set(pov):
    #this function provides basic setup of chess board while taking into account what colour is our percpective
    chess_board.pieces = []

    white_king = piecesExt.ChessPiece(wKingImg, "king", "white", chess_board)
    white_queen = piecesExt.ChessPiece(wQueenImg, "queen", "white", chess_board)
    white_rook_1 = piecesExt.ChessPiece(wRookImg, "rook", "white", chess_board)
    white_rook_2 = piecesExt.ChessPiece(wRookImg, "rook", "white", chess_board)
    white_knight_1 = piecesExt.ChessPiece(wKnightImg, "knight", "white", chess_board)
    white_knight_2 = piecesExt.ChessPiece(wKnightImg, "knight", "white", chess_board)
    white_bishop_1 = piecesExt.ChessPiece(wBishopImg, "bishop", "white", chess_board)
    white_bishop_2 = piecesExt.ChessPiece(wBishopImg, "bishop", "white", chess_board)
    white_pawn_1 = piecesExt.ChessPiece(wPawnImg, "pawn", "white", chess_board)
    white_pawn_2 = piecesExt.ChessPiece(wPawnImg, "pawn", "white", chess_board)
    white_pawn_3 = piecesExt.ChessPiece(wPawnImg, "pawn", "white", chess_board)
    white_pawn_4 = piecesExt.ChessPiece(wPawnImg, "pawn", "white", chess_board)
    white_pawn_5 = piecesExt.ChessPiece(wPawnImg, "pawn", "white", chess_board)
    white_pawn_6 = piecesExt.ChessPiece(wPawnImg, "pawn", "white", chess_board)
    white_pawn_7 = piecesExt.ChessPiece(wPawnImg, "pawn", "white", chess_board)
    white_pawn_8 = piecesExt.ChessPiece(wPawnImg, "pawn", "white", chess_board)

    black_king = piecesExt.ChessPiece(bKingImg, "king", "black", chess_board)
    black_queen = piecesExt.ChessPiece(bQueenImg, "queen", "black", chess_board)
    black_rook_1 = piecesExt.ChessPiece(bRookImg, "rook", "black", chess_board)
    black_rook_2 = piecesExt.ChessPiece(bRookImg, "rook", "black", chess_board)
    black_knight_1 = piecesExt.ChessPiece(bKnightImg, "knight", "black", chess_board)
    black_knight_2 = piecesExt.ChessPiece(bKnightImg, "knight", "black", chess_board)
    black_bishop_1 = piecesExt.ChessPiece(bBishopImg, "bishop", "black", chess_board)
    black_bishop_2 = piecesExt.ChessPiece(bBishopImg, "bishop", "black", chess_board)
    black_pawn_1 = piecesExt.ChessPiece(bPawnImg, "pawn", "black", chess_board)
    black_pawn_2 = piecesExt.ChessPiece(bPawnImg, "pawn", "black", chess_board)
    black_pawn_3 = piecesExt.ChessPiece(bPawnImg, "pawn", "black", chess_board)
    black_pawn_4 = piecesExt.ChessPiece(bPawnImg, "pawn", "black", chess_board)
    black_pawn_5 = piecesExt.ChessPiece(bPawnImg, "pawn", "black", chess_board)
    black_pawn_6 = piecesExt.ChessPiece(bPawnImg, "pawn", "black", chess_board)
    black_pawn_7 = piecesExt.ChessPiece(bPawnImg, "pawn", "black", chess_board)
    black_pawn_8 = piecesExt.ChessPiece(bPawnImg, "pawn", "black", chess_board)
    
    piece_collection = [white_king, white_queen, white_rook_1, white_rook_2, white_knight_1,
                        white_knight_2, white_bishop_1, white_bishop_2, white_pawn_1, white_pawn_2,
                        white_pawn_3, white_pawn_4, white_pawn_5, white_pawn_6, white_pawn_7, white_pawn_8,

                        black_king, black_queen, black_rook_1, black_rook_2, black_knight_1, black_knight_2,
                        black_bishop_1, black_bishop_2, black_pawn_1, black_pawn_2, black_pawn_3, black_pawn_4,
                        black_pawn_5, black_pawn_6, black_pawn_7, black_pawn_8]
    
    piece_poses = ["e1", "d1", "a1", "h1", "b1", "g1", "c1", "f1", "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
                   "e8", "d8", "a8", "h8", "b8", "g8", "c8", "f8", "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"]
    
    index = 0
    for piece in piece_collection:
        piece.setPos(piece_poses[index], board_width, pov)
        index += 1

def getPosition(pov):
    #return piece position in chess notation form based on mouse cursor coordinates
    global board_height
    global board_width
    mx, my = pygame.mouse.get_pos()
    row = int(my//(board_height/8))
    col = int(mx//(board_width/8))
    if row >= 0 and row <=7 and col >= 0 and col <= 7:
        if pov == "white":
            letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
            numbers = [8, 7, 6, 5, 4, 3, 2, 1]
        elif pov == "black":
            letters = ["h", "g", "f", "e", "d", "c", "b", "a"]
            numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        position = str(letters[col])+str(numbers[row])
        return position
    
def identifyPieceByPos(pos):
    #return piece based on position given
    for piece in chess_board.pieces:
        if piece.position == pos:
            return piece
    return "NoPiece"

def produce_dictionary_for_openings(name):
    #produces dictionary that is used to instruct program to go through a specific opening and its variations
    #example of output: chess_opening_beta = {"player":"white", "opening":"Bird's", "main_variation":"From's Gambit", "side_variations":["Variation #1", "Variation #2"], "Variation #1": {"white": ["f2|f4", "f4:e5", "e5:d6"], "black": ["e7|e5", "d7|d6"]}, "Variation #2": {"white": ["f2|f4", "f4:e5", "d2|d4"], "black": ["e7|e5", "d7|d5"]}}
    colour, op_name, main_var_name, moves = openings_handler.search_for_name(name, openings_list)
    
    #this branch shoudn't really be followed ever as we choose an opening by clicking buttons rather than giving custom input
    if colour == False:
        return False
    
    
    else:
        side_variations, dict_moves = openings_handler.split_variations(moves)
        result_dict = {"player": colour, "opening": op_name, "main_variation": main_var_name, "side_variations": side_variations}
        for side_var in side_variations:
            result_dict[side_var] = dict_moves[side_var]
        return result_dict

while run:
    screen.fill(BLACK)
    chess_board.display_board(screen)
        

    if scene == "main":
        
        main_scene_sprite_group.draw(screen)
        main_scene_sprite_group.update()
        

        if play_btn.check_clicked() and time_interval > 3:
            scene = "play"
            time_interval = 0

        if openings_btn.check_clicked() and time_interval > 3:
            scene = "openings"
            time_interval = 0
    
        if other_btn.check_clicked() and time_interval > 3:
            scene = "other"
            time_interval = 0
    
    if scene == "play":
        #this scene is not fully complete, so bugs are expected (improvements left: enable castling, en passant, promotion, check and checkmate)
        if setup_scene == False: 
            pieceToMove = ""
            main_pov = "white"
            just_clicked = False
            mouse_coor = "in"
            setup_scene = True
            turn = "white"
            default_pieces_set(main_pov)  
        
        chess_board.display_pieces(screen)

        if pygame.mouse.get_pressed()[0] == True and pieceToMove != "NoPiece":

            #select piece if not selected
            if just_clicked == False:
                pieceToMove =  identifyPieceByPos(getPosition(main_pov))             
                just_clicked = True
                
            #if selected, move along if not taken and appropriate colour
            else:
                if pieceToMove.colour == turn:
                    if pieceToMove.taken == False:
                        mx, my = pygame.mouse.get_pos()
                        pieceToMove.display = False
                        screen.blit(pieceToMove.display_piece_img, (mx-(pieceToMove.display_piece_img.get_width()/2), my-(pieceToMove.display_piece_img.get_height()/2)))

        #if pygame.mouse.get_pressed()[0] == True and pieceToMove != "NoPiece":


        if pygame.mouse.get_pressed()[0] == False:
           
            if pieceToMove != "NoPiece" and just_clicked == True and pieceToMove.colour == turn:
                #checks if move legal
                if pieceToMove.checkMoveLegal(getPosition(main_pov), chess_board.pieces) == True:
                         
                    pieceToTake = identifyPieceByPos(getPosition(main_pov))

                    #"removes" taken piece by changing pos and visibility
                    if pieceToTake != "NoPiece" and pieceToTake != pieceToMove:
                        pieceToTake.taken = True
                        pieceToTake.setPos("offboard", board_width, main_pov)

                    #move piece 
                    pieceToMove.setPos(getPosition(main_pov), board_width, main_pov) 

                    if turn == "white":
                        turn = "black"
                    else:
                        turn = "white"

                    
                    

                #display piece
                pieceToMove.display = True


            pieceToMove = ""
            just_clicked = False


    if scene == "openings":
        openings_scene_sprite_group.draw(screen)
        openings_scene_sprite_group.update()

        if birds_opening_btn.check_clicked() and time_interval > 3:
            scene = "bird's"
            time_interval = 0
            main_vars_scene_sprite_group.add(froms_gambit_btn)
            

        if grunfeld_defense_btn.check_clicked() and time_interval > 3:
            scene = "grunfeld defence"
            time_interval = 0
            main_vars_scene_sprite_group.add(early_h4_btn)
            

        if back_btn.check_clicked() and time_interval > 3:
            scene = "main"
            time_interval = 0
            

#chosen opennings
    if scene == "bird's":
        main_vars_scene_sprite_group.draw(screen)
        main_vars_scene_sprite_group.update()

        if froms_gambit_btn.check_clicked() and time_interval > 3:
            scene = "practice opening"
            search_opening = "bird's" + ": " + "from's gambit"
            time_interval = 0
            chess_opening = produce_dictionary_for_openings(search_opening)

        if back_btn.check_clicked() and time_interval > 3:
            scene = "openings"
            time_interval = 0
            main_vars_scene_sprite_group.remove(froms_gambit_btn)

    if scene == "grunfeld defence":
        main_vars_scene_sprite_group.draw(screen)
        main_vars_scene_sprite_group.update()

        if early_h4_btn.check_clicked() and time_interval > 3:
            scene = "practice opening"
            search_opening = "grunfeld defence" + ": " + "early h4!"
            time_interval = 0
            chess_opening = produce_dictionary_for_openings(search_opening)
            

        if back_btn.check_clicked() and time_interval > 3:
            scene = "openings"
            time_interval = 0
            main_vars_scene_sprite_group.remove(early_h4_btn)

    if scene == "practice opening":
        def correct_move(piece, moveTo, variation, move_num):
            #check if move made is equal to the move in the chess opening
            global chess_opening
            global your_colour
            correct_move_full = chess_opening[variation][your_colour][move_num-1]

            if correct_move_full == "O-O-O":
                if your_colour== "black":
                    correct_move_from = "e8"
                    correct_move_to = "c8"
                    correct_move_type = "king"
                elif your_colour == "white":
                    correct_move_from = "e1"
                    correct_move_to = "c1"
                    correct_move_type = "king"
            elif correct_move_full == "O-O":
                if your_colour == "black":
                    correct_move_from = "e8"
                    correct_move_to = "g8"
                    correct_move_type = "king"
                elif your_colour == "white":
                    correct_move_from = "e1"
                    correct_move_to = "g1"
                    correct_move_type = "king"


            else:
                if "|" in correct_move_full:
                    position = correct_move_full.find("|")

                elif ":" in correct_move_full:
                    position = correct_move_full.find(":")

                elif "E" in correct_move_full:
                    position = correct_move_full.find("E")
                
                #pawn
                if len(correct_move_full[:position]) == 2:
                    correct_move_from = correct_move_full[:position]
                    correct_move_to = correct_move_full[position+1:]
                    correct_move_type = "pawn"

                if len(correct_move_full[:position]) == 3:
                    correct_move_from = correct_move_full[1:position]
                    correct_move_to = correct_move_full[position+1:]
                    if correct_move_full[0] == "B":
                        correct_move_type = "bishop"
                    elif correct_move_full[0] == "N":
                        correct_move_type = "knight"
                    elif correct_move_full[0] == "R":
                        correct_move_type = "rook"
                    elif correct_move_full[0] == "Q":
                        correct_move_type = "queen"
                    elif correct_move_full[0] == "K":
                        correct_move_type = "king"
                        
            if piece.type == correct_move_type and piece.position == correct_move_from and moveTo == correct_move_to:
                return True
                
            else:
                return False

        def perform_castling_for_rook(castling_type, move_colour):
            #as castling performed, move rook to an appropriate square
            global board_width
            global your_colour
            if castling_type == "O-O-O":
                if move_colour == "black":
                    rook = identifyPieceByPos("a8")
                    rook.setPos("d8", board_width, your_colour)
                elif move_colour == "white":
                    rook = identifyPieceByPos("a1")
                    rook.setPos("d1", board_width, your_colour)
            elif castling_type == "O-O":
                if move_colour == "black":
                    rook = identifyPieceByPos("h8")
                    rook.setPos("f8", board_width, your_colour)
                elif move_colour == "white":
                    rook = identifyPieceByPos("h1")
                    rook.setPos("f1", board_width, your_colour)

        def perform_en_passant(move_to, move_colour):
            #as en passant is performed, take the pawn
            global board_width
            global your_colour
            if move_colour == "white":
                taken_pawn_pos = move_to[0] + "5"
            elif move_colour == "black":
                taken_pawn_pos = move_to[0] + "4"
            
            taken_pawn = identifyPieceByPos(taken_pawn_pos)
            taken_pawn.taken = True
            taken_pawn.setPos("offboard", board_width, your_colour)

        def produce_opponent_move(variation, move_num):
            #prepare opponents move
            global your_colour
            global chess_opening
            if your_colour == "white":
                opposite_colour = "black"
                
            else:
                opposite_colour = "white"

            move_full = chess_opening[variation][opposite_colour][move_num-1]
                

            if move_full == "O-O-O":
                if opposite_colour == "black":
                    move_from = "e8"
                    move_to = "c8"
                    take = False
                elif opposite_colour == "white":
                    move_from = "e1"
                    move_to = "c1"
                    take = False
                perform_castling_for_rook(move_full, opposite_colour)
            elif move_full == "O-O":
                if opposite_colour == "black":
                    move_from = "e8"
                    move_to = "g8"
                    take = False
                elif opposite_colour == "white":
                    move_from = "e1"
                    move_to = "g1"
                    take = False
                perform_castling_for_rook(move_full, opposite_colour)


            else:   
                if "|" in move_full:
                    position = move_full.find("|")
                    take = False

                elif ":" in move_full:
                    position = move_full.find(":")
                    take = True

                elif "E" in move_full:
                    position = move_full.find("E")
                    take = False
                    

                #pawn
                if len(move_full[:position]) == 2:
                    move_from = move_full[:position]
                    move_to = move_full[position+1:]

                elif len(move_full[:position]) == 3:
                    move_from = move_full[1:position]
                    move_to = move_full[position+1:]

                
                if "E" in move_full:
                    perform_en_passant(move_to, opposite_colour)
                
            return move_from, move_to, take

        def perform_opponent_move(p_from, p_to, taken):
            #self explanatory
            global board_width
            global your_colour
            pieceToMove_opponent = identifyPieceByPos(p_from)
            if taken == True:
                pieceToTake_opponent = identifyPieceByPos(p_to)
                pieceToTake_opponent.taken = True
                pieceToTake_opponent.setPos("offboard", board_width, your_colour)
            pieceToMove_opponent.setPos(p_to, board_width, your_colour) 

        def choose_variation(opening_vars, current_var):
            #randomly chooses a side variation from a list
            vars = opening_vars
            print(vars, "-------------------------------")
            if current_var != None and len(vars)>1:
                crit_pos = vars.index(current_var)
                numbers = [i for i in range(0, len(vars))]
                numbers.remove(crit_pos)
                chosen_num = numbers[random.randint(0, len(numbers)-1)]
                chosen_var = vars[chosen_num]
            else:
                chosen_var = vars[random.randint(0, len(vars)-1)]
            
            return chosen_var
        
        def take_piece(square, piece_moved):
            #perform taking of a piece
            global your_colour
            global board_width
            pieceToTake = identifyPieceByPos(square)
            #"removes" taken piece by changing pos and visibility
            if pieceToTake != "NoPiece" and pieceToTake != piece_moved:
                pieceToTake.taken = True
                pieceToTake.setPos("offboard", board_width, your_colour)

        #prepare scene
        if setup_scene == False: 
            your_colour = chess_opening["player"]
            side_vars_list = chess_opening["side_variations"]
            if your_colour == "white":
                opponent_colour = "black"
            else:
                opponent_colour = "white"            
            pieceToMove = ""
            just_clicked = False
            text_opening_name_surface = text_font_arial_small.render(str(chess_opening["opening"])+": "+str(chess_opening["main_variation"]), True, (WHITE))
            move = 1
            variation_chosen = choose_variation(side_vars_list, None)
            default_pieces_set(your_colour)
            setup_scene = True

            #if first move not yours
            if your_colour == "black":
                pos_from, pos_to, pieceTaken = produce_opponent_move(variation_chosen, move)
                perform_opponent_move(pos_from, pos_to, pieceTaken)
            
        #dislay
        chess_board.display_pieces(screen)
        practice_opening_scene_sprite_group.draw(screen)
        practice_opening_scene_sprite_group.update()
        screen.blit(text_opening_name_surface, (120, 645))

        #when clicked
        if pygame.mouse.get_pressed()[0] == True and pieceToMove != "NoPiece":

            #select piece if not selected
            if just_clicked == False:
                pieceToMove =  identifyPieceByPos(getPosition(your_colour))             
                just_clicked = True
                
            #if selected, move along if not taken and appropriate colour
            else:
                if pieceToMove.colour == your_colour:
                    if pieceToMove.taken == False:
                        mx, my = pygame.mouse.get_pos()
                        pieceToMove.display = False
                        screen.blit(pieceToMove.display_piece_img, (mx-(pieceToMove.display_piece_img.get_width()/2), my-(pieceToMove.display_piece_img.get_height()/2)))

        #when unclicked
        if pygame.mouse.get_pressed()[0] == False:
           
            if pieceToMove != "NoPiece" and just_clicked == True:
                cursor_square = getPosition(your_colour)
                #checks if move correct
                if correct_move(pieceToMove, cursor_square, variation_chosen, move) == True:
                    move_done = chess_opening[variation_chosen][your_colour][move-1]
                    #if castle
                    if move_done == "O-O-O" or move_done== "O-O":
                        perform_castling_for_rook(move_done, your_colour)

                    #if en passant
                    if "E" in move_done:
                        perform_en_passant(cursor_square, your_colour, your_colour)
                         
                
                    take_piece(cursor_square, pieceToMove)

                    #move piece 
                    pieceToMove.setPos(cursor_square, board_width, your_colour) 

                    if your_colour == "black":
                        move += 1

                    
                    next_move = chess_opening[variation_chosen][opponent_colour][move-1]

                    #reset scene if last move was complete
                    if  next_move == "$":
                        default_pieces_set(your_colour)
                        move = 1
                        variation_chosen = choose_variation(side_vars_list, variation_chosen)
                        if your_colour == "black":
                            pos_from, pos_to, pieceTaken = produce_opponent_move(variation_chosen, move)
                            perform_opponent_move(pos_from, pos_to, pieceTaken)

                    #keep current scene if moves left to go
                    else:
                        pos_from, pos_to, pieceTaken = produce_opponent_move(variation_chosen, move)
                        perform_opponent_move(pos_from, pos_to, pieceTaken)

                        if your_colour == "white":
                            move += 1

                #display piece that was hovering
                pieceToMove.display = True


            pieceToMove = ""
            just_clicked = False    
        
        if back_btn.check_clicked() and time_interval > 3:
            
            scene = chess_opening["opening"].lower()
            setup_scene = False
            time_interval = 0

        if next_btn.check_clicked() and time_interval > 3:
            
            setup_scene = False 
            time_interval = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    if time_interval <= 20:
        time_interval += 1

    pygame.display.update()
    
    clock.tick(25)
pygame.quit()