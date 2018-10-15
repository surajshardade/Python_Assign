"""A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an author, or in a single text. Define a function that given the file name of a text will return all its hapaxes. Make sure your program ignores capitalization."""



def hapax(file_name):
    list1=[]
    with open(file_name) as f1:
        words=f1.read().split()
        for word in words:
            if words.count(word)==1:
                list1.append(word)

    return list1


file_name=input("Enter file name: ")
list1=hapax(file_name)
print(list1)





