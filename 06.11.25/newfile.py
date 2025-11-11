#Sum - 1
def max_repeat(S):
  new = list(S)
  count_repeat = []
  for i in set(new):
    count = 0
    for j in new:
      if i == j:
        count += 1
    count_repeat.append(count)
  maximum = max(count_repeat)
  if maximum == 1:
    print(0)
  else:
    print(maximum)
  
max_repeat("success")
max_repeat("python")

# #Sum - 2
def modern_name(sentence):
  result = sentence[0]
  if len(sentence) == 0:
    print("Sum is not Exist")
  else:
    for i in range(0,len(sentence),+1):
      if sentence[i] == " ":
        result += sentence[i+1]
    print(result)
  
modern_name("united states america")
modern_name("binary indexed tree")

#Sum - 1
def max_repeat(S):
  new = list(S)
  count_repeat = []
  for i in set(new):
    count = 0
    for j in new:
      if i == j:
        count += 1
    count_repeat.append(count)
  
max_repeat("success")
max_repeat("python")