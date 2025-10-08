#given
x = int(input())
y = int(input())

#condition
if x == 0 and y == 0:
    print("Origin")
elif x >= 0 and y >= 0:
    print("Quadrant - I")
elif x <= 0 and y >= 0:
    print("Quadrant - II")
elif x <= 0 and y <= 0:
    print("Quadrant - III")
elif x >= 0 and y <= 0:
    print("Quadrant - IV")
else:
    print("invalid")