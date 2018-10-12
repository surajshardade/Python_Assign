def making_ing_form(word):
    new=''
    if word in ['be','see','flee','knee']:
        new+=word+'ing'
    elif word.endswith('ie'):
        new+=word[0:len(word)-2]+'y'+'ing'
    elif word.endswith('e'):
        new+=word[0:len(word)-1]+'ing'
    elif ( (word[0] not in "aeiou") and (word[1] in "aeiou") and (word[2] not in "aeiou" )):
        new+=word+word[2]+'ing'
    else :
        new+=word+'ing'

    return new

if __name__=="__main__":
    word=input("Enter verb in infinitive form : ")
    print("Present Participle : ",making_ing_form(word))
