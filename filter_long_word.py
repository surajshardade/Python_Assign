def filter_long_word(list1,num):
    filter_list=[]
    for word in list1:
        if len(word)>num:
            filter_list.append(word)
     
    return filter_list

if __name__=="__main__":
    word_of_list=eval(input("Enter list of words : "))
    num=int(input("Enter num : "))
    filtered_list=filter_long_word(word_of_list,num)
    print("list having word larger than length {} : {}".format(num,filtered_list))
