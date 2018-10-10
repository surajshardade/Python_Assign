def translate(text):
    newtext=""          #create an empty string(this is the version of the text that we will modify)
    for letter in text:         #for loop to do this to each letter
        if letter not in 'aeiou':   #if letter is a consonant
            newtext=newtext+letter+'o'+letter  #add it to the empty string twice with an o in between
        else:       #if its a vowel
            newtext=newtext+letter      #add it to the string
    return newtext      #return new version of text

#ACTUALCODE
text=input('write the text ')       #assign text variable
print('I will translate it to robbers language')
print (translate(text))
print("you're welcome")
