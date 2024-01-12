"""All the exceptions"""
class InvalidIDS(Exception):
    def __init__(self, item_name):
        super().__init__(f"Attempted to store incorrect IDS for item {item_name}")

class InvalidPrice(Exception):
    def __init__(self, item_name):
        super().__init__(f"Attempted to store incorrect IDS for item {item_name}")
        
class error418(Exception):
    def __init__(self):
        super().__init__("Returned: 418: I'm a teapot!")