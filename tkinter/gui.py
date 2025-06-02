import tkinter as tk
from tkinter import ttk
from tkinter import * 
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("Airplane Identification Quiz")
root.configure(bg="white")

counter = 0

pre_processed_images = ['emirates-777x.jpg', 'dc-10.jpg', '787-dreamliner.jpg', 'e175.jpg']
labels = [['boeing 777x', 'boeing 777', '777', '777x'], ['mcdonnell douglas dc-10', 'md dc-10','dc-10', 'dc10'], ['boeing 787-9 dreamliner', 'boeing 787 dreamliner', '787-9', '787'], ['embraer 175', 'embraer e175', 'e175']]
processed_images = []
start = 0
funnel = pre_processed_images[start:start+2]

# Loading images with PIL

for image in pre_processed_images:

    img = Image.open(f"./{image}")
    img = img.resize((300,240))
    tk_img = ImageTk.PhotoImage(img)
    processed_images.append(tk_img)

# Submit Button

def handle_next():
    global start
    start += 2
    load_images()


button = tk.Button(text="Next", justify="center", padx=40, pady=10, bg="lightblue", relief=FLAT, font=("Helvetica", 12, 'bold'), command=handle_next)

# Frames

top_frame = tk.Frame(root, bg="black", height=60)
top_frame.pack(fill=tk.X)

middle_frame = tk.Frame(root, bg="white")
middle_frame.pack(pady=20)

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
    text="Question 0/0",
    fg="white",
    bg="black",
    font=("Arial", 16, "bold")
)

question_label.pack(pady=15)

# Image input function

def create_image_input(parent, img):
    
    container = tk.Frame(parent, bg="white", bd=1, padx=10, pady=10)
    
    image_placeholder = tk.Label(container, image=img, bg="white")
    image_placeholder.pack(pady=(0, 10))

    entry = tk.Entry(container, width=30, font=("Arial", 11), highlightthickness=1, highlightbackground="black")
    entry.pack()

    container.pack(side=tk.LEFT, padx=30)


def load_images():
    for i in range(len(funnel)):
        create_image_input(image_input_frame, processed_images[start + i])

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
    mode="determinate"
)

progress["value"] = 0
progress.pack(pady=25)

# Refresh Progress Bar

def refresh_frame():
    global counter
    progress["value"] = counter % 101
    counter += 1
    root.after(100, refresh_frame)

refresh_frame()
root.mainloop()
