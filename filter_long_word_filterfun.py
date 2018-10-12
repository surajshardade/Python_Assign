'''Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.'''



def filter_long_word(list1,num):
    return list(filter(lambda x: len(x)>num,list1))


list1=eval(input("Enter list of words : "))
num=int(input("Enter num for which u wanted to filter list : "))
res_list=filter_long_word(list1,num)
print("Filtered list : {}".format(res_list))
