#sum - 1
# class todolist:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task_id, task_name, status="pending"):
#         current_task = {"id" : task_id, "name" : task_name, "status" : status}
#         self.tasks.append(current_task)
#         print(self.tasks)

#     def view_all_tasks(self):
#         print(self.tasks)

# todo = todolist()
# todo.add_task(task_id = 1, task_name = "Website", status = "completed")
# todo.add_task(task_id = 2, task_name = "Python",  status = "completed")
# todo.view_all_tasks() 

#sum - 2
class orders:
    def __init__(self):
        self.sales = []
    
    def add_new_items(self, id, product_name, quantity, price):
        new_items = {"id": id, "product": product_name, "qt": quantity, "cost": price}
        self.sales.append(new_items)
        print("Total:", quantity * price)
    
    def remove_items(self, id):
        for item in self.sales:
            if item["id"] == id:
                self.sales.remove(item)
                print("Item is removed successfully.")
                break
        else:
            print("Item not found.")

    def update_items(self, product_name, quantity):
        for item in self.sales:
            if item["product"] == product_name:
                item["qt"] += quantity
                print("Item is Updated")
                break
        else:
            print("Product not found.")


cust1 = orders()
cust1.add_new_items(1, "Samosa", 2, 10)
cust1.add_new_items(2, "Tea", 1, 15)
cust1.remove_items(1)
cust1.remove_items(3)
cust1.update_items("Tea", 3)
cust1.update_items("Samosa", 5)
