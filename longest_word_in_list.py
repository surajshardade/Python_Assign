def find_longest_word(list1):
    long_word=""
    max_len=0
    for word in list1:
        count=0
        for ele in word:
            count+=1
            if count>max_len:
                max_len=count
                long_word=word
    return max_len

if __name__=="__main__":
    list_of_words=eval(input("Enter list of word : "))
    max_len=find_longest_word(list_of_words)
    print("max word length : {}".format(max_len))

