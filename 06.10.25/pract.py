#Question - 1
# Input
a = int(input("Enter the First Number"))
b = int(input("Enter the Second Number"))

#Loop
while a <= b:
    print(a)
    a = (a+1)

#Question - 2
#Input   
a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
n = int(input("Enter the Divisor: "))
count = 0

#Loop
while a <= b:
    if n <= 0:
        print("Invalid Input" )  

    elif a%n == 0:
        count = (count + 1)

    a = (a + 1)
print(count)

#Question - 3
method - 1
#Input
a = int(input("Enter the Walking Steps: "))
stars = 0
#Count the points
for i in range(1, a+ 1):
    if i % 1000 == 0:
        stars += 5
    if i % 5000 == 0:
        stars +=20
print("Total points earned: ", stars)

#method - 2
#Input
a = int(input("Enter the Walking Steps: "))
stars = 5
bonus = 20
#condition
if a >= 1000 and a <= 1999:
    print(stars)
elif a >= 2000 and a <= 2999:
    print(stars + 5)
elif a >= 3000 and a <= 3999:
    print(stars + 10)
elif a >= 4000 and a <=4999:
    print(stars + 15)
elif a >= 5000:
    print(stars + bonus + 20)
