from shopitem import ShopItem

class Potion(ShopItem):
    def __init__(self, name, price, id_dict, item_class, image):
        super().__init__(name, price, id_dict, item_class, image)
        
    def use(self):
        pass