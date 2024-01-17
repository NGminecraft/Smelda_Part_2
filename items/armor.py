import sys
sys.path.append(sys.path[0]+"\\items")
from shopitem import ShopItem

class Armor(ShopItem):
    def __init__(self, name, price, id_dict, item_class, image, tier):
        super().__init__(name, price, id_dict, item_class, image)
        self.tier = tier
    
    def use(self):
        pass