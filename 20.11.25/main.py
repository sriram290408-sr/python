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