from functools import reduce
max1=""
def find_longest_word(list1):
    max2= reduce((lambda x,y: x if len(x)>len(y) else y),list1)
    if len(max2)>len(max1):
        max_length=len(max2)

    return max_length

list1=eval(input("Enter list of word : "))
len1=find_longest_word(list1)
print("Max word lenth : {}".format(len1))
