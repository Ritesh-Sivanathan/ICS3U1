'''
Name: Ritesh Sivanathan
Date: 3/1/2025
Description: (below)

--- Story ---

Inspired by John Grisham's `The Firm` and The `King of Torts`

A lawyer finds damning evidence against a large pharmaceutical company. Before he can litigate, he is approached by a corporate fixer, 
who offers him a bribe. His entire life is at risk no matter what choice he makes

--- Dependencies ---

Dependencies:
- pandas (latest version) `pip install pandas`
- colorama (latest version) `pip install colorama`
- matplotlib (latest version) `pip install matplotlib`
- numpy (latest version) `pip install numpy`
- tabulate (latest version) - `pip install tabulate`

pip install pandas colorama matplotlib numpy tabulate


'''

# Internal Dependencies

import os
import sys
import time
import random

# External Dependencies

import numpy as np
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from colorama import Fore, Style, init

# -------------------------------------------------------------------------

DEVELOPMENT_ENV = False # removes delays and other aesthetic/visual features

init(autoreset=True)

class Format: # custom formatting class because it's more reliable
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'

class Player:

    def __init__(self, RISK, REPUTATION):
        self.NETWORTH = 423512 
        self.RISK = RISK
        self.REPUTATION = REPUTATION

    def userStats(self):
        
        properties = {'Networth': f'${self.NETWORTH}', 'Reputation': self.REPUTATION, 'Risk': f'{self.RISK}%'}
        
        print('\n' + Format.BOLD + Format.UNDERLINE + "Stats:")

        for key, value in properties.items():
            print(f"{Fore.GREEN + key}: {Format.BOLD + str(value)}")

class utils:

    '''
    
    All utility functions put into a this class (utils) to group them easily. 
    Also improves code readability

    '''

    def delete_last_line(): # call this function in a for loop to delete x amount of lines
        sys.stdout.write("\033[F") # move cursor up
        sys.stdout.write("\033[K") # delete line
    
    def display_image(path, title=""):
    
        img = mpimg.imread(path)
        imgplot = plt.imshow(img)

        plt.xticks([])  
        plt.yticks([]) 
        plt.title(title)

        plt.show()
    
    def type_text(text: str, delay=(0.00 if DEVELOPMENT_ENV else 0.15), color=Fore.WHITE, bold=False, underline=False):

        for char in text:
            print(color + (Format.BOLD if bold else '') + (Format.UNDERLINE if underline else '') + char + Style.RESET_ALL, end='', flush=True) # bold and color options
            time.sleep(np.random.uniform(0,delay) if not DEVELOPMENT_ENV else 0) # Adds a bit of randomness to the delay
    
    def print_normal_text(text: str, color=Fore.WHITE, bold=False, underline=False): # This function lets us easily print (non slow) text with Colorama options avoiding the weird inline text formatting (Format.BOLD + Fore.RED + text)
        print(color + (Format.BOLD if bold else "") + (Format.UNDERLINE if underline else "") + text)

def loader():

    print('\n' + Fore.CYAN + Format.BOLD + "The Whistleblower", end="- ")
    print("A legal thriller\n")
    print('*'*50)

    for i in range(1,101): # loading percentage
        print(f"{i}%", end=" ")
        print("Loaded")
        time.sleep(0.05*i*(np.random.uniform(0,0.05)))
        if i != 100:
            utils.delete_last_line()
    
    print('*'*50)
    print('\n')

if not DEVELOPMENT_ENV:
    loader() # first function called so loading actually works

newPlayer = Player(5, 20)

