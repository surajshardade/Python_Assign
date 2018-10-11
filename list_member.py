def list_member(list1,list2):
    for ele in list1:
        for ele1 in list2:
            if ele==ele1:
                return True
    return False

if __name__=="__main__":
    list1=eval(input("Enter list1 : "))
    list2=eval(input("Enter list1 : "))
    res=list_member(list1,list2)
    print("member : {}".format(res))
