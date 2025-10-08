# #given
# cons = input()
# unit = int(input())

# #condition
# if cons == "residential":
#     if unit > 0 and unit <= 100:
#         print(cons,(3*unit))
#     elif unit > 101 and unit <= 200:
#         print(cons,(5*unit))
#     elif unit > 200:
#         print(cons,(7*unit))
#     else:
#         print("Invalid unit")
# elif cons == "commercial":
#     if unit > 0 and unit <= 100:
#         print(cons,(5*unit))
#     elif unit > 100 and unit <= 200:
#         print(cons,(7*unit))
#     elif unit > 200:
#         print(cons,(10*unit))
#     else: 
#         print("Invalid unit")

# #given 
# distance = float(input("Enter the distance:"))

# #condition
# if distance <= 5:
#     fare = (distance*10)
# elif distance >= 6 and distance <= 15:
#     fare = (distance*8)
# elif distance > 15:
#     fare = (distance*6)
# else:
#     fare = Invalid

# if fare < 50:
#     fare = 50

# print("Final fare: ₹", fare)

# #given
# a = int(input())
# b = int(input())
# c = int(input())

# #condition
# if  a+b < c or b+c < a or c+a < b:
#     if a == b == c:
#         print("Equilateral Triangle - All sides are equal")
#     elif a == b != c or b == c != a or c == a != b:
#         print("Isosceles Triangle - Two sides are equal")
#     elif a != b != c:
#         print("Scalene Triangle - No sides are equal")
# else:
#     print("Not a valid triangle")

# c = input("Enter the stream: ")

# match-case condition
# match c:
#     case "science":
#         print(input("Enter the sub-choice Medical or Engineering: "))
#     case "commerce":
#         print(input("Enter the sub-choice CA or B.com: "))
#     case "arts":
#         print(input("Enter the sub-choice History or Literature: "))
#     case _:
#         print("No choice")

#given
# a = int(input("Enter a number: "))

#condition
# if a % 3 == 0 and a % 5 == 0:
#     print("FizzBuzz")
# elif a % 3 == 0:
#     print("Fizz")
# elif a % 5 == 0:
#     print("Buzz")
# else:
#     print("not divisible by 3 and 5")

#given
# t = int(input())

#condition
# if t >= 9 and t <= 12:
#     print("Morning Show")
# elif t > 12 and t <= 16:
#     print("Matinee Show")
# elif t > 16 and t <= 20:
#     print("Evening Show")
# elif t > 20 and t <= 24:
#     print("Night Show")
# else:
#     print("Invalid time-format")

# # given
# d = float(input("Enter the distance in km"))
# choice = input("Enter the Conversion")

# # Condition - (Conversion)
# match choice:
#     case "meter":
#         print(d*1000,"m")
#     case "centimeter":  
#         print(d*100000,"cm")
#     case "millimeter":
#         print(d*1000000,"mm")
#     case "miles":
#         print(d*0.621371,"miles")
#     case _ :
#         print("Invalid Conversion")

# #given
# pm = (input())

# #condition
# if pm == "UPI":
#     print("You selected UPI payment")
# elif pm == "Card":
#     print( "You selected Debit/Credit Card payment")
# elif pm == "Net Banking":
#     print("You selected Net Banking")
# elif pm == "COD":
#     print("You selected Cash on Delivery")
# else:
#     print("Invalid Payment Mode")