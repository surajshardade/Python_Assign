from functools import reduce

def max_in_list(list1):
    return reduce(lambda x,y:x if x>y else y ,list1)




list1=eval(input("Enter list: "))
res=max_in_list(list1)
print("Max in list : {}".format(res))

