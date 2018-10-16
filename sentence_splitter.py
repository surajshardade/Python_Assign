import re

def sentence_splitter(file_name):
    
    with open(file_name) as f1:
        data=f1.read()
        proper_data=re.sub('\n',"",data)
        print(1,proper_data)
        proper_data=re.sub(r'(?<!Mr)(?<!Dr)(?<!Mrs)\.\s([A-Z])',r'.\n\1',proper_data)
        proper_data=re.sub(r'\?\s','?\n',proper_data)
        proper_data=re.sub(r'!\s','!',proper_data)

        print(proper_data)


file_name=input("Enter file name: ")
sentence_splitter(file_name)
        

