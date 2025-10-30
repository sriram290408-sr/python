class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_student(self):
        print(self.name, self.age, self.student_id)


class Child(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) 
        self.student_id = student_id 


x = Child("Sriram", 17, "001")

x.print_student() 