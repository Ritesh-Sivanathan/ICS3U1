'''
Name: Ritesh Sivanathan
Date: May 21, 2025
Description: Trying out Tkinter
'''

# main_window -> main window
# .pack() -> you need to pack your labels and frames

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()  # main window widget

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.other_frame = tkinter.Frame(self.main_window)

        self.physics = tkinter.Label(self.top_frame, text="Physics!", fg="purple", font=("Helvetica", 50), justify="left")
        self.rocks = tkinter.Label(self.other_frame, text="Rocks!", fg="grey", font=("Helvetica", 50))
        self.a = tkinter.Label(self.bottom_frame, text="A", fg="red", font=("Helvetica", 30))
        self.b = tkinter.Label(self.bottom_frame, text="B", fg="blue", font=("Helvetica", 30))

        self.physics.pack()
        
        self.a.pack(side="left")

        spacer = tkinter.Frame(self.bottom_frame)
        spacer.pack(side="left", expand=True, fill="x")

        self.b.pack(side="right")

        self.rocks.pack(side="bottom")
        self.top_frame.pack()
        self.bottom_frame.pack(fill="x", padx=10)
        self.other_frame.pack()

        tkinter.mainloop()

my_gui = MyGUI()
