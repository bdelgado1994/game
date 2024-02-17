import pygame
import sys
from settings import Settings
from ship import Ship
class AlienIvasion:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self._update_screen()
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    self.ship.rect.x += 1
                elif event.key == pygame.K_LEFT:
                    self.ship.rect.x -= 1


    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()






if __name__=='__main__':
    ai=AlienIvasion()
    ai.run_game()