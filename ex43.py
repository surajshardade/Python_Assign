"""An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once; e.g., orchestra = carthorse. Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that finds the sets of words that share the same characters that contain the most words in them."""



def anagram(file_name):
    with open(file_name) as f1:
        word_list=f1.read().split()
    dict={}
    for word in word_list:
        key=''.join(sorted(word))
        if key in dict:
            dict[key].append(word)
        else:
            dict[key]=[word]
    print(dict)
    cnt=0
    for len1 in dict.values():
        if len(len1)>cnt:
            max_list=len1
            cnt=len(len1)
        
    return max_list

file_name=input("Enter name of file : ")
print("Biggest set Anagram is ", anagram(file_name))

