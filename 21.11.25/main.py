#sum-1
# Rotate a list to the right by k positions
# Example:
# List = [1,2,3,4,5], k = 2 → [4,5,1,2,3]
list1 = [1,2,3,4,5]
k = 2
result = []
for i in range(len(list1)-k,len(list1),+1):
    result.append(list1[i])
for j in range(0,len(list1)-k,+1):
    result.append(list1[j])
print(result)

#sum-2
# (Strong number = sum of factorials of digits equals number)
# Example: 145 → 1! + 4! + 5! = 145
num = 145

a = (num // 10)
b = (num % 10)
c = (a // 10)
d = (a % 10)
total = 0

for digit in (b, d, c):
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    total += fact

print(total)