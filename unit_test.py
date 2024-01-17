import order
from items.sword import Sword
from items.potion import Potion
from items.armor import Armor
from items.arrow import Arrow
from items.teapotofbrokenreality import TeapotOfBrokenReality
import unittest

class UnitTesting(unittest.TestCase):
    def setUp(self):
        self.a = order.Order()
        self.b = order.Order()
    
    def test_add(self):
        self.b.add(Sword("Testing Sword", 184, {"Melee":True}, {"Sword":True, "Debugging":True}, "N/A", 100))
        self.assertEqual(len(self.b), 1)
        self.b.add(Potion("Testing Potion", 1658, {"Healing": False, "Harming":True}, {"Potion": True, "Debugging":True}, "N/A"))
        self.assertEqual(len(self.b.get_order()), 2)
        self.assertEqual(self.b.get_order()[-1].name, "Testing Potion")
        self.assertEqual(self.b.get_order()[-1].price, 1658)
        self.assertEqual(type(self.b.get_order()[-1].id_dict), dict)
        
    def test_loop(self):
        self.a.add(Potion("Testing Potion", 1658, {"Healing": False, "Harming":True}, {"Potion": True, "Debugging":True}, "N/A"))
        self.a.add(Sword("Testing Sword", 8723, {"Melee": True, "Ranged":False}, {"Sword": True, "Debugging":True}, "N/A", 10))
        self.a.add(Armor("Testing Armor", 6526, {"Armor": True}, {"Armor": True, "Debugging":True}, "N/A", 10))
        self.a.add(Arrow("Testing Arrow", 20, {"Melee": False, "Ranged":True}, {"Arrow": True, "Debugging":True}, "N/A"))
        self.a.add(TeapotOfBrokenReality("Testing Potion", 999999999, {"Destructive": True}, {"Cooking": True, "Debugging":True}, "N/A"))
        for i, v in enumerate(self.a):
            self.assertEqual(v, self.a.get_order()[i])
        
        
if __name__ == "__main__":
    unittest.main()