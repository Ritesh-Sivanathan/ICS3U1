import numpy as np
import time

class Player:
    def __init__(self, name):
        self.name = name

def staggeredPrint(text: str):
    pass
    
def Customization():

    global currentPlayer
    currentPlayer: Player = Player(str(input("What is the character's name?: ")))

def IntroductoryScene():
    
    print("February 4th, 2003 11:13 AM")
    print("Moultrie Courthouse, Washington D.C")
    
    Customization()
    
    print(f"For the plaintiff, we have {currentPlayer.name} Carter; for the defendant we have Julia Smith. Are we ready to proceed?")
    print(  f"""
            {currentPlayer.name} picks up his case file and reviews it for the first time. 20 year old Rumel Weston. Currently facing 20 years to 
            life for a string of violent burglaries just a week ago. Two people died. Mr.Weston, you are being brought up on 3 charges of burglary, 12 charges of aggravated
            assault and battery as well as two counts of second degree murder. How do you plead? {currentPlayer.name} takes his eyes off the file. "Not guilty, your honor"
            
            """)
