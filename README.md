# Quiz_2024ProgII_Assignment2
This is the repository where I will be working on the #2 assignment regarding Programming II.

# TKinter-based Python quiz game
## Created by: Márió Palágyi at IMC Krems FH, University of Applied Sciences

Design and major choices:
- I used TKinter for the quiz app and had to import PIL for the images
- the server communication is made possible by Django, I utilized the schemas studied during our Programming class on Django and also tweaked it some by myself
- I put everything in one file, as this was the most straight-forward for me
- I always defined an attribute of the main class Quiz, when I knew that I would have needed that specific attribute in the future, e.g. self.ScoreLabel
- I created a virtual environment to store my dependencies, as this makes it easy to follow what I needed
- I utilized my design knowledge, gained from the Design Lectures this semester and hand-drawn multiple copies of low-fidelity design on paper, horizontally, to explore the range of functionalities, and also vertically to study the depth needed
- I used sqlite3 for the database, it is lightweight, but can manage all the tables that I needed. When a user registers, their information gets recorded in both the Users and the Leaderboard tables 

Requirements:
- Django 5.0.6
- urllib3 == 2.2.2
- (also: "pip install -r requirements" in the terminal)

### Instructions on how to play:
- activate your virtual environment (".\.venv\Scripts\activate")
-  type "py manage.py runserver" in terminal to run the server
- start quiz.py manually or in the terminal to start the application
- the rest of the instructions is on the Instruction Page, marked by the "?" sign at the top left corner

There were some major errors, such as Bad Request error 400 at the login screen. That is the reason, that there is no 
login implementation.
Also, I started using requests package, but later resorted to urllib, even though I had to start again a big part of the
functionality. There was a circular implementation error that I couldn't figure out ("AttributeError: partially initialized module 'charset-normalizer' has no attribute 'md__mypyc' (most likely due to a circular import)"). I searched on multiple
websites, like stackoverflow, reddit and some people had a similar problem, but no one's solution worked for me.
The topic and own question creation screen is also missing, as I have run out of time by the end, but I feel like I could implement it if given more time.

Minor improvements would be to make the code neater. This is the first time I worked with TKinter and I feel
like there are lots of conventions that I should follow, I had to resort to hard coding most of the stuff.
There are lots of better ways I could do things better. I should have also created a quiz brain/functionality folder where 
I store the different methods and requests, so the main file doesn't get overcrowded.
I should have written more tests and cared more about the design.

