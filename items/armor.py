from exceptions import *
import pygame
from shopitem import ShopItem


class Armor(ShopItem):
    def __init__(self, name, price = 100, tier=1, image="Legend_of_Zink_Asset_Pack\Legend_of_Zink_Asset_Pack\Menu_Icons\PNG\sprIconShoe.png"):
        self.name = str(name)
        if type(price) == float or type(price) == int:
            self.price = price
        else:
            raise InvalidPrice(name, price)
        self.image = pygame.image.load(image)
        self.tax = 0.0725
        self.valid = True
        self.tier = tier

    def use(self):
        pass
    
    def get_ids():
        return {"consumable": False}
