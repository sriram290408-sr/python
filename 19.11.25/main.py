given = [3,5,7,2,4]
#1. Find the LCM amongst a list of Positive Integers.
for i in range(len(given)):
    for b in range(1,len(given)+1, +1):
         a = given[0]
         while b != 0:
              a, b = (b, (a % b))
    print(a)
#2. Find the factorials of each of the integers given in an List.
result = []
for num in given:
        fact = 1
        for i in range(1,num+1):
              fact*=i
        result.append(fact)
print(result)
#3. Perform search and replace without using library functions. 
# Given a String "This is programming" find_str = "is" and replace "are" result should be "Thare are programming"

sent = "This is programming"
check = ["i", "s"]
result = ""
new = list(sent)

for word in range(0, len(new), +1):
    if new[word] in check:
        if word + 1 < len(new) and new[word+1] in check:
            result += "are"
    else:
        result += new[word]

print(result)