import webbrowser
import sys
from shopitem import ShopItem
from exceptions import *
import pygame


class Newspaper(ShopItem):
    def __init__(self, name, price=100, image="Legend_of_Zink_Asset_Pack\Legend_of_Zink_Asset_Pack\HUD\PNG\sprHUDAssignAButton.png"):
        self.name = str(name)
        if type(price) == float or type(price) == int:
            self.price = price
        else:
            raise InvalidPrice(name, price)
        self.image = pygame.image.load(image)
        self.tax = 0.0725
        self.valid = True

    def use(self):
        raise error418

    def get_ids():
        return {"consumable": False}