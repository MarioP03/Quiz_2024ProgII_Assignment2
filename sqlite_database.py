import sqlite3
import os

# Database file path definition
db_folder = "db"
db_file = "questions_users.db"
db_path = os.path.join(db_folder, db_file)

# Creation of db folder, if it doesn't exist
os.makedirs(db_folder, exist_ok=True)

# Connection to sqlite database, in case it doesn't exist, it creates it also
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS PublicQuestions (
               question_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                title TEXT, 
                a TEXT, 
                b TEXT, 
                c TEXT, 
                d TEXT, 
                correct_answer TEXT, 
                diff TEXT, 
                topic TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Users
               (user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
               user_name TEXT,
               points INT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS PrivateQuestions 
               (qestion_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                user_id INTEGER, 
                title TEXT, 
                ans_a TEXT, 
                ans_b TEXT, 
                ans_c TEXT, 
                ans_d TEXT, 
                correct_answer TEXT,
                FOREIGN KEY (user_id) REFERENCES Users(user_id))''')

cursor.executemany('''INSERT INTO PublicQuestions (title, a, b, c, d, correct_answer, diff, topic) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                   ''', [
                   ('Who is the original author of the song "Hound Dog" by Elvis Presley?', 'himself.', 'Frank Sinatra', 'Big Mama Thornton', 'Wolfgang Amadeus Mozart', 'c', 'hard', 'music'),
                    ('What is the first rule of ... what club?', 'You dont talk about the Fight Club + Fight Club :)', 'the Avengers', 'Always bring your own book - Book Club', 'What rule? What club?', 'd', 'hard', 'movies'),
                    ('What did the Avengers eat at the end of the first movie??', 'döner', 'shawarma', 'the died.', 'langos', 'b', 'hard', 'movies'),
                    ('Who played Mr. Bean in the live-action series?', 'Rowan Atkinson', 'Mr. Bean himself', 'Robin Williams', 'Fred Rogers', 'a', 'medium', 'movies'),
                    ('Which character does Javier Bardem play in the movie "No Country for Old Men"?', 'Anton Chigurh', 'the policeman', 'random victim', 'Carson Wells', 'a', 'medium', 'movies'),
                    ('Which character says "No, I am your Father"?', 'Master Oogway', 'Darth Vader', 'Luke Skywalker', 'Han Solo', 'b', 'easy', 'movies'),
                    ('There is a coffee bean extracted from ... poop?', 'dog', 'fly', 'Kopi Luwak', 'anaconda', 'c', 'hard', 'cooking'),
                    ('What is the base ingredient of gummy bears?', 'gelatin', 'sugar', 'food-colouring', 'small bear cubs', 'a', 'easy', 'cooking'),
                    ('What are hot-dogs made of?', 'kielbasa', 'lean meat', 'emulsified meat trimmings', 'I would rather not know', 'c', 'medium', 'cooking'),
                    ('Which chocolate bar is the best?', 'obviously Mars', 'Milka is austrian, so Milka', 'I like Snickers', 'Eminem', 'a', 'easy', 'cooking'),
                    ('True or False? Cutting steak against the grain makes it more tender', 'True', 'False', 'I dont eat steak.', 'Depends...', 'a', 'medium', 'cooking'),
                    ('Who was the most trending female artist of 2023?', 'Doja Cat', 'Beyoncé', 'Rosalía', 'Taylor Swift', 'd', 'medium', 'music'),
                    ('Which rapper wrote the song "Candy Shop"?', '50 Cent', 'Chris Brown', 'Dr. Dre', 'Snoop Dogg', 'a', 'easy', 'music'),
                    ('Who wrote the diss track, titled "Rap Devil" about Eminem in 2018?', 'The Migos', 'NF', 'Machine Gun Kelly', 'Logic', 'c', 'medium', 'music'),
                    ('Which of the mentioned singers also act in the movie "A Star is Born" (2018)?', 'Lady Gaga', 'Lana Del Rey', 'Judy Garland', 'Rihanna', 'a', 'easy', 'movies')
                   ])

conn.commit()
conn.close()