def word_length(list1,num):
    filtered_list=[word for word in list1 if len(word)>num]
    print(filtered_list)

if __name__=="__main__":
    list1=eval(input("Enter list : "))
    num=int(input("Enter num : "))
    word_length(list1,num)
