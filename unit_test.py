import sys
sys.path.append(sys.path[0]+"\\items")
import order
from items import sword
from items import potion
from items import shopitem

a = order.Order()

a.add(sword.Sword("Sword of testing", 100, {"test": True}, {"melee":True}, "Nah", 8))
a.add(potion.Potion("name", 10, {"Test": True}, {"Potion":True}, "Nope"))
print(a.full_order)