def intro():

    utils.type_text("\nMoultrie Courthouse, Washington D.C - 3:03 PM\n", color=Fore.RED)
    utils.type_text("\nThe courtroom hums with quiet chatter as you sit behind your desk, flipping through the case files.")
    utils.type_text("\nThe name of the defendant, a former researcher at Vindex Pharmaceuticals, glares at you from the page.")
    utils.type_text("\nThe evidence is damning, yet something doesn’t sit right. Witness testimonies contradict, documents appear altered, and an anonymous source has hinted at something much bigger.")
    
    utils.type_text("\nYou look over the activity summary of Vindex that you drafted yesterday.\n")
    
    for i in range(3, 0, -1):
        utils.type_text(f"Data showing in {i}", color=Fore.MAGENTA)
        time.sleep(1)

    suspiciousEvidence = pd.read_csv('./suspicious_evidence.csv')
        
    print('\n' + '-' * 20 + '\n')
        
    table_str = tabulate(suspiciousEvidence, headers=suspiciousEvidence.columns, tablefmt="grid")
    print(table_str) 

    print('\n' + '-' * 20)
    
    utils.type_text("Read the data!\n")
    
    if not DEVELOPMENT_ENV:
        for i in range(15,1,-1):
            print(i)
            time.sleep(1)
            utils.delete_last_line()

    utils.type_text("\n\"Mr.Carter!\". You look up to everyone in the courtroom staring at you. You request for a postponement of the hearing to review evidence, and the judge approves.\n")
    utils.type_text("Later that night, a shadowy figure steps into your office. Dressed in a sharp suit, he slides a briefcase across your desk and makes an offer to drop the case and forget about all of this.\n", color=Fore.RED)
    
    choice = input(Fore.YELLOW + Format.BOLD + "Do you accept the bribe? (yes/no): ").strip().lower()
    
    if choice == 'yes':
        accept_bribe()
    elif choice == 'no':
        reject_bribe()
    else:
        utils.type_text("Invalid choice. Try again.", color=Fore.RED)
        intro()

def accept_bribe():

    utils.type_text("\nYour fingers tighten around the briefcase handle as you weigh the consequences.\n")
    utils.type_text("It’s more money than you’ve ever seen in your life. A way out. A fresh start.\n")
    utils.type_text("You sign the settlement, and within days, the case is buried\n")
    utils.type_text("Your career soars, promotions come fast, and soon you find yourself in the upper echelons of the legal world.")
    
    newPlayer.NETWORTH += 3000000
    newPlayer.REPUTATION += 50
    newPlayer.RISK += 83

    # utils.print_normal_text("\nPlayer Stats", underline=True, bold=True)

    newPlayer.userStats()
    

    print("-"*20)

    utils.type_text("\nBut secrets don’t stay buried forever.\n")
    
    events = [
        "A journalist starts investigating your early cases...",
        "Your partner finds something in your files and asks questions...",
        "The FBI receives an anonymous tip about illicit financial transactions..."
    ]
    
    shown_success_msg = False
    
    random.shuffle(events)
    
    for event in events:

        random_payment = np.random.randint(10000, 625000)
        newPlayer.NETWORTH += random_payment
        
        utils.type_text('\n' + event, color=Fore.MAGENTA)
        time.sleep(1)
        decision = input(Fore.YELLOW + "\nDo you cover it up or confess? (cover/confess): ").strip().lower()

        if decision == 'cover':
            
            utils.type_text("You manipulate evidence, silence witnesses, and keep your empire intact for now.")
            utils.type_text(f"\n+${random_payment} - Payment for Legal work\n", color=Fore.GREEN)

            newPlayer.userStats()

            if not shown_success_msg:
                utils.type_text("You notice people getting more distant. More suspicious of you. You brush it off as paranoia, but deep down you know something big is on the horizon.")
            
            if (not shown_success_msg):
                
                utils.type_text("\nYou're still making millions, though.", color=Fore.GREEN)
                utils.type_text("\nYou've purchased a few new toys, a downtown condo and have your own law firm. Life is great.")
                
                if not DEVELOPMENT_ENV:
                    utils.display_image('porsche.jpg', title="New Car")
                    utils.display_image('condo.jpg', title="Luxury Condo - Downtown D.C")
                    utils.display_image('watches.jpg', title="Watch collection")
                
                utils.type_text("\nYou reflect on how your life went from barely surviving in a run down apartment in the worst area of D.C to becoming the Wolf of K Street ")
                
                shown_success_msg = True

        elif decision == 'confess':

            random_low_networth = np.random.randint(0, 185000)
            
            utils.type_text("\nThe weight of your sins is too much. You come clean in an interview, exposing everything.", color=Fore.RED)
            utils.type_text("Within days, warrants are issued for your arrest. BAM! The feds kick your doors down, and the gavel falls. You’re sentenced to federal prison.")
            
            newPlayer.NETWORTH = random_low_networth

            game_over()

        else:
            utils.type_text("Invalid choice. Defaulting to cover-up.\n", color=Fore.RED)
    
    FBI_Finds_Out() # runs after all the events (unless game ends)

