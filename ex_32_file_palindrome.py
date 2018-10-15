
def palindrome(string):
    list1=[]
    for string1 in string:
        string1=string1[0:len(string1)-1]

        if string1==string1[::-1]:
            list1.append(string1)
    return list1

with open("sample.txt","r+") as file_des:
        string=file_des.readlines()
        Res=palindrome(string)
        if Res:
            for ele in range(len(Res)):
                print(Res[ele])



