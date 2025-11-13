#sum - 1
def count_instance(sent,search):
    new = list(search)
    count = 0
    for word in range(len(sent)):
        if sent[word] in new:
            if sent[word +1] in new:
                count += 1
        
    print(count)

count_instance("this is incredible", "is")

#sum - 2
def two_matrix(matrix1,matrix2):
    result = [] 
    if len(matrix1) != len(matrix2):
        print("Invalid") 
    else:
        for i in range(len(matrix1)):
            new = []
            for j in range(len(matrix1[i])):
                    new.append(matrix1[i][j] + matrix2[i][j])
            result.append(new)
        print(result)

two_matrix(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
