'''

Name: Ritesh Sivanathan
Date: 6/5/2025
Description:

Fun airplane identification quiz. Two questions per "slide", one point per correct question. 
Initial load time depends on your internet connection


'''

import tkinter as tk
from tkinter import ttk
from tkinter import * 
from PIL import Image, ImageTk
from info import pre_processed_images, labels
from urllib.request import urlopen
import io

MAX_QUESTIONS = int(len(pre_processed_images)/2) # Setting the number of questions dynamically
IMAGES_PER_QUESTION = 2

# Tkinter configurations

root = tk.Tk()
style = ttk.Style()
root.title("Airplane Identification Quiz")
root.configure(bg="white") # Main window colour

root.resizable(False, False)

# Important Variables

question = 1 # Current question number (not 0-indexed)
score = 0 # number of correct answers

processed_images = [] # Empty array to add the processed PIL objects to
entries = [] # Temporary stack for the current answers the user enters

style.configure("TProgressbar", troughcolor='white', bordercolor='white', background='lightblue', thickness=20) # Progress bar styling

# Loading images with PIL

for image in pre_processed_images:

    response = urlopen(image) # Image is the URL
    img_data = response.read()

    img = Image.open(io.BytesIO(img_data)) # Wrap in BytesIO for PIL to read

    img = img.resize((300, 240), Image.LANCZOS) # Resize the image

    tk_img = ImageTk.PhotoImage(img) # Convert to Tkinter image

    processed_images.append(tk_img) # Add image to processed_images

# Add the first two initial images to the temporary stack
    
stack = processed_images[:IMAGES_PER_QUESTION] # Temporary stack for the current images being displayed

# Submit Button

def handle_next():

    """
    
    This function handles the user clicking the "Next" button.
    It first checks the input the user entered in the Entry elements. If the answers are correct, it increments the score by one for each question.
    
    """
    
    global processed_images, stack, question, score # Making the variables global since we're REASSIGNING its value locally
        
    answer1, answer2 = get_user_input() # get_user_input function handles user input from the Entry elements

    # 

    if question in range(1, int(MAX_QUESTIONS)+1): # Check if the question is a valid number
    
        correct1 = answer1 in labels[question-1][0]  # Check if first answer correct
        correct2 = answer2 in labels[question-1][1]  # Check if second answer correct

        if correct1:
            score += 1
            entries[0].config(bg="lightgreen")  # Mark entry green if correct
        else:
            entries[0].config(bg="salmon")  # Mark red if incorrect

        if correct2:
            score += 1
            entries[1].config(bg="lightgreen")  # Mark entry green if correct
        else:
            entries[1].config(bg="salmon")  # Mark red if incorrect

    if question == (MAX_QUESTIONS + 1): # Handle "Submit" (the end of the quiz)
        button.destroy() # Get rid of the "Next" button
        handle_submit()
        return  # Prevent further execution after submit

    # Wait 800ms to show green/red, then go to next question without freezing UI
    root.after(800, advance_question)


def advance_question():
    global processed_images, stack, question

    if len(processed_images) > 0: # Check length of processed_images just in case. If something happened and the length of the processed_images didn't match up with the number of questions, it won't throw an error here,
        processed_images = processed_images[IMAGES_PER_QUESTION:] # Cut out the last two images from the previous question
        stack = processed_images[0:IMAGES_PER_QUESTION] # Select the next two images to add to the stack
    
    # Header Labels
    

    question_label.config(text=f"Question {question}/{MAX_QUESTIONS}")

    score_label.config(text=f"Score: {score}")

    # Delete the previous entries and load the new images

    entries.clear()
    load_images()

    refresh_frame() # Next slide/frame


