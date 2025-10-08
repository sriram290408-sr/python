# #problem-1
# #input
# A = int(input("Give a number"))

# #Condition
# if A%4 == 0:
#     print("Y")
# elif A < 0:
#     print("Invalid input")
# else:
#     print("N")

# #problem-2
# #input
# a = int(input("Enter the first value: "))
# b = int(input("Enter the second value: "))
# c = 0

# #loop
# while a <= b:
#     if a % 2 == 0:
#         c += a
#     a += 1

# print("Sum of even numbers:", c)

#problem-3
#input
p = int(input("Enter the weight of product"))

#condition
if p <= 5:
    cost = "10$"
elif p > 5 and p < 20:
    cost = "20$"
elif p > 20:
    cost = "50$"
else:
    cost = 50

shipping_cost = float(cost * 1.05)

print(cost,shipping_cost)