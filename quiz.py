from tkinter import *
from PIL import Image, ImageTk


# def createTxtlabel(root, txt):
#     return Label(root, text=txt, font="Verdana 12 bold")
#
# # def createImglabel(master, loc):
# #     return Label(master, image=loc)


class Quiz(Tk):
    def __init__(self):
        super().__init__()
        self.difficulty = "intermediate"  # for later purpose of diff level
        self.title("UnoVia")
        self.iconbitmap("assets/checkbox.ico")
        self.window_width = 800
        self.window_height = 600
        self.configure(bg='#fff2e6')  # Set the background color

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
            if widget not in (self.home_button, self.help_button):
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

        frame_buttons = LabelFrame(self, text="You can start playing or Create a New Question list!", font="Verdana 12 bold", padx=10, pady=10)
        frame_buttons.grid(column=2, row=3, padx=10, pady=10)

        # Configure the grid within the frame to have a single centered column
        frame_buttons.grid_columnconfigure(0, weight=1)

        play_button = Button(frame_buttons, text="PLAY", font="Verdana 12 bold", command=self.DiffScreen)
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

    def DiffScreen(self):
        self.ClearScreen()
        choose_diff_lab = LabelFrame(self, text="Choose difficulty", cursor="exchange", background="lightpink",
                                     font="Verdana 12 bold")
        choose_diff_lab.grid(column=2, row=2, padx=10, pady=10, ipadx=40, ipady=30, sticky="nsew")
        easy_button = Button(choose_diff_lab, text="Easy", font="Verdana 14 bold", bd=5, fg="#006600")
        easy_button.pack(pady=20)
        medium_button = Button(choose_diff_lab, text="Intermediate", font="Verdana 14 bold", bd=5, fg="#0066cc")
        medium_button.pack(pady=10)
        hard_button = Button(choose_diff_lab, text="Difficult", font="Verdana 14 bold", bd=5, fg="#990000")
        hard_button.pack(pady=10)
        topic_button = Button(choose_diff_lab, text="Choose a topic", activeforeground="red", font="Verdana 8 bold",)
        topic_button.pack(pady=10)

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



