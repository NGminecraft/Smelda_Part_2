import webbrowser
import sys
from shopitem import ShopItem
from exceptions import *
import pygame


class Newspaper(ShopItem):
    def __init__(self, name="The Daily Newspaper", price=100,
                 image="Legend_of_Zink_Asset_Pack\\Legend_of_Zink_Asset_Pack\\HUD\\PNG\\sprHUDAssignAButton.png"):
        self.name = str(name)
        if type(price) == float or type(price) == int:
            self.price = price
        else:
            raise InvalidPrice(name, price)
        self.image = pygame.image.load(image)
        self.tax = 0.0725
        self.valid = True

    def use(self):
        webbrowser.open_new_tab("Legend_of_Zink_Asset_Pack\\Legend_of_Zink_Asset_Pack\\Collectables\\PNG\\WebBest.html")

    def get_ids():
        return {"consumable": False}

    def calculate_price(self):
        return self.price

    def calculate_tax(self):
        return self.calculate_price() * self.tax
