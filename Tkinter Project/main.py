import tkinter
from tkinter import PhotoImage
import os

class MyGUI:

    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.state('zoomed')

        image = PhotoImage(file="emirates-777.jpg")

        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.title = tkinter.Label(self.top_frame, text="Airplane Quiz", font=("Helvetica", 20))
        self.questions = tkinter.Label(self.middle_frame, text="Question #/#", font=("Helvetica", 15), justify="left", bg="lightblue", padx=15, pady=5)

        self.title.pack(padx=300, pady=25)
        self.questions.pack(anchor="w", pady=10)

        self.top_frame.pack(fill="x")
        self.middle_frame.pack(fill="x")
        self.bottom_frame.pack()

        tkinter.mainloop()

gui = MyGUI()
