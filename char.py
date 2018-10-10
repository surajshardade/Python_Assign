vow=['a','e','i','o','u','A','E','I','O','U']

def vowel(str1):
    for i in vow:
        if str1==i :
            return True

    return False

if __name__=="__main__":
    str1=input("Enter char : ")
    if (str1>='a' and str1<='z') or (str1>='A' and str1<='Z'):
        str1=vowel(str1)
        print("Vowel : {}".format(str1))
    else :
        print("Not a char :")
    
