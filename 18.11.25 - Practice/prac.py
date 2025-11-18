#sum-1
#Given a list of integers, count how many unique numbers are present.
new = []
given = [2, 3, 3, 5, 2, 8, 8]
count = 0

for num in given:
    if num not in new:
        new.append(num)
        count += 1

print(count)

#sum-2
#Given a sentence, find the longest word.
