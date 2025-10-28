# ****

# string
# boolean
# int
# float
# list
# tuple
#Tuple
# set
# Dictionary
# ****

pi: float = 3.14
sum_of_angles:int = 180
student_status: bool = True

marks:List[int] = [108, 95, 84, 79, 99]
#Basic Data Type => List
#List of String

cities: List[string] = ["Delhi", "Mumbai", "Chennai"]

def print_status(i: bool):
    print("status is {i}")
    return

print_status("True")

# ****

# Write a function to find area of rectangle
# inputs ->
# length -> int ,
# breadth -> int

# output -> area -> int

# ****

def find_area(length: int, breadth: int) -> int:
    return (length * breadth)


def finding_sum_of_elements(List(int)) -> int:
    #Start
    sum: int = 0
    for i in numbers:
        sum += 1
    return sum
    #Stop

print(finding_sum_of_elements([108, 95, 84, 79, 99]))


status: Tuple[str, str, str, bool] = ("CREATION", "REVIEW", "SCRUTION", "APPROVED")
