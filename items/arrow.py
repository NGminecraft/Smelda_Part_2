from shopitem import ShopItem
from exceptions import *
import pygame


class Arrow(ShopItem):
    def __init__(self, name, price, item_class, image="Legend_of_Zink_Asset_Pack\Legend_of_Zink_Asset_Pack\Menu_Icons\PNG\sprIconMiniArrow.png"):
        self.name = str(name)
        if type(price) == float or type(price) == int:
            self.price = price
        else:
            raise InvalidPrice(name, price)
        self.item_class = item_class
        self.image = pygame.image.load(image)
        self.tax = 0.0725
        self.valid = True

    def use(self):
        pass

    def get_ids():
        return {"consumable":True}