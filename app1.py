import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches 
import sys

data = json.load(open("data.json"))

def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0]) 
        if yn == "Y" or yn =="y":
            return data[get_close_matches(word, data.keys())[0]]
        else: 
            if_quit = input("Enter new word or enter Q to quit: ")
            if if_quit == "Q" or if_quit == 'q':
                return sys.exit()
            else:
                return search(if_quit)
    else:
        return "The word doesn't exist."

word = input("Enter word: ")
output = search(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
