class order:
    def __init__(self):
        self.data = []

    def add_item(self,item_name,price,quantity):
        now_item = {"item_name": item_name, "price": price, "quantity": quantity}


    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["price"] + item["quantity"]
        return total

print()