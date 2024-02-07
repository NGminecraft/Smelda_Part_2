from exceptions import *
import pygame
from shopitem import ShopItem


class Armor(ShopItem):
    def __init__(self, name, price, id_dict, item_class, image, tier):
        self.name = str(name)
        if type(price) == float or type(price) == int:
            self.price = price
        else:
            raise InvalidPrice(name, price)
        self.item_class = item_class
        self.image = pygame.image.load(image)
        self.tax = 0.0725
        self.valid = True
        self.tier = tier

    def use(self):
        pass
    
    def get_ids():
        return {"consumable": False}
