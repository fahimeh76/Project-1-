import json
from pathlib import Path
import sqlite3

data = Path("dictionary_compact.json").read_text()
words_list = json.loads(data)

with sqlite3.connect("myapp.db") as conn:
    cursor = conn.cursor()
    table_command = """
        CREATE TABLE IF NOT EXISTS "Dictionary" (
	    "id"	INTEGER,
	    "word"	TEXT NOT NULL,
	    "meaning"	TEXT NOT NULL,
	    PRIMARY KEY("id")
);

"""
    cursor.execute(table_command)
    command = "INSERT INTO Dictionary (word,meaning) VALUES (?,?)"
    for word in words_list:
        for meaning in words_list[word]:
            cursor.execute(command , (word,meaning))
    conn.commit()
