
def sum1(list1):
    sum2=0
    for value in list1:
        sum2+=int(value)

    return sum2

def mul(list1):
    prod=1
    for value in list1:
        prod*=value

    return prod

if __name__=="__main__" :
    list1=[]
    list1=eval(input("Enter list : "))
    sum2=sum1(list1)
    prod=mul(list1)

    print("Sum = {} , mul = {}".format(sum2,prod))
