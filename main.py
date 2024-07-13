import pygame
import chessboardExt
import piecesExt
import button
import time
import random
import filehandler

pygame.init()

openings_handler = filehandler.OpeningsFileHandler("openings.txt")
openings_list = openings_handler.separate_openings()
board_width = 8*80
board_height = 8*80
screen = pygame.display.set_mode((board_width, board_height + 50))
pygame.display.set_caption("Chess Practicer")
clock = pygame.time.Clock()
run = True
scene = "main"
time_interval = 0
setup_scene = False
WHITE = (255, 255, 255)

text_font_arial_small = pygame.font.SysFont("Arial", 35, bold=True)

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
play_btn = button.Button(pygame.image.load("Assets/play_btn_1.png"), pygame.image.load("Assets/play_btn_2.png"), 90, 100, 0.6)
openings_btn = button.Button(pygame.image.load("Assets/openings_btn_1.png"), pygame.image.load("Assets/openings_btn_2.png"), 90, 275, 0.6)
other_btn = button.Button(pygame.image.load("Assets/other_btn_1.png"), pygame.image.load("Assets/other_btn_2.png"), 90, 450, 0.6)
back_btn = button.Button(pygame.image.load("Assets/back_btn_1.png"), pygame.image.load("Assets/back_btn_2.png"), 20, 650, 0.2)
next_btn = button.Button(pygame.image.load("Assets/next_btn_1.png"), pygame.image.load("Assets/next_btn_2.png"), 550, 650, 0.2)

main_scene_sprite_group = pygame.sprite.Group()
openings_scene_sprite_group = pygame.sprite.Group()
main_vars_scene_sprite_group = pygame.sprite.Group()
practice_opening_scene_sprite_group = pygame.sprite.Group()
main_scene_sprite_group.add(play_btn, openings_btn, other_btn)


#buttons for openings and vars
birds_opening_btn = button.Button(pygame.image.load("Assets/birds_btn_1.png"), pygame.image.load("Assets/birds_btn_2.png"), 20, 20, 0.4)
froms_gambit_btn = button.Button(pygame.image.load("Assets/froms_btn_1.png"), pygame.image.load("Assets/froms_btn_2.png"), 20, 20, 0.4)

openings_scene_sprite_group.add(back_btn, birds_opening_btn)
main_vars_scene_sprite_group.add(back_btn)
practice_opening_scene_sprite_group.add(back_btn, next_btn)


def default_pieces_set():
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
        piece.setPos(piece_poses[index], board_width)
        index += 1

