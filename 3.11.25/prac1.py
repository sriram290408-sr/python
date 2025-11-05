mark1 = [45, 60, 70, 55, 80]
mark2 = [50, 58, 75, 65, 78]

count = 0

for i in range(0,len(mark1),+1):
    if mark2[i] > mark1[i]:
        count += 1

print(count)

list1 = [11, 22, 33, 44, 55]
search = 33
count = -1
for i in list1:
    count += 1
    if i == search:
        print(count)

s = "Learning Python is Fine"
a = ""
for i in s:
    if i == " ":
        i= "-"
    a += i
print(a)

words = "Learning Python is Fine"
result = ""
for i in words:
    if i == " ":
        result += "-"
    else:
        result += i
print(result)