import pygame
from exceptions import *
from abc import ABC, abstractmethod


class ShopItem(ABC):
    def __init__(self, name, price, id_dict, item_class, image):
        self.name = str(name)
        if type(price) == float or type(price) == int:
            self.price = price
        else:
            raise InvalidPrice(name, price)
        if type(id_dict) == dict:
            self.id_dict = id_dict
        else:
            raise InvalidIDS(name, id_dict)
        self.item_class = item_class
        self.image = pygame.image.load(image)
        self.tax = 0.0725
        self.valid = True

    def set_name(self, new_name):
        self.name = new_name

    def set_price(self, new_price):
        if new_price == float or new_price == int:
            self.price = new_price
        else:
            raise InvalidPrice(self.name, new_price)

    def set_id_dict(self, new_dict):
        if type(new_dict) == dict:
            self.id_dict = new_dict
        else:
            raise InvalidIDS(self.name, new_dict)

    def set_item_class(self, new_classes):
        self.item_class = new_classes

    @abstractmethod
    def use():
        raise NotImplemented

    @abstractmethod
    def calculate_price(self):
        return self.price

    @abstractmethod
    def calculate_tax(self):
        return self.calculate_price() * self.tax