def getPosition():
    global board_height
    global board_width
    mx, my = pygame.mouse.get_pos()
    row = int(my//(board_height/8))
    col = int(mx//(board_width/8))
    if row >= 0 and row <=7 and col >= 0 and col <= 7:
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        numbers = [8, 7, 6, 5, 4, 3, 2, 1]
        position = str(letters[col])+str(numbers[row])
        return position
    
def identifyPieceByPos(pos):
    for piece in chess_board.pieces:
        if piece.position == pos:
            return piece
    return "NoPiece"

def produce_dictionary_for_openings(name):
    #example of output: chess_opening_beta = {"player":"white", "opening":"Bird's", "main_variation":"From's Gambit", "side_variations":["Variation #1", "Variation #2"], "Variation #1": {"white": ["f2|f4", "f4:e5", "e5:d6"], "black": ["e7|e5", "d7|d6"]}, "Variation #2": {"white": ["f2|f4", "f4:e5", "d2|d4"], "black": ["e7|e5", "d7|d5"]}}
    colour, op_name, main_var_name, moves = openings_handler.search_for_name(name, openings_list)
    if colour == False:
        return False
    else:
        side_variations, dict_moves = openings_handler.split_variations(moves)
        result_dict = {"player": colour, "opening": op_name, "main_variation": main_var_name, "side_variations": side_variations}
        for side_var in side_variations:
            result_dict[side_var] = dict_moves[side_var]
        return result_dict

while run:
    screen.fill((0,0,0))
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
        if setup_scene == False:
            default_pieces_set()   
            pieceToMove = ""
            just_clicked = False
            mouse_coor = "in"
            setup_scene = True
            turn = "white"
        
        chess_board.display_pieces(screen)

        if pygame.mouse.get_pressed()[0] == True and pieceToMove != "NoPiece":

            #select piece if not selected
            if just_clicked == False:
                pieceToMove =  identifyPieceByPos(getPosition())             
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
                if pieceToMove.checkMoveLegal(getPosition(), chess_board.pieces) == True:
                         
                    pieceToTake = identifyPieceByPos(getPosition())

                    #"removes" taken piece by changing pos and visibility
                    if pieceToTake != "NoPiece" and pieceToTake != pieceToMove:
                        pieceToTake.taken = True
                        pieceToTake.setPos("offboard", board_width)

                    #move piece 
                    pieceToMove.setPos(getPosition(), board_width) 

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
            search_opening = "bird's"

        if back_btn.check_clicked() and time_interval > 3:
            scene = "main"
            time_interval = 0
            

    if scene == "bird's":
        main_vars_scene_sprite_group.draw(screen)
        main_vars_scene_sprite_group.update()

        if froms_gambit_btn.check_clicked() and time_interval > 3:
            scene = "practice opening"
            search_opening = search_opening + ": " + "from's gambit"
            time_interval = 0
            #following must be generated according to what opening was chosen and its variation using file handler + randomise side variations
            #chess_opening = {"player":"white", "opening":"Bird's", "main_variation":"From's Gambit", "side_variation":"Variation #1", "white": ["f2|f4", "f4:e5", "e5:d6"], "black": ["e7|e5", "d7|d6"]}
            chess_opening_beta = produce_dictionary_for_openings(search_opening)
            #chess_opening_beta = {"player":"white", "opening":"Bird's", "main_variation":"From's Gambit", "side_variations":["Variation #1", "Variation #2"], "Variation #1": {"white": ["f2|f4", "f4:e5", "e5:d6"], "black": ["e7|e5", "d7|d6"]}, "Variation #2": {"white": ["f2|f4", "f4:e5", "d2|d4"], "black": ["e7|e5", "d7|d5"]}}
            #print(chess_opening_beta)

        if back_btn.check_clicked() and time_interval > 3:
            scene = "openings"
            time_interval = 0
            main_vars_scene_sprite_group.remove(froms_gambit_btn)

    if scene == "practice opening":
        def correct_move(piece, moveTo, opening, variation, move_num):
            correct_move_full = opening[variation][opening["player"]][move_num-1]
            
            if "|" in correct_move_full:
                position = correct_move_full.find("|")

            elif ":" in correct_move_full:
                position = correct_move_full.find(":")
            
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
                    

            #print(correct_move_type, correct_move_from, correct_move_to)
            #print(piece.type, piece.position, moveTo)

            if piece.type == correct_move_type and piece.position == correct_move_from and moveTo == correct_move_to:
                return True
            
            else:
                return False

        def perform_opponent_move(opening, variation, move_num):
            if opening["player"] == "white":
                move_full = opening[variation]["black"][move_num-1]
            else:
                move_full = opening[variation]["white"][move_num-1]
            
            if "|" in move_full:
                position = move_full.find("|")
                take = False

            elif ":" in move_full:
                position = move_full.find(":")
                take = True
            
            #pawn
            if len(move_full[:position]) == 2:
                move_from = move_full[:position]
                move_to = move_full[position+1:]

            elif len(move_full[:position]) == 3:
                move_from = move_full[1:position]
                move_to = move_full[position+1:]
                
            return move_from, move_to, take

        def choose_variation(opening, current_var):
            vars = opening["side_variations"]
            if current_var != None:
                crit_pos = vars.index(current_var)
                numbers = [i for i in range(0, len(vars))]
                numbers.remove(crit_pos)
                chosen_num = numbers[random.randint(0, len(numbers)-1)]
                chosen_var = vars[chosen_num]
            else:
                chosen_var = vars[random.randint(0, len(vars)-1)]
            #print (chosen_var)
            return chosen_var

        if setup_scene == False:           
            default_pieces_set()   
            pieceToMove = ""
            just_clicked = False
            text_opening_name_surface = text_font_arial_small.render(str(chess_opening_beta["opening"])+": "+str(chess_opening_beta["main_variation"]), True, (WHITE))
            setup_scene = True
            turn = chess_opening_beta["player"]
            move = 1
            variation_chosen = choose_variation(chess_opening_beta, None)
        
        chess_board.display_pieces(screen)
        practice_opening_scene_sprite_group.draw(screen)
        practice_opening_scene_sprite_group.update()
        screen.blit(text_opening_name_surface, (120, 645))

        if pygame.mouse.get_pressed()[0] == True and pieceToMove != "NoPiece":

            #select piece if not selected
            if just_clicked == False:
                pieceToMove =  identifyPieceByPos(getPosition())             
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
                if correct_move(pieceToMove, getPosition(), chess_opening_beta, variation_chosen, move) == True:
                         
                    pieceToTake = identifyPieceByPos(getPosition())

                    #"removes" taken piece by changing pos and visibility
                    if pieceToTake != "NoPiece" and pieceToTake != pieceToMove:
                        pieceToTake.taken = True
                        pieceToTake.setPos("offboard", board_width)

                    #move piece 
                    pieceToMove.setPos(getPosition(), board_width) 

                    
                    #perform opponent's move if not finished theory
                    print(chess_opening_beta[variation_chosen]["black"][move-1])
                    if chess_opening_beta[variation_chosen]["black"][move-1] == "$":
                        default_pieces_set()
                        move = 1
                        variation_chosen = choose_variation(chess_opening_beta, variation_chosen)
                    else:
                        pos_from, pos_to, pieceTaken = perform_opponent_move(chess_opening_beta, variation_chosen, move)
                        pieceToMove_opponent = identifyPieceByPos(pos_from)
                        #print(pos_from)
                        #print(pieceToMove_opponent)
                        if pieceTaken == True:
                            pieceToTake_opponent = identifyPieceByPos(pos_to)
                            pieceToTake_opponent.taken = True
                            pieceToTake_opponent.setPos("offboard", board_width)
                        pieceToMove_opponent.setPos(pos_to, board_width) 
                        move += 1

                #display piece
                pieceToMove.display = True


            pieceToMove = ""
            just_clicked = False    
        
        if back_btn.check_clicked() and time_interval > 3:
            
            scene = chess_opening_beta["opening"].lower()
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