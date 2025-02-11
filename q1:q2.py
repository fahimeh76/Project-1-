from pathlib import Path
from difflib import get_close_matches
import json


data = Path("dictionary_compact.json").read_text()
words_list = json.loads(data)

def get_user_input():
    word = input("please enter the word:\n ")
    return word

def confirm_new_word(word):
   return input (f"if you are looking for '{word}' please enter yes:\n")
   

def search_in_dictionary(w):
    try:
        meanings = words_list[w]
        print(meanings)
    except:
        similar_words = get_close_matches(w, words_list.keys() , n = 5 , cutoff = 0.8)
        if similar_words:
            result = confirm_new_word(similar_words[0])
            if result.lower == 'yes':
                search_in_dictionary(w[0])
        else:
            print("The search has no results...")







word = get_user_input()
search_in_dictionary(word)



    

    


