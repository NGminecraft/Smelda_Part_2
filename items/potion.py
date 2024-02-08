from shopitem import ShopItem
from exceptions import *
import abc


class Potion(ShopItem):
    def __init__(self, name, price, id_dict, item_class, image):
        super().__init__(name, price, id_dict, item_class, image)

    def use(self):
        raise NotImplemented

    def calculate_price(self):
        return self.price * self.tier

    def calculate_tax(self):
        return self.calculate_price() * self.tax