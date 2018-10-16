import random

list1=['orange','blue','white','black','green','yellow','violet','pink','red','gray','maroon']

def anagram(list1):
    ana=''
    index_random=random.randint(0,len(list1)-1)
    random_word=list1[index_random]
   # print(random_word)
   # for index in range(len(random_word))
    while len(ana)<len(random_word):
        ele=random.randint(0,len(random_word)-1)
        if random_word[ele] not in ana:
            for x in range(0,random_word.count(random_word[ele])):
                ana+=random_word[ele]
   #             print(ana)

    if ana!=random_word and len(ana)==len(random_word):
        print("anagram:{} ".format(ana))
    
    while True:
        string=input("Guess the word : ")
        if string==random_word:
            print("correct")
            break

anagram(list1)


