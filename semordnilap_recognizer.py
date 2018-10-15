def semordnilap_recognizer(file_name):
    list1=[]
    with open(file_name,"r") as f1:
        data=f1.read().split()
        for index in range(len(data)):
            for index2 in range(len(data)):
                if index!=index2:
                    data1=data[index2]
                    if data[index]==data1[::-1]:
                        if data[index] not in list1:
                            list1.append(data[index])
    print(list1)

file_name=input("Enter ffile name : ")
semordnilap_recognizer(file_name)

