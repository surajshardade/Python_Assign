dict1={"merry":"god","christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}

def translate(string):
    words=string.split(" ")
    trans=''
    for ele in words:
        trans+=dict1.get(ele)+" "

    print(trans)

if __name__=="__main__":
    string=input("Enter String : ")
    translate(string)


