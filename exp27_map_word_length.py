def map_using_for(list1):
    list2=[]
    for word in list1:
        len1=0
        for ele in word:
            len1+=1;
        list2.append(len1)

    print("mapping using for loop: {}".format(list2))


def map_using_mapfun(list1):
    print("mapping using map() :{} ".format(list(map(lambda x:len(x),list1))))

def map_using_list_comprehention(list1):
    print("mapping using list compreshention : {}".format([len(word) for word in list1]))





list1=eval(input("Enter List : "))
map_using_for(list1)
map_using_mapfun(list1)
map_using_list_comprehention(list1)
