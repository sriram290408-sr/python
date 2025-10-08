#given
m = int(input())

#condition
if m <= 100 and m >= 80:
    print("A")
else:
    if m <= 79 and m >= 60:
        print("B")
    else:
        if m <= 59 and m >= 50:
            print("C")
        else:
            if m <= 49 and m >= 40:
                print("D")
            else:
                print("Fail")