#sum-1
def diagonalDifference(arr):
    # Write your code here
    n = -1
    m = len(arr)
    count1 = 0
    count2 = 0
    for i in range(0,len(arr),+1):
        a = arr[i]
        n += 1
        m -= 1
        for j in range(0,len(a),+1):
            if j == n:
                count1 += a[j]
        for k in range(0,len(a),+1):
            if k == m:
                count2 += a[k]
    result = abs(count1-count2)
    return result
    
print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))