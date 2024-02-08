import warnings


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
        items = {}
        for i in self._full_order:
            if i in items:
                items[i] += 1
            else:
                items[i] = 1
        items["Subtotal: "] = self.order_cost()
        items["Taxes: "] = self.order_tax()
        items["Total: "] = self.order_cost() + self.order_tax()
        length = 20
        result = []
        for key in items:
            print(key)
            print(type(key))
            result.append(f"{key}{" "*(10-len(key)+len(str(length)))}{items[key]}")
        return "/n".join(result)

    def order_cost(self):
        return sum(i.calculate_price() for i in self._full_order)

    def order_tax(self):
        return sum(i.calculate_tax() for i in self._full_order)
