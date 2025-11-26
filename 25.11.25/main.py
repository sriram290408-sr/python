#sum-1
num = [1,2,3]
count = 0
for i in num:
    if i%2 == 0:
        count += 1
for j in range(0,len(num),+1):
    if j != len(num)-1:
        new = []
        new.append(num[j])
        new.append(num[j+1])
        new_sum = sum(new)
        if new_sum%2 == 0:
            count += 1
num_sum = sum(num)
if num_sum%2 == 0:
    count +=1
print(count)

#sum-2
def count_el(num):
    count = 0
    product_num1 = 1
    for i in num:
        count += 1
        sum_num1 = sum(num)
        product_num1 *= i
    if sum_num1 == product_num1:
        count += 1
    for j in range(0,len(num),+1):
        if j != len(num)-1:
            sum_num = num[j] + num[j+1]
            product_num = num[j]*num[j+1]
            if sum_num == product_num:
                count += 1
    print(count)
            
count_el([1,2,3])
count_el([1,2,4])

#sum-3
def number(num):
    result = []
    for i in num:
        a = ((i//10)//10)//10
        b = (((i-(a*1000))//10)//10)
        c = ((i-(a*1000 + b*100))//10)
        d = i%10
        if a>b:
            if b>c:
                if c<d:
                    result.append(i)
    print(result)
    
number([5326, 98712, 1234, 5432, 5263, 76109])

#sum-4
num = [10, 101, 2005, 340, 89]
result = []
for i in num:
    count = 0
    if len(str(i)) == 2:
        a = i // 10
        b = i % 10
        if a == 0:
            count += 1
        if b == 0:
            count += 1
    elif len(str(i)) == 3:
        a = i // 100
        b = (i // 10) % 10
        c = i % 10
        if a == 0:
            count += 1
        if b == 0:
            count += 1
        if c == 0:
            count += 1
    elif len(str(i)) == 4:
        a = i // 1000
        b = (i // 100) % 10
        c = (i // 10) % 10
        d = i % 10
        if a == 0:
            count += 1
        if b == 0:
            count += 1
        if c == 0:
            count += 1
        if d == 0:
            count += 1
    if count == 1:
        result.append(i)
print(result)

#sum-5
sent = ["apple", "cat", "moon", "dog"]
result = []
new1 = []
for i in sent:
    new = ""
    for j in i:
        if j not in new:
            new += j
    new1.append(new)
    
for k in range(len(sent)):
    if sent[k] in new1:
        result.append(new1[k])
print(result)