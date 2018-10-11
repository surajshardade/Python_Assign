def max_in_list(list1):
    max1=0;
    for ele in list1:
        if ele>max1:
            max1=ele
    return max1

if __name__=="__main__":
    list1=eval(input("Enter List : "))
    Res=max_in_list(list1)
    print("max in list : {}".format(Res))
