class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def print_values(self):
        print("a =", self.a)
        print("b =", self.b)

    def addition(self):
        add = (self.a + self.b)
        print("Addition:", add)

    def subtraction(self):
        sub = (self.a - self.b)
        print("Subtraction:", sub)
    
    def multiply(self):
        multi = (self.a * self.b)
        print("Multiply:", multi)
    
    def division(self):
        try:
            div = (self.a / self.b)
            print("Division:", int(div))
        except ZeroDivisionError:
            print("Error: b cannot be zero")

values = Calculator(20, 5)

values.print_values()
values.addition()
values.subtraction()
values.multiply()
values.division()
