"""All the exceptions"""


class InvalidIDS(Exception):
    def __init__(self, item_name, info):
        super().__init__(f"Attempted to store incorrect IDS for item {item_name}. ({info})")


class InvalidPrice(Exception):
    def __init__(self, item_name, info):
        super().__init__(f"Attempted to store incorrect IDS for item {item_name}. ({info})")


class error418(Exception):
    def __init__(self):
        super().__init__("Returned: 418: I'm a teapot!")
