'''

Tkinter colours --> https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html

'''


import tkinter as tk
from tkinter import ttk
from tkinter import * 
from PIL import Image, ImageTk
import os
from info import pre_processed_images, labels

# Tkinter configurations

root = tk.Tk()
style = ttk.Style()
root.title("Airplane Identification Quiz")
root.configure(bg="white")

counter = 0 # !TEMP Counter for the progress bar
question = 1 # Current question
score = 0 # number of correct answers
MAX_QUESTIONS = len(pre_processed_images)/2

processed_images = [] # Empty array to add the processed PIL objects to
stack = [] # Temporary stack for the images
entries = []

style.configure("TProgressbar", troughcolor='white', bordercolor='white', background='lightblue', thickness=20)

# Loading images with PIL

for image in pre_processed_images:

    img = Image.open(f"./{image}")
    img = img.resize((300,240), Image.LANCZOS)
    tk_img = ImageTk.PhotoImage(img)
    processed_images.append(tk_img)

# Add the first two initial images to the temporary stack
    
stack.append(processed_images[0])
stack.append(processed_images[1])

# Submit Button

def handle_next():

    global processed_images, stack, question, score # Making the variables global since we're reassigning its value locally
    
    answer1, answer2 = get_user_input()

    if question in range(1, int(MAX_QUESTIONS)):
    
        if answer1 in labels[question-1][0]:
            score +=1
        if answer2 in labels[question-1][1]:
            score += 1

    if question != MAX_QUESTIONS:

        if len(processed_images) > 0:
            processed_images = processed_images[2:]
            stack = processed_images[0:2]

        question += 1
        
        question_label.config(text=f"Question {question}/4")
        score_label.config(text=f"Score: {score}")
        question_text.destroy()

        entries.clear()
        load_images()

    refresh_frame()

    if question == MAX_QUESTIONS:
        button.destroy()
        handle_submit()

def handle_submit():

    for widget in image_input_frame.winfo_children():
        widget.destroy()
    
    final_score = tk.Label(
        top_frame,
        text=f"Final Score: {score}",
        font=("Helvetica", 16, "bold")
    )

    percentage_score = tk.Label(
        middle_frame,
        text=str(int((score/(MAX_QUESTIONS*2))*100))
    )

    percentage_score.pack()

    final_score.pack()


# "Next" Button

button = tk.Button(text="Next", justify="center", padx=40, pady=10, bg="lightblue", relief=FLAT, font=("Helvetica", 12, 'bold'), command=handle_next)

# Frames

top_frame = tk.Frame(root, bg="black", height=60)
top_frame.pack(expand=True, fill=tk.X)

middle_frame = tk.Frame(root, bg="white")
middle_frame.pack(pady=20, expand=True, fill=tk.X)

question_text = tk.Label(
    middle_frame,
    text="Identify these aircraft",
    font=("Arial", 14, "italic"),
    bg="white",
    justify="left",
)

question_text.pack(pady=(0, 20))

button.pack()

image_input_frame = tk.Frame(middle_frame, bg="white")
image_input_frame.pack()

bottom_frame = tk.Frame(root, bg="white")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)

# Question Header

question_label = tk.Label(
    top_frame,
    text=f"Question {question}/{int(MAX_QUESTIONS)}",
    fg="white",
    bg="black",
    font=("Arial", 16, "bold")
)

question_label.pack()

score_label = tk.Label(
    top_frame,
    text=f"Score: {score}",
    fg="white",
    bg="blue",
    font=("Arial", 16, "bold")
)

score_label.pack()

# Image input function

def create_image_input(parent, img):
    
    container = tk.Frame(parent, bg="white", bd=1, padx=10, pady=10)
    
    image_placeholder = tk.Label(container, image=img, bg="white")
    image_placeholder.pack(pady=(0, 10))

    entry = tk.Entry(container, width=30, font=("Arial", 11), highlightthickness=1, highlightbackground="black")
    entry.pack()
    entries.append(entry)

    container.pack(side=tk.LEFT, padx=30)

def get_user_input():
    return ([entry.get() for entry in entries])

def load_images():
    
    for widget in image_input_frame.winfo_children():
        widget.destroy()

    for i in range(len(stack)):
        create_image_input(image_input_frame, stack[i])

load_images()

# Tick

tick_label = tk.Label(
    bottom_frame,
    text="",
    font=("Arial", 16),
    bg="white"
)

tick_label.pack()

# Progress Bar

progress = ttk.Progressbar(
    bottom_frame,
    orient="horizontal",
    length=800,
    mode="determinate",
)

progress["value"] = 0
progress.pack(pady=25)

# Refresh Progress Bar

def refresh_frame():
    global counter
    progress["value"] = ((question)/MAX_QUESTIONS)*100
    counter += 1

refresh_frame()
root.mainloop()
