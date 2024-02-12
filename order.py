from decimal import ROUND_DOWN
import warnings


class Order:
    def __init__(self):
        self._full_order = []
        self._location = 0

    def add(self, item):
        if item().name:
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
        items = {}
        for i in self._full_order:
            i = i().name
            if i in items.keys():
                items[i] += 1
            else:
                items[i] = 1
        length = 30
        result = []
        for key in items:
            result.append(f"{key}{" "*(length-(len(key)+len(str(items[key]))))}{items[key]}")
        items["Total: "] = self.order_cost() + self.order_tax()
        result.append(f"{"Subtotal: "}{" "*(length-(10-len(str(self.order_cost()))))}${round(self.order_cost(), 2)}")
        result.append(f"Taxes: {" "*(length-7-len(str(self.order_tax())))}${round(self.order_tax(), 2)}")
        result.append(f"Total: {" "*(length-7-len(str(self.order_cost() + self.order_tax())))}${round(self.order_cost() + self.order_tax(), 2)}")
        return "/n".join(result)

    def order_cost(self):
        return sum(i().calculate_price() for i in self._full_order)

    def order_tax(self):
        print(sum(i().calculate_tax() for i in self._full_order))
        return sum(i().calculate_tax() for i in self._full_order)
    
    def order(self, player, store, screen):
        if self.order_cost() + self.order_tax() <= player.money:
            player.money -= self.order_cost() + self.order_tax()
            for i in self._full_order:
                player.add_to_inventory(i)
            self._full_order = []
        store.pygame_multiline(screen, f"${str(player.money)}", (screen.get_width()-(len(str(player.money))+1)*15, 50, (255,0,0)))


if __name__ == "__main__":
    import main