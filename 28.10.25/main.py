#Sum - 1
def extract_vowel(word):
    new_list = []
    for i in word:
        if i in ["a","e", "i", "o", "u"]:
            new_list.append(i)
    print(new_list)

extract_vowel("education")

#Sum - 2
def integers(num):
    even = 0
    odd = 0
    for i in num:
        if i%2 == 0:
            even += 1
        elif i%2 != 0:
            odd += 1
        else:
            print("Invalid Input")
    print("even:", even ,"odd:", odd)
    
integers([1,2,3,4,5,6,7,8,9,10])

#Sum - 3
def maximum_vowels(words):
    vowels = ["a", "e", "i", "o", "u"]
    max_vowel_word = ""
    max_count = 0

    for i in words:
        count = 0
        for j in i.lower():
            if j in vowels:
                count += 1
        if count > max_count:
            max_count = count
            max_vowel_word = i

    print(max_vowel_word)

maximum_vowels(["cat", "panda", "umbrella", "sky"])

def lists(list1,list2):
    result = []
    for i in range(len(list1)):
        # result = list1 + list2
        result.append(list1[i])
        result.append(list2[i])
    print(result)

lists([10, 20, 30],[1, 2, 3])
