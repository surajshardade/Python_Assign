def map1(fun,list1):
    res=[]
    for ele in list1:
        res.append(fun(ele))

    return res

def filter1(fun,sequence):
    res=[]
    for ele in sequence:
            if fun(ele):
                res.append(ele)
    if isinstance(sequence,list):
        res=list(res)
    if isinstance(sequence,set):
        res=set(res)
    if isinstance(sequence,tuple):
        res=tuple(res)


    return res


def reduce1(fun,seq):
    res=0
    for ele in seq:
        res=fun(res,ele)
    return res
        


def add(x):
    return x+x
print(map1(add,[1,2,3,4]))
print(filter1(lambda x: x>2,{1,2,3,4}))
print(reduce1(lambda x,y:x+y,[1,2,3,4]))