def handle_submit():

    """
    
    Handles the click of the last "Next" button.
    Destroys the images from the previous frame. Also destroys the score label so it can be refreshde.
    
    """

    for widget in image_input_frame.winfo_children(): # Destroy images from previous frame
        widget.destroy()
    
    score_label.destroy() # Destroy score label at top of screen

    final_score = tk.Label( # Final score as points
        top_frame,
        text=f"Final Score: {score}",
        font=("Segoe UI", 16, "bold"),
        justify="center",
    )

    percentage_score = tk.Label( # Final score as a Percentage
        middle_frame,
        text=str(f"{int((score/(MAX_QUESTIONS*2))*100)}%"),
        font=("Segoe UI", 20, "bold")
    )

    pass_or_fail = "PASS" # This variable is set to "PASS" and reassigned to "FAIL" if the user fails
    colour = "green" # Same logic as the pass_or_fail variable but changes to "red" on fail
    
    if int((score/(MAX_QUESTIONS*2))*100) < 50: # Checking if user failed
        pass_or_fail = "FAIL"
        colour = "red"

    pass_ = tk.Label( # Using _ at the end because I want this variable to be named pass.
        middle_frame,
        text=pass_or_fail,
        font=("Segoe UI", 20, "bold"),
        fg=colour
    )

    # Pack the Labels

    percentage_score.pack()
    final_score.pack()
    pass_.pack()


# "Next" Button

button = tk.Button(text="Next", justify="center", padx=40, pady=10, bg="lightgreen", relief=FLAT, font=("Segoe UI", 12, 'bold'), command=handle_next)

# Basic frame definitions

"""

Most of the code below is just creating and packing frames and buttons and labels, so too many comments won't be added.

"""

top_frame = tk.Frame(root, bg="black", height=300, pady=25)
top_frame.pack(expand=True, fill=tk.X)

middle_frame = tk.Frame(root, bg="white")
middle_frame.pack(pady=20, expand=True, fill=tk.X)

question_text = tk.Label( # Question Label
    middle_frame,
    text="Identify these aircraft",
    font=("Segoe UI", 14, "bold italic"),
    bg="white",
    justify="left",
)

question_text.pack(pady=(0, 20))

button.pack()

image_input_frame = tk.Frame(middle_frame, bg="white")
image_input_frame.pack()

bottom_frame = tk.Frame(root, bg="white")

# Progress Bar

progress = ttk.Progressbar( # 
    bottom_frame,
    orient="horizontal",
    length=800,
    mode="determinate",
)

progress["value"] = 0 # Setting value of progress
progress.pack(pady=25)

bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)

# Question Header

question_label = tk.Label(
    top_frame,
    text=f"Question {question}/{int(MAX_QUESTIONS)}",
    fg="white",
    bg="black",
    font=("Segoe UI", 16, "bold")
)

question_label.pack()

score_label = tk.Label(
    top_frame,
    text=f"Score: {score}",
    fg="white",
    bg="grey",
    font=("Segoe UI", 16, "bold")
)

score_label.pack()

# Image input function

def create_image_input(parent, img):

    """
    
    Create the image frame and input box

    """
    
    container = tk.Frame(parent, bg="white", bd=1, padx=10, pady=10)
    
    # Images

    image_placeholder = tk.Label(container, image=img, bg="white")
    image_placeholder.pack(pady=(0, 10))

    entry = tk.Entry(container, width=30, font=("Segoe UI", 11), highlightthickness=1, highlightbackground="black") # Input box
    entry.pack()
    entries.append(entry)

    container.pack(side=tk.LEFT, padx=30)

def get_user_input():

    """
    
    Process and return the inputs that the user entered
    
    """

    return ([entry.get().lower().strip().replace("-", "") for entry in entries]) # The formatting converts the letters to lowercase, gets rid of whitespaces and gets rid of any dashes (-)

def load_images():
    
    """
    
    Delete previous image frames and load next two.
    
    """
    
    for widget in image_input_frame.winfo_children(): # Delete the previous images
        widget.destroy()

    for i in range(len(stack)): # Add the images and entry fields
        create_image_input(image_input_frame, stack[i])

load_images()

# Refresh Progress Bar

def refresh_frame():

    global question

    progress["value"] = ((question)/MAX_QUESTIONS) * 100
    question += 1

refresh_frame()
root.mainloop()