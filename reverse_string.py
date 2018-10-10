def reverse(str1):
    str1=list(str1)
    last=len(str1)-1
    for index in range(int(len(str1)/2)):
        str1[index],str1[last]=str1[last],str1[index]
        last-=1
    
    str2=""
    str2=str2.join(str1)
    return str2

if __name__=="__main__":
    str1=input("Enter String : ")
    str1=reverse(str1)
    print("Reverse String : {}".format(str1))
