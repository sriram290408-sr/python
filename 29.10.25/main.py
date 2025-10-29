# #One function is called at one time
# #Without parameter
# #requested function calls

# x = "hello world"

# a = x.capitalize()
# b = x.upper()
# c = x.lower()
# d = x.split(" ")
# e = list(x)
# f = e.reverse()
# print([a,b,c,d,e,f])

#class (class_name)
class OrderRestaurant:
    def __init__(self, order_id, rest_id, bill_amount):
        self.order_id = order_id
        self.rest_id = rest_id
        self.bill_amount = bill_amount
        pass

#variable = call your class with attribute (need to assign Variable)
order1 = OrderRestaurant(101, "R001", 550.75)
print(order1.order_id)     
print(order1.rest_id)      
print(order1.bill_amount)