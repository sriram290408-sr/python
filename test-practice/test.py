#def calculator(operator, number1, number2):
    #Write your code here
operator = input()
number1 = int(input())
number2 = int(input())
match operator:
     case '+':
         print (number1 + number2)
     case '-':
         print (number1 - number2)
     case '*':
         print (number1 * number2)
     case '/':
         print (number1 / number2)
     case _:
         print("INVALID")