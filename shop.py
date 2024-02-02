from items import *
from items.potions import *
import order
import pygame


class Shop:
    def __init__(self):
        self.is_open = False
        
    def update_gui(screen):
        s = pygame.Surface((1000, 1000))
        s.set_alpha(100)
        screen.blit(s, (0,0))