def generate_n_char(num,char):
    str1=""
    for i in range(num):
        str1+=char

    return str1

if __name__=="__main__" :
    num=int(input("Enter Num : "))
    char=input("Enter char : ")
    Res=generate_n_char(num,char)
    print("Result String : {}".format(Res))

