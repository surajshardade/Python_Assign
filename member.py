def member(num,list1):
    last1=len(list1)-1
    index=0
    #print(type(num))
    while(index<=last1):
        if num==list1[index]:
            return True
        else:
            index+=1
    return False

if __name__=="__main__":
    list1=[]
    num=eval(input("Enter number : "))
    list1=[eval(x) for x in (input("Enter list : ").split())]
    res=member(num,list1)
    print("member : {}".format(res))
