def word_to_intlen(list1):
    list2=[int(len(ele)) for ele in list1]
    print("list of lengths : {}".format(list2))

if __name__=="__main__":
    list1=eval(input("Enter list : "))
    word_to_intlen(list1)
