def palindrome_recognizer(string):
    s=''
    for char in string:
        if (char>='a' and char<='z' ) or (char>='A' and char<='Z'):
            if (char>='A' and char<='Z'):
                s+=chr(ord(char) ^ 32)
                
            else :
                s+=char
    
    last=len(s)-1
    for index in range(int(len(string)/2)):
        if s[index]!=s[last-index]:
            return False
        return True


if __name__=="__main__":
    string=input("Enter string : ")
    Res=palindrome_recognizer(string)  
    print("Palindrome after ignoring spaces and punctuations : {}".format(Res))

