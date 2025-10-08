#given
amount = int(input())
member = bool(int(input()))

#condition
if member == 0:
    print("non-member",member)
if member == 1:
    print("member",member,"earned rewards:",amount // 10)