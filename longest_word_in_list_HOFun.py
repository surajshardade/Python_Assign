'''Write a function find_longest_word() that takes a list of words and returns the length of the longest one. Use only higher order functions.'''


from functools import reduce
max1=""
def find_longest_word(list1):
    max2= reduce((lambda x,y: x if len(x)>len(y) else y),list1)
    if len(max2)>len(max1):
        max_length=len(max2)

    return max_length




def using_map(list1):
    print("max length : {}".format(max(map(len,list1))))


def using_list_comprehention(list1):
    print(max([len(x) for x in list1]))

list1=eval(input("Enter list of word : "))
len1=find_longest_word(list1)
using_map(list1)
print("Max word lenth : {}".format(len1))
using_list_comprehention(list1)

