"""Your task in this exercise is as follows:

    Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
    Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.

Examples:

   []        OK   ][        NOT OK
   [][]      OK   ][][      NOT OK
   [[][]]    OK   []][[]    NOT OK

"""

import re

def check(string):
    result=string
    while len(re.findall(r'\[\]',string))>0:
        string=re.sub('\[\]','',string)

    if len(string)>0:
        print("{} : Not Ok".format(result))
    else :
        print("{} : Ok ".format(result))
    
    

string=input("Enter string of [,] :")
check(string)
