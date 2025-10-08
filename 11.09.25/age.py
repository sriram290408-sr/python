#given
a = int(input())

#condition
if a < 13:
    print("Child")
else:
    if a >= 13 and  a <= 19:
        print("Teen")
    else:
        if a >= 20 and a <= 59:
            print("Adult")
        else:
            if a >=60 and a <= 100:
                print("Senior")
            else:
                print("Died")