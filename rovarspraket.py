def rovarspraket(str1):
    list_char=list(str1)
    list1=[]
    s=""
    for i in list_char:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i== 'u' or i==" "):
            list1.append(i)
        else:
            list1.append(i)
            list1.append('o')
            list1.append(i)
            #print("list:",list1)

    #print("list:",list1)
    str1=s.join(list1)
    return str1

if __name__=="__main__" :
    str1=input("Enter string: ")
    str1=rovarspraket(str1)
    print(str1)

