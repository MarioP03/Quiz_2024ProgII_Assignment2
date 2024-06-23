from tkinter import *
from PIL import Image, ImageTk
import sqlite3
import os


class Quiz(Tk):
    def __init__(self):
        super().__init__()
        self.difficulty = "intermediate"  # for later purpose of diff level
        self.cqi = 0  # cqi = Current Question Index
        self.questions = self.get_questions()
        self.username = "Mario"
        self.title("UnoVia")
        self.iconbitmap("assets/checkbox.ico")
        self.window_width = 1000
        self.window_height = 650
        self.configure(bg='#fff2e6')  # Set the background color
        self.userscore = 0
        self.correct_answer = ""



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
            if widget not in (self.home_button, self.help_button, self.user_label, self.logout_button, self.user_score_label):  # only destroys widgets that are not supposed to be displayed at all times
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
        self.home_button = Button(self, text="Home", image=self.photo3, command= self.HomeScreen)
        self.home_button.grid(column=3, row=0, sticky="e", pady=10)

        self.user_label = Label(self, text=f"User: {self.username}" if self.username else "User - Not logged in",
                                font="Arial 8 italic")
        self.user_label.grid(column=3, row=1, sticky="e")

        self.user_score_label = Label(self, text=f"Score: {self.userscore}" if self.username
                                else "No login = No score :(",
                                font="Arial 10 italic bold")
        self.user_score_label.grid(column=3, row=10, sticky="e")

        self.logout_button = Button(text="Log out", command= self.logout)
        self.logout_button.grid(column=3, row=2, sticky="ne")

        frame_buttons = LabelFrame(self, text="You can start playing or Create a New Question list!", font="Verdana 12 bold", padx=10, pady=10)
        frame_buttons.grid(column=2, row=3, padx=10, pady=10)

        # Configure the grid within the frame to have a single centered column
        frame_buttons.grid_columnconfigure(0, weight=1)

        play_button = Button(frame_buttons, text="PLAY", font="Verdana 12 bold", command=self.play)
        play_button.grid(column=0, row=0, pady=10)
        new_button = Button(frame_buttons, text="CREATE", font="Verdana 12 bold", command=self.UniqueQuestionScreen)
        new_button.grid(column=0, row=1, pady=10)

        exit_button = Button(text="EXIT", font="Verdana 12 bold", bg="red", command = lambda : self.quit())
        exit_button.grid(column=2, row=6, pady=20)

    def HelpScreen(self):
        self.ClearScreen()
        expl = LabelFrame(self, padx=10, pady=10, text="Description", font="Verdana 12 bold")
        expl.grid(column=2, row=2, padx=10, pady=10)
        descr = Label(expl, text='''This is a TKinter-based, Python 
        quiz game.
        It's the result of long hours of work, mixed with blood, 
        sweat and tears.Even though there were difficulties on 
        the way, it didn't stop me to create 
        something cool, something for me, 
        RékaLili, 
        my family, my mom,
        my dad, my sister, my
        other sister, my grandma, grandpa, grandma2, grandpa2,
        my dog, my other dog 
        etc...
        
        I heard once that you should leave tomorrow's problems to 
        tomorrow's You.
        But this game is the
        exception!
        Play now! And play twice more tomorrow! 
        
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
        entry_button = Button(RegisterFrame, text="Register")
        entry_button.pack(pady=10)

        LoginFrame = LabelFrame(SignFrame, text="Log in here! (if you have an account)",
                                font="Verdana 12 bold")
        LoginFrame.pack(side=BOTTOM, pady=20)
        login_name = Entry(LoginFrame)
        login_name.pack(pady=5)
        login_pwd = Entry(LoginFrame)
        login_pwd.pack(pady=5)
        login_button = Button(LoginFrame, text="Log in")
        login_button.pack(pady=10)

        own_q_button = Button(LoginFrame, text="Play own questions", activeforeground="purple",
                              font="Verdana 8 italic bold", underline=0)
        own_q_button.pack(pady=15, side=BOTTOM)

    def DiffScreen(self):
        self.ClearScreen()
        choose_diff_lab = LabelFrame(self, text="Choose difficulty", cursor="question_arrow", background="lightpink",
                                     font="Verdana 12 bold")
        choose_diff_lab.grid(column=2, row=2, padx=10, pady=10, ipadx=40, ipady=30, sticky="nsew")
        easy_button = Button(choose_diff_lab, text="Easy", font="Verdana 14 bold", bd=5, fg="#006600", command=self.Questions)
        easy_button.pack(pady=20)
        medium_button = Button(choose_diff_lab, text="Intermediate", font="Verdana 14 bold", bd=5, fg="#0066cc")
        medium_button.pack(pady=10)
        hard_button = Button(choose_diff_lab, text="Difficult", font="Verdana 14 bold", bd=5, fg="#990000")
        hard_button.pack(pady=10)
        topic_button = Button(choose_diff_lab, text="Choose a topic", activeforeground="red", font="Verdana 8 bold",)
        topic_button.pack(pady=10)
        own_q_button = Button(choose_diff_lab, text="Play own questions", activeforeground="purple", font="Verdana 8 italic", underline=0)
        own_q_button.pack(pady=15, side=BOTTOM)

    def get_questions(self):
        db_folder = "db/"
        db_file = "questions_users.db"
        db_path = os.path.join(db_folder, db_file)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT title, a, b, c, d FROM PublicQuestions")
        questions = cursor.fetchall()
        conn.close()
        return questions

    def show_question_details(self):
        if self.cqi < len(self.questions):
            title, a, b, c, d, corr = self.questions[self.cqi]
            self.TitleLabel.config(text=title)
            self.q_btn_list[0].config(text=a)
            self.q_btn_list[1].config(text=b)
            self.q_btn_list[2].config(text=c)
            self.q_btn_list[3].config(text=d)
            self.correct_answer = corr
        elif self.cqi + 1 == len(self.questions):
            self.finish_quiz()

    def finish_quiz(self):
        self.NextButton.pack_forget()
        self.TitleLabel.config(text="Congratulations, you... finished?!")
        for btn in self.q_btn_list:
            btn.pack_forget()
        if self.userscore >= 0 and self.userscore < 6:
            self.ScoreLabel.config(text=f"Final Score: {self.userscore}... meh")
        elif self.userscore >= 6 and self.userscore < 10:
            self.ScoreLabel.config(text=f"Final Score: {self.userscore}... not great, not terrible")
        else:
            self.ScoreLabel.config(text=f"Final Score: {self.userscore}... WOW O_O, you are well-informed")

        self.cqi = 0
        # TODO: add userscore to user details in db

    def check_answer_correctness(self):
        pass

    def next_question_jump(self):
        if self.cqi < len(self.questions) -1:
            self.cqi += 1
            self.show_question_details()
        else:
            self.finish_quiz()

    def Questions(self):
        self.ClearScreen()
        QuestionFrame = LabelFrame(self, text="Questions and Answers!")
        QuestionFrame.grid(column=2, row=2, padx=10, pady=10, ipadx=40, ipady=30, sticky="nsew")
        qs_label = Label(QuestionFrame, anchor="center", wraplength=500, pady=10, padx=10)
        qs_label.pack(pady=10)

        self.TitleLabel = Label(QuestionFrame, text=f"title", font="Verdana 12 bold")
        self.TitleLabel.pack(pady=10)
        self.q_btn_list = []
        for i in range(4):
            q_btn = Button(QuestionFrame, text="QuestionPLaceHolderForButtonETCETCCHECKLENGTH", activebackground="black")
            q_btn.pack(pady=5)
            self.q_btn_list.append(q_btn)
        self.ScoreLabel = Label(QuestionFrame, text=f"Score: ", font="Verdana 12 italic")
        self.ScoreLabel.pack(pady=20)

        self.NextButton = Button(QuestionFrame, text="Another One", command=self.next_question_jump)
        self.NextButton.pack(pady=10)

        self.show_question_details()

    def UniqueQuestionScreen(self):
        self.ClearScreen()
        ImAUniqueLabel = LabelFrame(text="Enter your question's parameters", font="Verdana 14 bold")
        ImAUniqueLabel.grid(column=2, row=2, padx=10, pady=10, ipadx=40, ipady=30, sticky="nsew")
        label_q_title = Label(ImAUniqueLabel, text="SMTH")
        label_q_title.pack()
        q_title = Entry(ImAUniqueLabel, width=30)
        q_title.pack()
        label_a = Label(ImAUniqueLabel, text="SMTH")
        label_a.pack()
        q_a = Entry(ImAUniqueLabel, width=30)
        q_a.pack()
        label_b = Label(ImAUniqueLabel, text="SMTH")
        label_b.pack()
        q_b = Entry(ImAUniqueLabel, width=30)
        q_b.pack()
        label_c = Label(ImAUniqueLabel, text="SMTH")
        label_c.pack()
        q_c = Entry(ImAUniqueLabel, width=30)
        q_c.pack()
        label_d = Label(ImAUniqueLabel, text="SMTH")
        label_d.pack()
        q_d = Entry(ImAUniqueLabel, width=30)
        q_d.pack()

        entry_button = Button(ImAUniqueLabel, text="Send", font="Verdana 12 bold")
        entry_button.pack(pady=10)




if __name__ == '__main__':
    app = Quiz()
    app.mainloop()



