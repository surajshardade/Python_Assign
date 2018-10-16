"""In a game of Lingo, there is a hidden word, five characters long. The object of the game is to find this word by guessing, and in return receive two kinds of clues: 1) the characters that are fully correct, with respect to identity as well as to position, and 2) the characters that are indeed present in the word, but which are placed in the wrong position. Write a program with which one can play Lingo. Use square brackets to mark characters correct in the sense of 1), and ordinary parentheses to mark characters correct in the sense of 2). Assuming, for example, that the program conceals the word "tiger", you should be able to interact with it in the following way:

>>> import lingo
snake
Clue: snak(e)
fiest
Clue: f[i](e)s(t)
times
Clue: [t][i]m[e]s
tiger
Clue: [t][i][g][e][r]

"""
import random
list1=['suraj','white','black','green']


def lingo(words):
    root_word=words[random.randrange(0,len(words))]
    print("root_word : {}".format(root_word))
    res=True
    while res:
        guess=input("Guess word: ")[:5]
        clue=''
        if len(root_word)==5 and len(guess)==5:
            for index1 in range(len(guess)):

                # for index in range(len(root_word)):
                if guess[index1] in root_word:

                    if root_word[index1]==guess[index1]:\

                            clue+="["+guess[index1]+"]"
                            print(clue)
                        #cnt=1
                        #break
                    #elif root_word[index]==guess[index1]:
                    else:
                        clue+="("+guess[index1]+")"
                        print(2,clue)
                           # cnt1+=1
                        #break
                #if cnt==0:   
                else:

                    clue+=guess[index1]
                    print(3,clue)
                    #cnt=0
                        
        print("clue :{}".format(clue))
        if guess==root_word:
            res=False

lingo(list1)

