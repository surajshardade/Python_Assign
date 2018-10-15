
def char_freq_tble(file_name):
    char_freq={}
    with open(file_name,"r") as f1:
        data=f1.read()
        for char in data:
            if char >='a' and char<= 'z':
                if char in char_freq:
                    char_freq[char]+=1
                else :
                    char_freq[char]=1
    print("Char_Freq Table : ")
    for char in sorted(char_freq.items(),key=lambda x:x[1]):
        print("     {}  |  {}".format(char[0] ,char_freq[char[0]]))
file_name=input("Enter file name: ")
char_freq_tble(file_name)





