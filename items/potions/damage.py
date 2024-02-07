from potion import Potion
import pygame
from exceptions import *


class Damage(Potion):
    def __init__(self, name, price = 100, tier = 1, image="Legend_of_Zink_Asset_Pack\Legend_of_Zink_Asset_Pack\Menu_Icons\PNG\sprIconHealthJar.png", item_class = "potion"):
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

    def use(self, player):
        player.health -= 10 * self.tier

    def get_ids():
        return {"consumable":True}