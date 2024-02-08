import pygame
from potion import Potion

from exceptions import *


class Health(Potion):
    def __init__(self, name="Health Potion", price=100, tier=1,
                 image="Legend_of_Zink_Asset_Pack\\Legend_of_Zink_Asset_Pack\\Menu_Icons\\PNG\\sprIconHealthPotion.png",
                 item_class="potion"):
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
        player.health += 10 * self.tier

    def get_ids():
        return {"consumable": True}

    def calculate_price(self):
        return self.price * self.tier

    def calculate_tax(self):
        return self.calculate_price() * self.tax
