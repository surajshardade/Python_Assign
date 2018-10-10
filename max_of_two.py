def max(num1,num2):
    if num1>num2:
        return num1
    else :
        return num2


if __name__=="__main__" :
    n,n1=[int(x) for x in input("Enter two number:").split()]
    res=max(n,n1)
    print("Max = {}".format(res))
