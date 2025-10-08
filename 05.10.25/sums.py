#Question - 1
age = int(input("Enter your age: "))

if age < 18:
    print(150)
elif age <= 60:
    print(250)
else:
    print(100)

#Question - 2
age = int(input("Enter your age: "))

if age < 12:
    ticket = 50
elif age <= 59:
    ticket = 120
else:
    ticket = 80

if age % 2 == 0:  # Even age → ₹5 discount
    ticket -= 5

print(ticket)

#Question - 3
mangoes = int(input("Enter number of mangoes: "))

full_baskets = mangoes // 5
left_over = mangoes % 5

print("Full Basket is", full_baskets)
print("Left Over mangoes is", left_over)

#Question - 4

#Question - 5
salary = float(input("Enter your salary: "))
sales = int(input("Enter your sales: "))

if sales >= 100:
    bonus = salary * 0.10
elif sales >= 50:
    bonus = salary * 0.05
else:
    bonus = 0

total_salary = salary + bonus

print("Bonus =", int(bonus))
print("Total Salary =", int(total_salary))

#Question - 6
sales = float(input("Enter weekly sales: "))

if sales <= 5000:
    commission = sales * 0.05
elif sales <= 10000:
    commission = sales * 0.10
else:
    commission = sales * 0.15

print(int(commission))

#Question - 7
price = float(input("Enter item price: "))

if price > 100:
    discount = price * 0.10
elif price >= 50:
    discount = price * 0.05
else:
    discount = 0

final_price = price - discount
print(int(final_price))

#Question - 8
file = input("Enter file extension: ")

if file == ".csv":
    print("This is an Excel File")
elif file == ".jpg":
    print("This is a JPEG File")
elif file == ".doc":
    print("This is a Word File")
elif file == ".pdf":
    print("This is a PDF File")
elif file == ".py":
    print("This is a Python File")
else:
    print("Unknown File Type")

#Question - 9
km = int(input("Enter distance in km: "))

if km <= 10:
    fare = km * 15
elif km <= 30:
    fare = 10 * 15 + (km - 10) * 12
else:
    fare = 10 * 15 + 20 * 12 + (km - 30) * 10

print(fare)

print(factorial(5))