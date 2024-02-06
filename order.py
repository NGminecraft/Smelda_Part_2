from items import *
import warnings
from items.sword import Sword
from items.potion import Potion
from items.shopitem import ShopItem


class Order:
    def __init__(self):
        self._full_order = []
        self._location = 0
    
    def add(self, item):
        if item.name:
            self._full_order.append(item)
            
    def get_order(self):
        return tuple(self._full_order)
    
    def __len__(self):
        return len(self._full_order)
    
    def __iter__(self):
        return iter(self._full_order)
    
    def __next__(self):
        try:
            self._location += 1
            return self._full_order[self._location - 1]
        except IndexError:
            warnings.warn("Attempted to access more orders then available")
            return None
        
    def __str__(self):
        return self
