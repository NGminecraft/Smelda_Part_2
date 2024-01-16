import order
from items import sword
from items import potion

a = order.Order()

a.add(sword.sword("Sword of testing", 100, {"test": True}, {"melee":True}, "Nah", 8))
print(a.get_order())
a.add(potion.potion("name", 10, {"Test": True}, {"Potion":True}, "Nope"))
print(a.get_order())
for i in a:
    print(i)