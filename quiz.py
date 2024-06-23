from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import os
import random
import urllib.request
import json


class Quiz(Tk):
    def __init__(self):
        super().__init__()
        self.difficulty = "intermediate"  # for later purpose of diff level
        self.cqi = 0  # cqi = Current Question Index
        self.questions = self.get_all_questions()
        self.username = ""
        self.userid = None
        self.title("UnoVia")
        self.iconbitmap("assets/checkbox.ico")
        self.window_width = 1000
        self.window_height = 700
        self.configure(bg='#fff2e6')  # Set the background color
        self.userscore = 0
        self.correct_answer = ""

        self.cglist = ["Congrats!", "much wow, such smart", "Good job!"]
        self.faillist = ["Oops!", "Next time...", "Almost!"]
        self.pending_choice = ["Give up?", "Think, think, think...", "-_-'"]

        # The grid weights allow columns to expand, so we set them
        for i in range(5):
            self.grid_columnconfigure(i, weight=1)

        # We look for the user's screen dimensions
        screen_width = self.winfo_screenwidth()

        # We calculate x and y coordinates, so we can properly place the window always in the middle
        x_cor = (screen_width - self.window_width) // 2
        y_cor = 20

        self.geometry(f"{self.window_width}x{self.window_height}+{x_cor}+{y_cor}")
        self.HomeScreen()

    def ClearScreen(self):
        for widget in self.winfo_children():
            if widget not in (self.home_button, self.help_button, self.user_label, self.logout_button,
                              self.user_score_label):  # only destroys widgets that are not supposed to be displayed at all times
                widget.destroy()
        return

    def HomeScreen(self):
        self.ClearScreen()
        welcome_label = Label(self, text="UnoVia", bg="#fff2e6", font="Verdana 12 bold")
        welcome_label.grid(column=2, row=0)

        self.photo1 = ImageTk.PhotoImage(Image.open("assets/quiz_welcome.jpg"))
        image_label = Label(self, image=self.photo1)
        image_label.grid(column=2, row=2)

        self.photo2 = ImageTk.PhotoImage(Image.open("assets/Help.jpg"))
        self.help_button = Button(self, text="Help", image=self.photo2, command=self.HelpScreen)
        self.help_button.grid(column=0, row=0, pady=20, padx=10)

        self.photo3 = ImageTk.PhotoImage(Image.open("assets/Home.jpg"))
        self.home_button = Button(self, text="Home", image=self.photo3, command=self.HomeScreen)
        self.home_button.grid(column=3, row=0, sticky="e", pady=10)

        self.user_label = Label(self, text=f"User: {self.username}" if self.username else "User - Not logged in",
                                font="Arial 8 italic")
        self.user_label.grid(column=3, row=1, sticky="e")

        self.user_score_label = Label(self, text=f"Score: {self.userscore}" if self.username
        else "No login = No score :(",
                                      font="Arial 10 italic bold")
        self.user_score_label.grid(column=3, row=10, sticky="e")

        self.logout_button = Button(text="Log out", command=self.logout)
        self.logout_button.grid(column=3, row=2, sticky="ne")

        frame_buttons = LabelFrame(self, text="You can start playing or Create a New Question list!",
                                   font="Verdana 12 bold", padx=10, pady=10)
        frame_buttons.grid(column=2, row=3, padx=10, pady=10)

        # Configure the grid within the frame to have a single centered column
        frame_buttons.grid_columnconfigure(0, weight=1)

        play_button = Button(frame_buttons, text="PLAY", font="Verdana 12 bold", command=self.play)
        play_button.grid(column=0, row=0, pady=10)
        new_button = Button(frame_buttons, text="CREATE", font="Verdana 12 bold", command=self.UniqueQuestionScreen)
        new_button.grid(column=0, row=1, pady=10)

        exit_button = Button(text="EXIT", font="Verdana 12 bold", bg="red", command=lambda: self.quit())
        exit_button.grid(column=2, row=6, pady=20)

    def HelpScreen(self):
        self.ClearScreen()
        expl = LabelFrame(self, padx=10, pady=10, text="Description", font="Verdana 12 bold")
        expl.grid(column=2, row=2, padx=10, pady=10)
        descr = Label(expl, text='''This is a TKinter-based, Python 
        quiz game. To play, simply register. Make sure to register a 
        new account each time you enter. This is a race to do as 
        many questions as you can in one sitting. You will compete
        with other users around the world. Your username must be
        made of lowercase letters and numbers, at least 8 characters
        long. The password you choose should also contain at least
        8 characters, lowercase and uppercase alike, with some numbers.
        After that, jump to the Home Screen (House icon on the top right) 
        and start playing. You should be able to choose a difficulty 
        or play all questions. The topic and own question creation tool
        are still under implementation. When you finish, you get a message
        and your score gets added. When you feel like it, log out. This is the
        end of your session.

        I heard once that you should leave tomorrow's problems to 
        tomorrow's You.
        But this game is the
        exception!
        Play now! And play twice more tomorrow! 

        It's the result of long hours of work, mixed with blood, 
        sweat and tears. Even though there were difficulties on 
        the way, it didn't stop me to create 
        something cool. I feel proud.
        
        Have fun :)
        ''', font="Verdana 10")
        descr.pack(padx=10, pady=10)

    def play(self):
        if len(self.username) > 0:
            self.DiffScreen()
        else:
            self.RegisterScreen()

    def logout(self):
        if self.username:
            self.username = ""
            self.user_label.config(text="User: Not logged in")
            self.userscore = 0
            self.cqi = 0
            self.HomeScreen()

    def RegisterScreen(self):
        self.ClearScreen()
        SignFrame = LabelFrame(self, text="Did you already register?", background="grey",
                               font="Verdana 12 bold")
        SignFrame.grid(column=2, row=2, padx=10, pady=10, ipadx=40, ipady=30, sticky="nsew")
        RegisterFrame = LabelFrame(SignFrame, text="Register here!",
                                   font="Verdana 12 bold")
        RegisterFrame.pack(pady=10)
        entry_name = Entry(RegisterFrame)
        entry_name.pack(pady=5)
        entry_pwd = Entry(RegisterFrame)
        entry_pwd.pack(pady=5)
        entry_button = Button(RegisterFrame, text="Register", command = lambda : [self.register_user(username = entry_name.get(), password1 = entry_pwd.get(), password2 = entry_pwd.get())])
        entry_button.pack(pady=10)

        # LoginFrame = LabelFrame(SignFrame, text="Log in here! (if you have an account)",
        #                         font="Verdana 12 bold")
        # LoginFrame.pack(side=BOTTOM, pady=20)
        # login_name = Entry(LoginFrame)
        # login_name.pack(pady=5)
        # login_pwd = Entry(LoginFrame)
        # login_pwd.pack(pady=5)
        # login_button = Button(LoginFrame, text="Log in", command = lambda : self.login_user(username = entry_name.get(), password = entry_pwd.get()))
        # login_button.pack(pady=10)

    def login_user(self, username, password):
        data = {'username': username, 'password': password}
        encoded_data = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request('http://localhost:8000/quiz/login/', data = encoded_data, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        try:
            with urllib.request.urlopen(req) as response:
                response = json.loads(response.read().decode('utf-8'))
                if response['status'] == 'error':
                    return None
                self.username = response['data']['username']
        except urllib.error.HTTPError as e:
            print('HTTPError: ', e)
        except urllib.error.URLError as e:
            print('URLError: ', e)

    def register_user(self, username, password1, password2):
        data = {'username': username, 'password1': password1, 'password2': password2, 'points': 0}
        encoded_data = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request('http://localhost:8000/quiz/register/', data = encoded_data, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        try:
            with urllib.request.urlopen(req) as response:
                response = json.loads(response.read().decode('utf-8'))
                if response['status'] == 'error':
                    return None
                self.username = response['data']['username']
        except urllib.error.HTTPError as e:
            print('HTTPError: ', e)
        except urllib.error.URLError as e:
            print('URLError: ', e)

    def get_userid(self):
        db_folder = "quiz/"
        db_file = "db.sqlite3"
        db_path = os.path.join(db_folder, db_file)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f"SELECT user_id FROM Users WHERE user_name = {self.username}")
        userid = cursor.fetchone()
        conn.close()
        return userid

    def get_username(self):
        data = {'username':self.username}
        encoded_data = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request('http://localhost:8000/quiz/register/', data = encoded_data, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        try:
            with urllib.request.urlopen(req) as response:
                response = json.loads(response.read().decode('utf-8'))
                if response['status'] == 'error':
                    return None
                return response['data']
        except urllib.error.HTTPError as e:
            print('HTTPError: ', e)
        except urllib.error.URLError as e:
            print('URLError: ', e)

    def get_userscore(self):
        db_folder = "quiz/"
        db_file = "db.sqlite3"
        db_path = os.path.join(db_folder, db_file)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f"SELECT points FROM Users WHERE user_name = {self.username}")
        userpoints = cursor.fetchone()
        conn.close()
        return userpoints

    def DiffScreen(self):
        self.ClearScreen()
        choose_diff_lab = LabelFrame(self, text="Choose difficulty", cursor="question_arrow", background="lightpink",
                                     font="Verdana 12 bold")
        choose_diff_lab.grid(column=2, row=2, padx=10, pady=10, ipadx=40, ipady=30, sticky="nsew")
        All_button = Button(choose_diff_lab, text="All", font="Verdana 14 bold", bd=5,
                             command=lambda :[self.all_click(), self.AllQuestions()])
        All_button.pack(pady=20)
        easy_button = Button(choose_diff_lab, text="Easy", font="Verdana 14 bold", bd=5, fg="#006600",
                             command=lambda :[self.easy_click(), self.AllQuestions()])
        easy_button.pack(pady=20)
        medium_button = Button(choose_diff_lab, text="Intermediate", font="Verdana 14 bold", bd=5, fg="#0066cc",
                             command=lambda :[self.inter_click(), self.AllQuestions()])
        medium_button.pack(pady=10)
        hard_button = Button(choose_diff_lab, text="Difficult", font="Verdana 14 bold", bd=5, fg="#990000",
                             command=lambda :[self.hard_click(), self.AllQuestions()])
        hard_button.pack(pady=10)
        # topic_button = Button(choose_diff_lab, text="Choose a topic", activeforeground="red", font="Verdana 14 bold", )
        # topic_button.pack(pady=10)
        # own_q_button = Button(choose_diff_lab, text="Play own questions", activeforeground="purple",
        #                       font="Verdana 8 italic", underline=0)
        # own_q_button.pack(pady=15, side=BOTTOM)

    def all_click(self):
        self.questions = self.get_all_questions()

    def get_all_questions(self):
        db_folder = "quiz/"
        db_file = "db.sqlite3"
        db_path = os.path.join(db_folder, db_file)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT title, a, b, c, d, correct_answer, diff, topic FROM PublicQuestions")
        questions = cursor.fetchall()
        conn.close()
        return questions

    def easy_click(self):
        self.questions = self.get_easy_questions()
        self.difficulty = "easy"
    def inter_click(self):
        self.questions = self.get_inter_questions()
        self.difficulty = "medium"
    def hard_click(self):
        self.questions = self.get_hard_questions()
        self.difficulty = "hard"


    def get_easy_questions(self):
        db_folder = "quiz/"
        db_file = "db.sqlite3"
        db_path = os.path.join(db_folder, db_file)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT title, a, b, c, d, correct_answer, diff, topic FROM PublicQuestions WHERE diff = 'easy'")
        questions = cursor.fetchall()
        conn.close()
        return questions

    def get_inter_questions(self):
        db_folder = "quiz/"
        db_file = "db.sqlite3"
        db_path = os.path.join(db_folder, db_file)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT title, a, b, c, d, correct_answer, diff, topic FROM PublicQuestions WHERE diff = 'medium'")
        questions = cursor.fetchall()
        conn.close()
        return questions

    def get_hard_questions(self):
        db_folder = "quiz/"
        db_file = "db.sqlite3"
        db_path = os.path.join(db_folder, db_file)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT title, a, b, c, d, correct_answer, diff, topic FROM PublicQuestions WHERE diff = 'hard'")
        questions = cursor.fetchall()
        conn.close()
        return questions

    def show_question_details(self):
        if self.cqi < len(self.questions):
            title, a, b, c, d, corr, diff, topic = self.questions[self.cqi]
            self.TitleLabel.config(text=title)
            self.A_btn.config(text=a)
            self.B_btn.config(text=b)
            self.C_btn.config(text=c)
            self.D_btn.config(text=d)
            self.correct_answer = corr
        elif self.cqi + 1 == len(self.questions):
            self.finish_quiz()

    def finish_quiz(self):
        self.NextButton.pack_forget()
        self.CheckQuestionLabel.pack_forget()
        self.TitleLabel.config(text="Congratulations, you... finished?!")
        for btn in [self.A_btn, self.B_btn, self.C_btn, self.D_btn]:
            btn.pack_forget()
        if self.userscore >= 0 and self.userscore < 6:
            self.ScoreLabel.config(text=f"Final Score: {self.userscore}... meh")
        elif self.userscore >= 6 and self.userscore < 10:
            self.ScoreLabel.config(text=f"Final Score: {self.userscore}... not great, not terrible")
        else:
            self.ScoreLabel.config(text=f"Final Score: {self.userscore}... WOW O_O, you are well-informed")
        self.user_score_label.config(text=f"Score: {self.userscore}")
        self.cqi = 0
        # TODO: add userscore to user details in db

    def check_answer_correctness(self, choice):
        
        if choice == self.correct_answer:
            congrats_text = random.choice(self.cglist)
            self.CheckQuestionLabel.configure(text=congrats_text, fg="green")
            self.userscore += 1
            for btn in [self.A_btn, self.B_btn, self.C_btn, self.D_btn]:
                btn.pack_forget()
        else:
            fail_text = random.choice(self.faillist)
            for btn in [self.A_btn, self.B_btn, self.C_btn, self.D_btn]:
                btn.pack_forget()
            self.CheckQuestionLabel.configure(text=fail_text, fg="red")
            # TODO: only deduce a point in hard ;self.userscore -= 1
            self.ScoreLabel.config(text=f"Score: {self.userscore}")


    def next_question_jump(self):
        self.AllQuestions()
        if self.cqi < len(self.questions) - 1:
            self.cqi += 1
            self.show_question_details()
        else:
            self.finish_quiz()

    def AllQuestions(self):
        self.ClearScreen()
        QuestionFrame = LabelFrame(self, text="Questions and Answers!")
        QuestionFrame.grid(column=2, row=2, padx=10, pady=10, ipadx=40, ipady=30, sticky="nsew")
        qs_label = Label(QuestionFrame, anchor="center", wraplength=500, pady=10, padx=10)
        qs_label.pack(pady=10)

        self.TitleLabel = Label(QuestionFrame, text=f"title", font="Verdana 12 bold")
        self.TitleLabel.pack(pady=10)
        self.A_btn = q_btn = Button(QuestionFrame, text="QuestionPLaceHolderForButton",
                           activebackground="black", command= lambda :self.check_answer_correctness("a"))
        self.A_btn.pack(pady=5)
        self.B_btn = q_btn = Button(QuestionFrame, text="QuestionPLaceHolderForButton",
                               activebackground="black", command= lambda :self.check_answer_correctness("b"))
        self.B_btn.pack(pady=5)
        self.C_btn = q_btn = Button(QuestionFrame, text="QuestionPLaceHolderForButton",
                               activebackground="black", command= lambda :self.check_answer_correctness("c"))
        self.C_btn.pack(pady=5)
        self.D_btn = q_btn = Button(QuestionFrame, text="QuestionPLaceHolderForButton",
                               activebackground="black", command= lambda :self.check_answer_correctness("d"))
        self.D_btn.pack(pady=5)

        self.ScoreLabel = Label(QuestionFrame, text=f"Score: {self.userscore}", font="Verdana 12 italic")
        self.ScoreLabel.pack(pady=20)

        self.CheckQuestionLabel = Label(QuestionFrame, text=random.choice(self.pending_choice), font="Verdana 12 bold")
        self.CheckQuestionLabel.pack(pady=20)

        self.NextButton = Button(QuestionFrame, text="Another One", command=self.next_question_jump)
        self.NextButton.pack(pady=10)

        self.show_question_details()

    def UniqueQuestionScreen(self):
        self.ClearScreen()
        ImAUniqueLabel = LabelFrame(text="Enter your question's parameters", font="Verdana 14 bold")
        ImAUniqueLabel.grid(column=2, row=2, padx=10, pady=10, ipadx=40, ipady=30, sticky="nsew")
        label_q_title = Label(ImAUniqueLabel, text="Question Title", font="Verdana 12 bold")
        label_q_title.pack()
        q_title = Entry(ImAUniqueLabel, width=30)
        q_title.pack()
        label_a = Label(ImAUniqueLabel, text="Answer 1", font="Verdana 12 italic")
        label_a.pack()
        q_a = Entry(ImAUniqueLabel, width=30)
        q_a.pack()
        label_b = Label(ImAUniqueLabel, text="Answer 2", font="Verdana 12 italic")
        label_b.pack()
        q_b = Entry(ImAUniqueLabel, width=30)
        q_b.pack()
        label_c = Label(ImAUniqueLabel, text="Answer 3", font="Verdana 12 italic")
        label_c.pack()
        q_c = Entry(ImAUniqueLabel, width=30)
        q_c.pack()
        label_d = Label(ImAUniqueLabel, text="Answer 4", font="Verdana 12 italic")
        label_d.pack()
        q_d = Entry(ImAUniqueLabel, width=30)
        q_d.pack()

        entry_button = Button(ImAUniqueLabel, text="Send", font="Verdana 12 bold")
        entry_button.pack(pady=10)


if __name__ == '__main__':
    app = Quiz()
    app.mainloop()