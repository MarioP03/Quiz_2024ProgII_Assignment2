from tkinter import *
from PIL import Image, ImageTk


def createTxtlabel(master, txt):
    return Label(master, text=txt, font="Verdana 12 bold")

# def createImglabel(master, loc):
#     return Label(master, image=loc)

class Quiz(Tk):
    def __init__(self):
        super().__init__()
        self.title("UnoVia")
        self.iconbitmap("assets/checkbox.ico")
        self.window_width = 600
        self.window_height = 500

        # We look for the user's screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # We calculate x and y coordinates, so we can properly place the window always in the middle
        x_cor = (screen_width - self.window_width) // 2
        y_cor = 20

        self.geometry(f"{self.window_width}x{self.window_height}+{x_cor}+{y_cor}")

        welcome_label = createTxtlabel(self, "UnoVia")

        welcome_label.pack()

        self.photo1 = ImageTk.PhotoImage(Image.open("assets/quiz_welcome.jpg"))

        image_label = Label(self, image=self.photo1)
        image_label.pack()



if __name__ == '__main__':
    app = Quiz()
    app.mainloop()

    # root1 = Tk()
    # root1.title("UnoVia")
    # root1.iconbitmap("assets/checkbox.ico")
    #
    # window_width = 600
    # window_height = 500
    #
    # # We look for the user's screen dimensions
    # screen_width = root1.winfo_screenwidth()
    # screen_height = root1.winfo_screenheight()
    #
    # # We calculate x and y coordinates, so we can properly place the window always in the middle
    # x_cor = (screen_width - window_width) // 2
    # y_cor = 20
    #
    # root1.geometry(f"{window_width}x{window_height}+{x_cor}+{y_cor}")
    #
    # welcome_label = createTxtlabel(root1, "UnoVia")
    #
    # welcome_label.pack()
    #
    # photo = ImageTk.PhotoImage(Image.open("assets/quiz_welcome.jpg"))
    #
    # image_label = Label(root1, image=photo)
    # image_label.pack()
    #
    # test_btn = Button(text="WowButton")
    #
    # mainloop()

