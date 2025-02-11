import sqlite3

def get_user_input():
    word = input("please enter the word:\n ")
    return word

def search_in_dictionary(w):
    with sqlite3.connect("myapp.db") as conn:
        cursor = conn.cursor()
        command = "SELECT * FROM Dictionary WHERE word = ?"
        cursor.execute(command,(w,))
        rows = cursor.fetchall()
        if rows:
            print(rows)
        else:
            print("The search has no results...\n")

word = get_user_input()
search_in_dictionary(word)


