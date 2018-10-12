def make_3sg_form(word):
    new=""
    if word.endswith("y"):
        new+=word[0:len(word)-1]+'ies'
    elif word.endswith(('o','ch','s','sh','x','z')):
        new+=word+'es'
    else:
        new+=word+'s'

    return new

if __name__=="__main__":
    word=input("Enter word : ")
    res=make_3sg_form(word)
    print("3SG-Form : {}".format(res))
