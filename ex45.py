
"""A certain childrens game involves starting with a word in a particular 
category. Each participant in turn says a word, but that word must begin 
with the final letter of the previous word. Once a word has been given, it 
cannot be repeated. If an opponent cannot give a word in the category, they 
fall out of the game. For example, with "animals" as the category,
Child 1: dog 
Child 2: goldfish
Child 1: hippopotamus
Child 2: snake
...
Your task in this exercise is as follows: Take the following selection of 70 
English Pokemon names (extracted from Wikipedia's list of Pokemon) and 
generate the/a sequence with the highest possible number of Pokemon names 
where the subsequent name starts with the final letter of the preceding name. 
No Pokemon name is to be repeated.
audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"""


string="audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"


def last_letter(char,list2):
    for str in list2:
        if str.startswith(char):
            return str
    else : 
        return False


def poke_names(string):
    list1=string.split()
    all_series=[]
    long_series=[]

    for name in list1:
        series=[]
        list2=list1
        current_name=name
        series.append(current_name)
        list2.remove(current_name)
        ele=last_letter(current_name[-1],list2)
        while ele:
            current_name=ele
            series.append(current_name)
            list2.remove(current_name)
            ele=last_letter(current_name[-1],list2)
            
               
        if len(long_series)<len(series):
            long_series=series

    print(long_series)

poke_names(string)

