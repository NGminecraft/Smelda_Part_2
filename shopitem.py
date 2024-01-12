from exceptions import *

class ShopItem:
    def __init__(self, name, price, id_dict, item_class, image):
        self.name = str(name)
        if price == float or price == int:
            self.price = price
        else:
            raise InvalidPrice(name)
        if type(id_dict) == dict:
            self.id_dict = id_dict
        else:
            raise InvalidIDS(name)
        self.item_class = item_class
        self.image_file = image
    
    def set_name(self, new_name):
        self.name = new_name
        
    def set_price(self, new_price):
        if new_price == float or new_price == int:
            self.price = new_price
        else:
            raise InvalidPrice(self.name)
        
    def set_id_dict(self, new_dict):
        if type(new_dict) == dict:
            self.id_dict = new_dict
        else:
            raise InvalidIDS(self.name)
        
    def set_item_class(self, new_classes):
        self.item_class = new_classes
        
    def use(self):
        raise NotImplemented