def reject_bribe():
    utils.type_text("Your jaw tightens. You push the briefcase back across the desk.", color=Fore.RED)
    utils.type_text("\nThe fixer smirks. ‘You’ll regret this,’ he says before disappearing into the night.")
    utils.type_text("\nDays later, your world starts unraveling.")
    utils.type_text("\nThe pharmaceutical company hires an army of lawyers to crush your case. Your credibility is questioned. Your bank accounts are frozen. Your loved ones receive threats.")
    
    events = [
        "You notice a black SUV following you home...",
        "Your house is ransacked, files stolen...",
        "An FBI agent reaches out, saying you might be in danger..."
    ]
    
    random.shuffle(events)
    
    for event in events:

        print('\n\n')
        utils.type_text(event, color=Fore.MAGENTA)
        
        time.sleep(1)
        
        print('\n')
        decision = input(Fore.YELLOW + "Do you go public or stay quiet? (public/quiet): ").strip().lower()
        
        if decision == 'public':
            utils.type_text("You hold a press conference, exposing the corruption. The world watches.", color=Fore.GREEN)
            utils.type_text("But the company fights back with every tool at their disposal. They paint you as a fraud, fabricate evidence, and soon, an arrest warrant is issued—against you.")
            utils.type_text("With nowhere left to run, you must decide: flee or fight?")
            final_decision = input(Fore.YELLOW + "Do you flee the country or fight the case in court? (flee/fight): ").strip().lower()

            if final_decision == 'flee':
                utils.type_text("\nYou disappear under a new identity, living in exile.", color=Fore.RED)
                utils.type_text("Justice was never served, but at least you’re alive with your millions.")
                game_over()
            elif final_decision == 'fight':
                utils.type_text(Fore.GREEN + "You stand trial. The evidence is overwhelming, but a whistleblower from inside the company testifies on your behalf.")
                
                utils.type_text("All you need, the one little piece of evidence to put this company down is the first date on that suspicious evidence you compiled")
                utils.type_text("Damn, that was destroyed by the pharmaceutical company. You have to go off memory", color=Fore.RED)

                date = input("\nWhat was the first date listed on that suspicious evidence? (yyyy-mm-dd or Month Date Year)")
                
                if (date == "2003-01-15" or date.lower().strip() == "january 15 2003"):
                    utils.type_text("The courtroom erupts as the truth finally comes out. You win—at a heavy cost.")
                    utils.type_text("Vindex Pharmaceuticals has been ordered to pay your clients a settlement of $150,000,000, with a 25% fee, of which $20M is going straight to your bank account.")
                    utils.type_text("The case makes history, but the danger never truly leaves you.")
                
                else:
                    utils.type_text("You fail to recall the correct date and can't find the evidence in time. The judge rules in the company's favour and you are forced to pay restitution to the amount of $3,000,000, for slander, malicious prosecution and a dozen other civil claims that will sink both your finances and reputation.")
                    newPlayer.NETWORTH -= 3600000
                    print(f"Networth: {newPlayer.NETWORTH}")
                    game_over()


        elif decision == 'quiet':
            utils.type_text("You lay low, hoping the storm passes. But it doesn’t.", color=Fore.BLUE)
            utils.type_text("One night, there’s a knock at your door. It’s the police.")
            utils.type_text("You are arrested on fabricated charges and thrown into a legal battle you can’t win.")
            game_over()

        else:
            utils.type_text("Invalid choice. Defaulting to staying quiet.", color=Fore.RED)
            game_over()

