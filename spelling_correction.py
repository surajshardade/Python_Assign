def correct(string):
    s=''
    for index in range(len(string)):
        if string[index]!=' ':
            s+=string[index]
            cnt=0
        else:
            if cnt==0:
                cnt=1
                s+=string[index]
            else :
                pass
        if string[index]=='.':
            if string[index+1]!=' ':
                s+=' '
            else:
                s+=string[index]


    return s

if __name__=="__main__":
    string=input("Enter String : ")
    Res_string=correct(string)
    print("Result String : {}".format(Res_string))
