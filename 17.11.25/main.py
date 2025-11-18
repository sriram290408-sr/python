#sum-1
new = [8, 14, 11, 23, 6]
count = 0

for n in new:
    if n > 1:
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            count += 1

print(count)

#sum -2
n = 3
i = 0

while i < n:
    print(" " * i, end="")

    j = 0
    stars = 2*(n-i)-1
    while j < stars:
        print("*", end=" ")
        j += 1

    print()
    i += 1