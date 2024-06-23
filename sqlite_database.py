import sqlite3
import os

# Database file path definition
db_folder = "quiz"
db_file = "db.sqlite3"
db_path = os.path.join(db_folder, db_file)

# Creation of db folder, if it doesn't exist
os.makedirs(db_folder, exist_ok=True)

# Connection to sqlite database, in case it doesn't exist, it creates it also
conn = sqlite3.connect(db_path)

# assign cursor to variable
cursor = conn.cursor()

# Executes the query that creates the table PublicQuestions, with attributes id, title, a, b, c, d (options),
# the correct answer (single letter), the question difficulty and topic
cursor.execute('''CREATE TABLE IF NOT EXISTS PublicQuestions (
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
                title TEXT, 
                a TEXT, 
                b TEXT, 
                c TEXT, 
                d TEXT, 
                correct_answer TEXT, 
                diff TEXT, 
                topic TEXT)''')

# Executes the query that creates the Users table, with attributes id, username, password, points, last_login, is_active
# is_admin. The last 3 attributes are only needed for Django to properly function
cursor.execute('''CREATE TABLE IF NOT EXISTS Users
               (id INTEGER PRIMARY KEY AUTOINCREMENT, 
               username TEXT,
               password TEXT,
               points INT,
               last_login DATETIME,
               is_active INT,
               is_admin INT)''')

# Executes the query that creates the PrivateQuestions table, with attributes id, user_id
# (which is a foreign key from Users table), the question title, ans_a, ans_b, ans_c, ans_d (answer options),
# correct_answer, which is a single letter and
cursor.execute('''CREATE TABLE IF NOT EXISTS PrivateQuestions 
               (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                user_id INTEGER, 
                title TEXT UNIQUE, 
                ans_a TEXT, 
                ans_b TEXT, 
                ans_c TEXT, 
                ans_d TEXT, 
                correct_answer TEXT,
                FOREIGN KEY (user_id) REFERENCES Users(id))''')

# Executes the query that creates the Leaderboard table, with attributes id, username, points (user score) and the date
# that it was achieved. The date_achieved attribute is also something needed for django functionality, otherwise
# I received an error.
cursor.execute('''CREATE TABLE IF NOT EXISTS Leaderboard
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT,
               points INT,
               date_achieved DATETIME)''')

# Questions: their titles, the 4 options, the correct answer, the appropriate difficulty, and their topic
# in a list of tuples, assigned to a variable
publ_questions = [
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
                   ]

# The query that Inserts the questions into PublicQuestions table. This query makes it possible to insert
# multiple values at the same time, using the publ_questions variable
cursor.executemany('''INSERT INTO PublicQuestions (title, a, b, c, d, correct_answer, diff, topic) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                   ''', publ_questions)

conn.commit()
conn.close()