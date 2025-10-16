#sum-1
def integers(l,n):
    for i in range (0, len(l), +1):
        if l[i] == n:
            return "Found"
    return "Not Found"

#Test Case
print(integers([35,45,55],65))
print(integers([15,21,33],21))

#sum - 2
def odd_or_even(num):
    add = 0
    for i in num:
        add += i
    if add % 2 ==0:
        print('Even')
    else:
        print('Odd')

#Test Case
odd_or_even([12,9])
odd_or_even([30,10])

#sum - 3
def finder(num, a, b):
    for i in range(0, len(num), +1):
        if a <= num[i] <= b:
            return num[i]
    return "Invalid Input"

# Test Case
finder([8, 1, 0, 19, 11, 28, 3, 5], 10, 20)