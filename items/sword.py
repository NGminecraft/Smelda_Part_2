from shopitem import ShopItem
class sword(ShopItem):
    def __init__(self, name, price, id_dict, item_class, image, tier):
        super().__init__(name, price, id_dict, item_class, image)
        self.tier = tier
    
    def use(self):
        pass