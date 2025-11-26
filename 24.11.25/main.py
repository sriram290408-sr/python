#sum-1
names = ["Arun", "Bala", "Cathy", "David", "Elena", "Farhan", 
"Gita","Hari"]
bd = ["05/01", "19/07", "23/03", "30/06", "11/11", "02/05",
"15/06", "01/12"]

result = []

for i in range(len(bd)):
    date = bd[i]          
    m1 = date[3]         
    m2 = date[4]          
    
    month = int(m1 + m2)   
    
    if month >= 1 and month <= 6:
        result.append(names[i])

print(result)

#sum-2 
def count_common_words(s1, s2):
    li1 = []
    li2 = []
    count = 0
    new = ""
    new1 = ""

    for i in range(len(s1)):
        new += s1[i]
        if s1[i] == " ":
            li1.append(new.strip())
            new = ""
    li1.append(new.strip())

    for j in range(len(s2)):
        new1 += s2[j]
        if s2[j] == " ":
            li2.append(new1.strip())
            new1 = ""
    li2.append(new1.strip())

    for k in range(len(li1)):
        if li1[k] in li2:
            count += 1

    print(count)


count_common_words("hello world python code", "python is fun world")
count_common_words("one two three", "four five six")

#sum-3
def print_pattern(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "* " * i)

    for i in range(n-1, 0, -1):
        print(" "*(n-i) + "* " * i)


print_pattern(3)

#sum-4
sent = "fastapi"
result = sent[0] + sent[1]
for i in range(len(sent)-3,1,-1):
    result += sent[i]
result += sent[-2] + sent[-1]
print(result)