from items import *
from items.potions import *


class Order:
    def __init__(self):
        self.full_order = []
        self.location = 0
    
    def add(self, item):
        if item.name:
            self.full_order.append(item)
            
    def get_order(self):
        return tuple(self.full_order)
    
    def __len__(self):
        return len(self.full_order)
    
    def __iter__(self):
        return iter(self.full_order)
    
    def __next__(self):
        return self.full_order[self.location]