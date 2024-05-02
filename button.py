import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, image, image_highlight, pos_x, pos_y, scale):
        super().__init__()
        width = image.get_width()
        height= image.get_height()
        
        self.image_normal = pygame.transform.scale(image, (int(width*scale), int(height*scale))) 
        self.image_highlight = pygame.transform.scale(image_highlight, (int(width*scale), int(height*scale)))
        
        self.image = self.image_normal
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.clicked = False
        self.new_image = False
        
        

    def check_clicked(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.new_image = True
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == False:
                self.clicked = False
                
        if self.rect.collidepoint(pos) == False:
            self.new_image = False

        return action

    def update(self):
         if self.new_image == True:
            self.image = self.image_highlight
         if self.new_image == False:
            self.image = self.image_normal