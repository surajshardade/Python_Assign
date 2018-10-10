len1=0;
def my_length(str1):
    global len1 
    str2=list(str1)
    for i in str2:
        len1+=1;
    return len1;

if __name__=="__main__":
    str1=input("Enter string : ")
    len1=my_length(str1);
    print(len1)
