#method-1
#given
a = int(input())

#condition
if a >= 1000:
    d = 0.10 * a  
    print(d,a - d)
elif a >= 500 and a<= 1000:
    d = 0.05 * a  
    print(d, a - d)
else:
    print(a)

#method-2
#given
a = int(input())

#condition
if a >= 1000:
    d = 1/10 * a  
    print(d,a - d)
elif a >= 500 and a<= 1000:
    d = 1/20 * a  
    print(d, a - d)
else:
    print(a)