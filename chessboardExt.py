import pygame

class ChessBoard(pygame.sprite.Sprite):
    def __init__(self, chessBoardImg, width, height):
        super().__init__()
        self.display_board_img = pygame.transform.scale(pygame.image.load(f"Assets/{chessBoardImg}"), (width, height))
        self.pieces = []

    def display_board(self, surface):
        surface.blit(self.display_board_img, (0,0))

    def display_pieces(self, surface):
        for piece in self.pieces:
            if piece.display == True and piece.taken == False:
                surface.blit(piece.display_piece_img, (piece.x_coor, piece.y_coor))
