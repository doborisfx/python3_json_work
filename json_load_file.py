#import io
'''
 uses Json file as data dictionary
 searches and shows the information found
 '''


from difflib import get_close_matches
import json

def print_lines(data_collectionm):
    #print(type(data_collectionm))
    if type(data_collectionm)==list:
        for lin in data_collectionm:
            print(" - " + lin)
    else:
        print(data_collectionm)

def get_jsonInfo(word,data):
    if word in data:
        return (data[word])
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(word.lower(),data.keys())) > 0:
        yn=input("Do you mean %s instead? Enter (y=Yesm n=No)?" % get_close_matches(word.lower(),data.keys())[0])
        if yn=='y':
            return (data[get_close_matches(word.lower(),data.keys())[0]])
        elif yn=='n':
            return ("word '%s' does'nt exist!. Please double check it." % word)
        else:
            return ("I did not understand your Entry.")
    else:
        return ("word '%s' not foud!. Please double check it." % word)

with open('data.json',"r") as json_data:
    source=json_data.read()
data = json.loads(source)
word = input("Enter word? ")
print_lines(get_jsonInfo(word,data))
