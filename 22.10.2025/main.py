# #Question - 1
# #(i)
# #Input
# Sentence = str(input("Enter the Sentence: "))

# #Split
# word = Sentence.split('-')

# print(word)

# #(ii)
# sentence = "Emma-is-a-data-scientist"

# word = ""
# for alpha in sentence:
#     if alpha != '-':           
#         word += alpha
#     else:
#         print(word)           
#         word = ""    

# print(word)              

# #Question - 2
# #(i)
# sentence = str(input("Enter the Sentence: "))

# word = sentence[::-1]
# print(word)

# #Question - 3
# sentence = str(input("Enter the Sentence:"))
# count = 0

# for i in range(0, len(sentence), +1):
#     if sentence[i] not in ['a', 'e', 'i', 'o', 'u', " "]:
#         count += 1

# print(count)

#Question - 4
# sentence = str(input("Enter the Sentence: "))
# word = " "

# for i in sentence:
#     if i != " ":
#         word += i
# print(word) 

# # Question - 5
# password = input("Enter the Password: ")
# special = "!@#$%^&*"

# for i in password:
#     if i in special:
#         print("Password is strong")
#         break
# else:
#     print("Password is not strong")
