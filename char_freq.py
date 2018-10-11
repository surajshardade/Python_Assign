def char_freq(string):
    freq={}
    for char in string:
        if char in freq:
            freq[char]+=1
        else :
            freq[char]=1


    print(freq)

if __name__=="__main__":
    string=input("Enter String : ")
    char_freq(string)

