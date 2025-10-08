#Problem-1

#start & end
start = 0
end = 100

#loop
while start <= end:
    if start % 5 == 0:
        print(start)
    start = (start + 5)

#Problem-2

#start & end
start = 1
end = 10
user = int(input())

#loop
while start <= end:
    print(user * start)

    start = (start + 1)

#Problem-3

#start & end
start = 1
end = 5
sum = 0

#loop
while start <= end:
    sum = (sum + start)
    start = (start + 1)
print(sum)