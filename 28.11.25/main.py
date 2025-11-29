ps = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
new = []
new1 = []
result = ""
for sep in ps:
    for i in range(len(sep)):
        if i % 2 != 0:
            new.append(sep[i])
            
for check in range(len(new)):
    max_check = max(new)
    new1.append(max_check)
    new.remove(max_check)

for sep in ps:
    for i in range(len(sep)):
        if i % 2 != 0:
            if sep[i] == new1[0] or sep[i] == new1[1]:
                result += sep[i-1] + " "

print(result)