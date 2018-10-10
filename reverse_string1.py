def reverse(str1):
    list1=[]
    last=len(str1)
    for i in range(-1,-last-1,-1):
        list1.append(str1[i])

    str1=''
    str1=str1.join(list1)
    return str1


if __name__=="__main__":
    str1=input("Enter String : ")
    res=reverse(str1)
    print("Reverse String : {}".format(res))
