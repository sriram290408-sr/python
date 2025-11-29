#sum-1
def count_unique(sent):
    new = []
    for word in sent:
        if word not in new:
            new.append(word)
    for letter in new:
        count = 0
        for ch in sent:
            if ch == letter:
                count += 1
        print(letter, "->", count)

count_unique("banana")
count_unique("apple")

#sum-2
def count_v_c(sent):
    countv = 0
    countc = 0
    vowel = "aeiou"
    num = "1234567890"
    if sent in num:
        print("Invalid input")
    else:
        for word in sent:
            if word in vowel:
                countv += 1
            else:
                countc += 1
        print("Vowel ->", countv)
        print("Consonant ->", countc)
        
count_v_c("education")
count_v_c("sky")

#sum-3
def first_occur(sent):
    result = ""
    for word in sent:
        if word not in result:
            result += word
    print(result)
    
first_occur("programming")
first_occur("mississipi")

#sum-4
def rev_word(sent):
    result = ""
    for i in range(len(sent)-1, -1, -1):
        result += sent[i]
    print(result)

rev_word("python is super")