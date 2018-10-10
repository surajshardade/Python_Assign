def max(num1,num2):
    if num1>num2:
        return num1
    else :
        return num2


def max_three(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num3:
        return num2
    else:
        return num3


if __name__=="__main__" :
    n,n1,n2=[eval(x) for x in input("Enter three number:").split()]
    res=max(n,n1)
    res=max(n2,res)
    print("Max = {}".format(res))
    res=max_three(n,n1,n2)
    print("Max = {}".format(res))
