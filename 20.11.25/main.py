#sum-1
nums = [11,22,33,44,55]
result = []

for num in nums:
    new1 = 0
    new2 = 0
    new1 += (num//10)
    new2 += (num%10)
    total = (new1 + new2)
    if total > 5:
        result.append(total)
print(result)

#sum-2
nums = [5, 4, 0, 9, 8, 7, 0, 3, 2]
a = 0
b = 0
result = []

for i in range(len(nums)):
    if nums[i] == 0:
        a = i
        break

for j in range(a + 1, len(nums)):
    if nums[j] == 0:
        b = j
        break

for k in range(a+1, b-1 + 1):
    result.append(k)

print(result)

#sum-3
given = "Anna went to America and met Adam"
given2 = given.lower()
count = 0
new1 = [given2[0]]
new2 = []

for i in range(1,len(given2),+1):
    if given2[i] == " ":
        new1.append(given2[i+1])
        new2.append(given2[i-1])
        
for j in range(0,len(new1)-1,+1):
    if new1[j] == new2[j]:
        count += 1
        
print(count)

#sum-4
# Print the following pattern using loops:
# 1
# 12
# 123
# 1234
# 12345

n = 5
start = 1
result = ""
while start <= n:
    result += str(start)
    print(result)
    start += 1

#sum-4
n = 1
start = 5
result = ""
while start >= n:
    result += str(start)
    print(result)
    start -= 1

#sum-5
n = 1
result = ""
start = 5
while start >= n:
    result = result + str(start) + " "
    print(" " * (start - n) + result)
    start -= 1