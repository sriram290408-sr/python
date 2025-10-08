#Problem-1
#Input
n = int(input())
start = 1

#loop
while start <= n:
    print(start * start * start)
    start = (start + 1)

#Input
x = int(input("Enter the number: "))
y = int(input("How many numbers: "))

# set the end point
end = x + y

#loop
while x <= end:
    print(x)
    x = (x + 1)

#Problem-3
#Input
N = int(input("User value"))
x = 1

#loop
while x <= N:
    print((x*x) + 1)
    x = (x + 1)

#Problem-4
#Input
num = int(input("Enter a number: "))
total = 0

#loop
while num > 0:
    digit = num % 10       
    total += digit       
    num = num // 10        

print("Sum of digits:", total)