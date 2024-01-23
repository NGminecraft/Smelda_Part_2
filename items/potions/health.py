from potion import Potion


class Health(Potion):
    def __init__(self, name, price, id_dict, item_class, image, tier):
        super().__init__(name, price, id_dict, item_class, image)
        self.tier = tier

    def use(self, player):
        player.health += 10 * self.tier
