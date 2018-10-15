

def palindrome(str1):
    last=len(str1)-1
    for index in range(int(len(str1)/2)):
        if str1[index]!=str1[last-index]:
            return False
    return True
            


if __name__=="__main__":
    str1=input("Enter string : ")
    res=palindrome(str1)
    print("Palindrome : {}".format(res))
