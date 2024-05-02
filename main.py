import pygame
import chessboardExt
import piecesExt
import button

pygame.init()

board_width = 8*80
board_height = 8*80
screen = pygame.display.set_mode((board_width, board_height + 50))
pygame.display.set_caption("Chess Practicer")
clock = pygame.time.Clock()
run = True
scene = "main"
time_interval = 0

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

first_scene_sprite_group = pygame.sprite.Group()
first_scene_sprite_group.add(play_btn, openings_btn, other_btn)


def default_pieces_set():
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
default_pieces_set()


while run:
    chess_board.display_board(screen)

    if scene == "main":
        first_scene_sprite_group.draw(screen)
        first_scene_sprite_group.update()

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
        chess_board.display_pieces(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    if time_interval <= 20:
        time_interval += 1

    pygame.display.update()
    clock.tick(40)
pygame.quit()