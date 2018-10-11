def pangram(string):
    string=string.lower()
    set1=set(string)
    count=0
    for ele in set1:
        if ele>='a' and ele<='z':
            count+=1
    if count==26:
        return True
    else:
        return False

if __name__=="__main__":
    string=input("Enter string : ")
    Res=pangram(string)
    print("pangram : {}".format(Res))