def fight_or_flight():
    quiet_or_public = input("You are being constantly harrassed by people who you presume are federal law enforcement agents. Do you go public or stay quiet? (public/quiet)")
    
    if quiet_or_public == "quiet":
        utils.type_text("You don't go public with the harrassment out of fear for your life.")
        utils.type_text("The harrassment gets worse and one day, as you walk past a dark D.C alleyway,")
        utils.type_text("POP POP POP", color=Fore.RED)
        game_over()
    elif quiet_or_public == "public":
        utils.type_text("You talk to a reporter at The Washington Post and recount the harrassment by federal law enforement.")
        utils.type_text("The FBI is angered by this, but killing you now would be too obvious. They're scheming and you know it.")
        flee_or_fight = input("Do you flee the country or fight the law on this? (flee/fight)")
        if flee_or_fight == "flee":
            utils.type_text("You catch the next flight out of the U.S. You land in Germany and fly from there to Italy, where you have a citizenship.")
            utils.type_text("You live your life quietly with your millions, but still have that feeling like someone is watching you...", color=Fore.RED)
        elif flee_or_fight == "fight":
            utils.type_text("You choose to stay in D.C and fight the law.")
            utils.type_text("You're suddenly awaken in the middle of the night. You check your clock, and see that it's 3:03AM.")
            utils.type_text("\"This is the FBI. We have a warrant for your arrest. \"", color=Fore.RED)
            game_over()

def FBI_Finds_Out():

    chance = random.randint(1,4)

    utils.type_text("\nAs you are walking to your car from your home, a black Cadillac Escalade pulls up quickly. Two men in suits get out of the car, flash their badges and tell you to hop in.", color=Fore.RED)
    get_in = input(Fore.YELLOW + "\nDo you get in? (yes/no): ").strip().lower()

    if get_in == "no":

        if chance == 1:    
        
            utils.type_text("You don't hop in the car and immediately call your lawyer. The men look frustrated by get back in the car and park just across the street. At least now you know you're being watched.")
            fight_or_flight()

        else:
            utils.type_text("The men refuse to let you go, citing they're with federal law enforcement and that you have to go with them.")
            utils.type_text("You reluctantly get in the car and are taken to an FBI field office just outside of D.C.")
            Interrogation()

    elif get_in == "yes":
        utils.type_text("\nYou get in the car with them and are taken to an FBI field office.")
        Interrogation()
    else:
        print(Fore.RED + "Invalid input. Defaulting to \"yes\"")
        utils.type_text("You get in the car with them and are taken to an FBI field office.")
        Interrogation()

def Interrogation():
    
    utils.type_text("\nIn the quiet of an empty conference room deep in the FBI Headquarters, a team of field agents, lead by the Executive Assistant Director of the head office meet you.")
    utils.type_text("After a few moments of silence, the AD breaks the silence. \"We know what you've done.\"")
    utils.type_text("Your stay calm because you know you've covered you tracks well.")
    utils.type_text("\"If you confess to all your crimes now, we can offer you protective custody at the best white collar prison in the country as well as a reduced sentence.\"")
    offer = input("Do you take the bait and accept the deal or do you decline? (accept/decline): ")

    if offer.strip().lower() == "accept":
    
        utils.type_text("You confess to all your crimes, the bribery, malpractice and everything in between.")
        utils.type_text("The AD smiles, nods to the field agents, and exits the room without a word.")
        utils.type_text("You're promptly handcuffed by the agents and taken to an in-house jail, where you will wait until your trial starts.")
        game_over()

    elif offer.strip() == "decline":
        pass
    
def game_over():

    newPlayer.userStats()

    utils.type_text("\nGAME OVER.", color=Fore.RED, bold=True)
    
    retry = input(Fore.GREEN + "Would you like to try again? (yes/no):").strip().lower()
    
    if retry == 'yes':
        intro()
    else:
        utils.type_text("Thanks for playing!", color=Fore.CYAN, bold=True)
        os.abort()

if __name__ == "__main__":
    
    try:
        intro()
    except KeyboardInterrupt:
        utils.print_normal_text("\nGame Exited. Thanks for playing!\n", color=Fore.RED, bold=True)