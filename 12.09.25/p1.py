#Problem-1

#given 
a = int(input("Enter mark 1: "))
b = int(input("Enter mark 2: "))
c = int(input("Enter mark 3: "))

#condition
if a & b & c > 40 and a & b & c <=100:
    print("Promote")
else:
    print("Not Promote")


#Problem-2

#given
a = str(input())

#condition
if a == "rainy":
    print("Bring Umberlla")

elif a == "sunny":
    print("No Umberlla Needed")

else:
    print("INVALID")

#Problem-3

#given
a = str(input())

#condition
if a == "saturday":
    print("Holiday")

elif a == "sunday":
    print("Holiday")

else:
    print("Working day")