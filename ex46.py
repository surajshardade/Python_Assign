"""An alternade is a word in which its letters, taken alternatively in a 
strict sequence, and used in the same order as the original word, make up at 
least two other words. All letters must be used, but the smaller words are not 
necessarily of the same length. For example, a word with seven letters where 
every second letter is used will produce a four-letter word and a three-letter 
word. Here are two examples:
  "board": makes "bad" and "or".
  "waists": makes "wit" and "ass".
Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, 
write a program that goes through each word in the list and tries to make two 
smaller words using every second letter. The smaller words must also be members 
of the list. Print the words to the screen in the above fashion."""




def alternade(file_name):
    with open(file_name) as file:
        words=file.read().split('\n')
    for word in words:
        w1=''
        w2=''
        for index in range(len(word)):
            if index in [0,2,4,6,8,10]:
                w1+=word[index]
            else:
                w2+=word[index]
        print("{} makes {} and {}".format(word,w1,w2))
file_name=input("Enter file name : ")
alternade(file_name)

