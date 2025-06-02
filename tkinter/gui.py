import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("Question Interface")
root.geometry("900x600")
root.configure(bg="white")

print(os.getcwd())

counter = 0

img = Image.open("./emirates-777x.jpg")
img = img.resize((300,240))
tk_img = ImageTk.PhotoImage(img)

top_frame = tk.Frame(root, bg="black", height=60)
top_frame.pack(fill=tk.X)

question_label = tk.Label(
    top_frame,
    text="Question #/#",
    fg="white",
    bg="black",
    font=("Arial", 16, "bold")
)
question_label.pack(pady=15)

middle_frame = tk.Frame(root, bg="white")
middle_frame.pack(pady=20)

question_text = tk.Label(
    middle_frame,
    text="Question",
    font=("Arial", 14, "italic"),
    bg="white"
)
question_text.pack(pady=(0, 20))

image_input_frame = tk.Frame(middle_frame, bg="white")
image_input_frame.pack()

def create_image_input(parent):
    container = tk.Frame(parent, bg="white", bd=1, padx=10, pady=10)
    
    image_placeholder = tk.Label(container, image=tk_img, bg="white")
    image_placeholder.pack(pady=(0, 10))

    entry = tk.Entry(container, width=30, font=("Arial", 11), highlightthickness=1, highlightbackground="black")
    entry.pack()

    container.pack(side=tk.LEFT, padx=30)

for _ in range(3):
    create_image_input(image_input_frame)

bottom_frame = tk.Frame(root, bg="white")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)

tick_label = tk.Label(
    bottom_frame,
    text="",
    font=("Arial", 16),
    bg="white"
)
tick_label.pack()

progress_label = tk.Label(
    bottom_frame,
    text="0% completed",
    bg="#333",
    fg="white",
    font=("Arial", 10, "bold"),
    width=15,
    pady=5
)
progress_label.place(x=85, y=0)

progress = ttk.Progressbar(
    bottom_frame,
    orient="horizontal",
    length=800,
    mode="determinate"
)
progress["value"] = 0
progress.pack(pady=25)

def refresh_frame():
    global counter
    progress_label.config(text=f"{counter}% completed")
    progress["value"] = counter % 101
    counter += 1
    root.after(100, refresh_frame)

refresh_frame()
root.mainloop()
