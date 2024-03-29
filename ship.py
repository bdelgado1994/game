import pygame

class Ship:
    def __init__(self,ai_game) -> None:
        """Initialize the ship and set its starting position."""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image=pygame.image.load(r"images/DurrrSpaceShip.png")
        self.rect=self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom=self.screen_rect.midbottom
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)