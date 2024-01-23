from shopitem import ShopItem
from exceptions import *


class TeapotOfBrokenReality(ShopItem):
    def __init__(self, name, price, id_dict, item_class, image):
        super().__init__(name, price, id_dict, item_class, image)

    def use(self):
        raise error418
