n = 3
result = ""
start = 1
while start <= n:
    result = result + str(start) + " "
    print(" " * (n - start) + result)
    start += 1