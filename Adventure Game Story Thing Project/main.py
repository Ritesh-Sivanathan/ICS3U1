'''
Name: Ritesh Sivanathan
Date: 3/1/2025
Description: (below)

--- Assignment --- 

My code includes:
- Decision structures
- Boolean expressions
- Repetition structures
- Conditonal Loops
- Counter loops
- Variables, Input Statements, Print Statements, Different datatypes, Decision and Repetition structures
- Uses common coding conventions (camel case and underscores for variables, default indenting, modularization of different functions)

--- Story ---

Inspired by John Grisham's `The Firm`, `The King of Torts` and a little bit of `The Broker`

A lawyer finds damning evidence against a large pharmaceutical company. Before he can litigate, he is approached by a corporate fixer, 
who offers him a bribe. His entire life is at risk no matter what choice he makes

There are 5 possible outcomes
- Accepts Bribe + Survives Attacks
- Accepts Bribe + Doesn't Surive Attacks (dies or goes to prison)
- Declines Bribe + Successfully takes down the pharmaceutical
- Declines Bribe + Fails to take the pharmaceutical down and is countersued for everything
- Declies Bribe + Runs away to another country 

--- Dependencies ---

Python 3.11

Dependencies:
- pandas (latest version) `pip install pandas`
- colorama (latest version) `pip install colorama`
- matplotlib (latest version) `pip install matplotlib`
- numpy (latest version) `pip install numpy`
- tabulate (latest version) - `pip install tabulate`

RUN THIS EXACT COMMAND TO INSTALL ALL DEPENDENCIES:

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

# Configs

DEVELOPMENT_ENV = True # removes delays and other aesthetic/visual features
LIGHTWEIGHT = True # Removes all assets / external depedencies (images and CSV)

init(autoreset=True) # This is for Colorama's initial configuration

# -------------------------------------------------------------------------


class Format: # Custom formatting class to make inserting ANSI codes easier
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'

class Player:

    def __init__(self, RISK, REPUTATION):
        self.networth = 423512
        self.risk = RISK
        self.reputation = REPUTATION

    def userStats(self):
        
        properties = {'Networth': f'${self.networth}', 'Reputation': self.reputation, 'Risk': f'{self.risk}%'}
        
        print('\n\n' + Format.BOLD + Format.UNDERLINE + "Stats:")

        for key, value in properties.items():
            print(f"{Fore.GREEN + key}: {Format.BOLD + str(value)}")

supiciousData = ('''
        +----+-----------+------------------------+--------------------------------------------------------+------------+
        |    |        ID | Type                   | Description                                            | Date       |
        +====+===========+========================+========================================================+============+
        |  0 | 255431235 | Financial Transaction  | Large sum wired from offshore account to a law firm    | 2003-01-15 |
        +----+-----------+------------------------+--------------------------------------------------------+------------+
        |  1 | 220004129 | Email Leak             | Internal memo discussing 'silencing' a whistleblower.  | 2003-02-03 |
        +----+-----------+------------------------+--------------------------------------------------------+------------+
        |  2 | 268664138 | Forensic Report        | Tampered drug trial results uncovered.                 | 2003-02-17 |
        +----+-----------+------------------------+--------------------------------------------------------+------------+
        |  3 | 299834652 | Surveillance Footage   | Unmarked black SUV tailing key witness.                | 2003-03-01 |
        +----+-----------+------------------------+--------------------------------------------------------+------------+
        |  4 | 250963847 | Bank Statement         | Unusual withdrawals made by company executives.        | 2003-03-10 |
        +----+-----------+------------------------+--------------------------------------------------------+------------+
        |  5 | 218189729 | Confidential Testimony | Former employee reveals cover-up tactics.              | 2003-03-15 |
        +----+-----------+------------------------+--------------------------------------------------------+------------+
        |  6 | 259108233 | Internal Document      | Handwritten notes indicating bribery scheme.           | 2003-03-22 |
        +----+-----------+------------------------+--------------------------------------------------------+------------+
        |  7 | 262767883 | Phone Call Recording   | Threatening call to journalist investigating case.     | 2003-03-27 |
        +----+-----------+------------------------+--------------------------------------------------------+------------+
        |  8 | 223639945 | Legal Contract         | Shady settlement agreement signed under duress.        | 2003-04-02 |
        +----+-----------+------------------------+--------------------------------------------------------+------------+
        |  9 | 247701633 | Lab Report             | Evidence of manipulated test results for FDA approval. | 2003-04-10 |
        +----+-----------+------------------------+--------------------------------------------------------+------------+
''')

asciiPorsche = '''
@@@(@@&&#(@@%%*@&@&(&@@&@@@@@(&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&/@(@&&#/@*&%&&@(&,& @,.@&&#,/*
@%%@@@@*@/&@@#*#&&&&&&%%&&*%&&&#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%& (@@&,@,**%((,  ,*#*(#
#*%%@@@@*/,..%@&&&&&(#&&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%&&(%&&&@,@@&(&%%&%&&(@&&..@ #*&@&%&*,/
%#&@%@/&@,@&@&%%&&#%@&&&,&@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@/&&&&&&&&*&*&@&&&@&/@@*&&&.%@@*&(#((,,
&&@*@ ((@(%@@@#,@%@,,#(#(@&&&&&&&&@@@@@@&&&&&&&&&&&&%&.@&&&&&&&&%#&&&%&,&&#@&&&&&&&&&&&&&&&&&&&*@/,%
@#@%( @,@*#.*/.&&#@@&&&&#&&&&&&&&&&&&&&&*&&&&%&#@&&&&&&&&&&&& #%&*&&&%&#&&&@(&&#&&& &.&&&&&@.& /&.,&
*/%%&*(/##,/@#(#&&#*%.,&&&&&&&&&(&&%&&,(/,%&%&&&&&&&&&&&&&%%%&&&&/%.%&/&*@*&&&&&&&&&.@&&,&&&&&&*&,*,
&*&#,#%%&@*&%&/%,,*,/**&*/%&&%%&/&##/%,*.,*,*.*(%&/&&&&&&.&&%&&,.% &&&@&.&&&&%#%&%%%%%%#/%*,,,@*#/*,
##/*(/,.* ,,,***#(/,.,,,/&%&/./##(%/(/..*,,,.#%,/*&(/*(,/&&( ,%/%& (##%#/(%& ,*,,&&&&&&&&&&&*.*,,.//
//(%*//,(*/,%*,,.,*./.((/*,*,.., % */*..,,,,,. ,,****%#((((((((((/%/###&%,(&.&/&(%%.#&.,.(/(.. (,//*
*(#*,/**/..,,, ,..,..,.*,,. ...* .,./ .,(.*,*, %%%#%#####(##(((((#(*,##%.*,#/*.*((/%.(**., *./.,,.,,
,/.,,,(((,*,, /(*/    *,, ,....,**,,,**..,,.%%%#####((#(((((((%&(*(,(#,   %%%%,*****,,..(*,*,,.,...*
 ,(*...,.,*/,*.,..,*.,.,  *,, %#(,,/,,,.*/,*#%%%%#######(#(/***/#%*,  /..... ...,.**,/*.,.,   ,.,, .
,,*.,*/,*,.,, ,,.,*/,/,,(*.&@((*%#%###(%%##########/%#(/*/#/////.  ,....   . ., *(,*/*,*.. *.**.***.
.   .*.. ,,**(/*/**,.*,*#%@#%%/##((#########((##****.* . ,,,,..*,..  /,(*/*///*(/*/,,**##
&&%%&%&&&&&%&&%%%%%%%%&&#(%#%##########(##((#(((((@&& (///**...    , ,,,,,*...  ,/(((((#*##(##.#####
####@#####(##((((#(###%%################((((((((####(((//**.., .   . ,,*,..,   .**////(/(/@@((((/(((
####(##(@#((#(###(#(#*,,*##/%(##.#%&@&&%%#@%/.,/#((   ,.....,,     ,....  .,,/*///////(//@&#//((((((
(##((###(#(((########,    ..,,.. ,,,,,,         *   . ........   . . ..,.,/(/////((//((@&(&/((((/(#(
###((##(#####((((#%(#%,. ,             ,.*         .....,.,.,.      */*,*//*/(///((/((&%*#(((//#/(#(
###%#((((/(#@&###((#(/,,,...** **%%,*//*&#%*.%%%%%##,,,......       /*/////((///((((/@@@%*//////(/(/
##(/@@((((#/#%#%(##(##/**..*/(*///**/,.,,..,,,,,,          .,,,**,,(((((((/(((/((//&@.@#//#(///(/*/(
(((#(#(##((#/##(((/%((/(***,*.,... . .  .    ... . ,.,,,.*/*/,,*#(/((%%((##(((/(((%@@##/((///(((*(/(
%#/(*(##/(//(//((%/(#/*((#/#/((//*((///#/**((*(/(//#(/(*#/,((/(((/((%(//#((#*//((&&@//*(/(#//(/*/(*(
((//(#((##/%(%*##/((%#(((#%%#//((/%//##((#((%((/%#%#(,*#(%(%%/#(((%%(#(/#/(///#/@&%#(//(///#(/////(/
((#/%*#(%//%%(%%#&#%(&/*%##((###(///%/(##((/#&***,*@&(**(##(#((#(**(#%((#/#((/#&&/*%%(#(/(**(/(/(,/(
(,(,(%#/%%%%##/(#((###,*(*/(%(&%(%/##((#,//##%(%((////##//####((/(#/(/(#/#*(/#@&@&*,*,//(*//(*//(*((
*/*(/,/%#(((&##(%%###(/((/(*(%%(*&*,(#/(##(###%#**#(%%#&##//#((%*##%/#(/%(//@&&@@*,**(/(/#%/////(/(/
(&%##*,(#//,(#***(#%((###(/#/**%*%/##%#%%(%#/#***#@##(&((/%##/(/#(((&(((/##&@&&%/(,*#/((////,,/#/*(/
(##(/((**(*//**%%(/%###%(/*(//%/(%#/(#%#&#(/*#**#@(&###(#*(((#(/#(//**//#,@@&*(,,/(//(*(/*#(////*///

'''

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

    for i in range(1,101): # Loading percentage, a range of 1-100
        print(f"{i}%", end=" ")
        print("Loaded")
        time.sleep(0.05*i*(np.random.uniform(0,0.05)))
        if i != 100:
            utils.delete_last_line()
    
    print('\n')

if not DEVELOPMENT_ENV:
    loader() # first function called so loading actually works

newPlayer = Player(5, 20)

def intro():

    utils.type_text("\nMoultrie Courthouse, Washington D.C - May 6th, 2003 | 3:03 PM\n", color=Fore.RED)
    utils.type_text("\nThe courtroom hums with quiet chatter as you sit behind your desk, flipping through the case files.")
    utils.type_text("\nThe name of the defendant, a former researcher at Vindex Pharmaceuticals, glares at you from the page.")
    utils.type_text("\nThe evidence is damning, yet something doesn't sit right. Witness testimonies contradict, documents appear altered, and an anonymous source has hinted at something much bigger.")
    
    utils.type_text("\n\nYou look over the activity summary of Vindex that you drafted yesterday.\n")
    
    if not DEVELOPMENT_ENV: # skip the timer for development environments
        for i in range(3, 0, -1):
            utils.type_text(f"Data showing in {i}\n", color=Fore.MAGENTA)
            time.sleep(1)

    if not LIGHTWEIGHT:
        suspiciousEvidence = pd.read_csv('./assets/suspicious_evidence.csv')

    print('\n' + '-' * 20 + '\n')
     
    if LIGHTWEIGHT: 
        print(supiciousData)
    else:
        table_str = tabulate(suspiciousEvidence, headers=suspiciousEvidence.columns, tablefmt="grid")
        print(table_str)

    print('\n' + '-' * 20)
    
    utils.type_text("Read the data!\n")
    if not DEVELOPMENT_ENV:
        for i in range(15, 0,-1):
            print(i)
            time.sleep(1)
            utils.delete_last_line()

    utils.type_text("\n\"Mr.Carter!\". You look up to everyone in the courtroom staring at you. You ask for a postponement of the hearing to review evidence, and the judge approves.\n")
    utils.type_text("\nLater that night, a shadowy figure steps into your office. Dressed in a sharp suit, he slides a briefcase across your desk and makes an offer to drop the case and forget about all of this.\n\n", color=Fore.RED)
    
    choice = input(Fore.YELLOW + Format.BOLD + "Do you accept the bribe? (yes/no): ").strip().lower()
    
    if choice == 'yes':
        accept_bribe()
    elif choice == 'no':
        reject_bribe()
    else:
        utils.type_text("Invalid choice. Try again.", color=Fore.RED)
        intro()

def accept_bribe(): # Storyline 1

    utils.type_text("\nYour fingers tighten around the briefcase handle as you weigh the consequences.\n")
    utils.type_text("It's more money than you've ever seen in your life. A way out. A fresh start.\n")
    utils.type_text("You sign the settlement, and within days, the case is buried\n")

    utils.type_text("\nYou still need to cover your tracks. While reviewing your documents, you find these pieces of potentially identifying material. Remove the ones you think can personally identify you and leave the rest (as to not arouse suspicion).\n\n")

    personal_info = [
        {"id": 1, "name": "Full name", "need_to_remove": True},
        {"id": 2, "name": "Social security number", "need_to_remove": True},
        {"id": 3, "name": "Bank account number", "need_to_remove": True},
        {"id": 4, "name": "Passport number", "need_to_remove": True},
        {"id": 5, "name": "Credit card details", "need_to_remove": True},
        {"id": 6, "name": "Favorite color", "need_to_remove": False},
        {"id": 7, "name": "Shoe size", "need_to_remove": False},
        {"id": 8, "name": "Preferred vacation destination", "need_to_remove": False},
        {"id": 9, "name": "Hobbies", "need_to_remove": False},
        {"id": 10, "name": "Sports team preference", "need_to_remove": False}
    ]

    random.shuffle(personal_info) # Make it a bit more fun by randomly shuffling the dictionary every time

    if not DEVELOPMENT_ENV:

        removals = [1,2,3,4,5] # Keep these to track the ones the user hasn't removed so we can easily print it if they fail

        for info in personal_info: # Iterate through every object in the dictionary
            utils.type_text(f'ID: {info["id"]} Name: {info["name"]}\n', color=Fore.RED)

        number_to_remove = int(input("\nHow many pieces of IDENTIFYING evidence do you think you have to remove to be well covered without completely wiping all the data?: "))

        utils.type_text("\nEnter the IDs of the pieces of evidence you think should be removed\n", color=Fore.YELLOW)

        for i in range(number_to_remove): # Iterate through the user provided input

            input_id = int(input(f"ID of the article to be removed ({(i+1)}/{number_to_remove}): "))
            
            if input_id in removals:
                removals.pop(removals.index(input_id))
            else:
                utils.type_text("You removed the wrong piece of evidence! Someone caught on and exposed you!")
                game_over()

        if (len(removals) > 0):
            utils.type_text(f"You failed to remove the identifying pieces of evidence! You got exposed because your `{personal_info[removals[-1]]['name']}` was in a document. You make {len(removals)} mistakes!" )
            utils.type_text(f"\n\n{len(removals)} mistakes!!!", color=Fore.RED, bold=True)
            game_over()

        utils.type_text("\nYou successfully remove any connection between you and this bribe.\n", color=Fore.GREEN)
    utils.type_text("\nYour career soars, promotions come fast, and soon you find yourself in the upper echelons of the legal world.")
    
    newPlayer.networth += 3000000
    newPlayer.reputation += 50
    newPlayer.risk += 83

    # utils.print_normal_text("\nPlayer Stats", underline=True, bold=True)

    newPlayer.userStats()
    

    print("-"*20)

    utils.type_text("\nBut secrets don't stay buried forever.\n")
    
    events = [
        "A journalist starts investigating your early cases...",
        "Your partner finds something in your files and asks questions...",
        "The FBI receives an anonymous tip about illicit financial transactions..."
    ]
    
    shown_success_msg = False
    
    random.shuffle(events)
    
    for event in events:

        random_payment = np.random.randint(10000, 625000)
        newPlayer.networth += random_payment
        
        utils.type_text('\n' + event, color=Fore.MAGENTA)
        time.sleep(1)
        decision = input(Fore.YELLOW + "\nDo you cover it up or confess? (cover/confess): ").strip().lower()

        if decision == 'cover':
            
            utils.type_text("You manipulate evidence, silence witnesses, and keep your empire intact for now.")
            utils.type_text(f"\n\n+${random_payment} - Monthly Personal Profits", color=Fore.GREEN)

            newPlayer.userStats()

            if not shown_success_msg:
                utils.type_text("\nYou notice people getting more distant. More suspicious of you. You brush it off as paranoia, but deep down you know something big is on the horizon.\n")
            
            if (not shown_success_msg):
                
                utils.type_text("\nYou're still making millions, though.", color=Fore.GREEN)
                utils.type_text("\nYou've purchased a few new toys, a downtown condo and have your own law firm.\n")
                
                time.sleep(2)

                if not DEVELOPMENT_ENV and not LIGHTWEIGHT:
                    utils.display_image('./assets/porsche.jpg', title="New Car")
                    utils.display_image('./assets/condo.jpg', title="Luxury Condo - Downtown D.C")
                    utils.display_image('./assets/watches.jpg', title="Watch collection")
                    utils.type_text("Life is great.")
                elif LIGHTWEIGHT:
                    utils.type_text("\nPicture of your brand new Sports Car\n", color=Fore.CYAN)
                    print(asciiPorsche)

                time.sleep(2)
                
                utils.type_text("\nYou reflect on how your life went from barely surviving in a run down apartment in the worst part of D.C to becoming 'the Wolf of K Street'\n")
                
                shown_success_msg = True

        elif decision == 'confess':

            random_low_networth = np.random.randint(0, 185000)
            
            utils.type_text("\nThe weight of your sins is too much. You come clean in an interview, exposing everything.", color=Fore.RED)
            utils.type_text("\nWithin days, warrants are issued for your arrest. BAM! The feds kick your doors down, and the gavel falls. You're sentenced to federal prison.")
            
            newPlayer.networth = random_low_networth
            newPlayer.reputation = -12
            newPlayer.risk = 15

            game_over()

        else:
            utils.type_text("Invalid choice. Defaulting to cover-up.\n", color=Fore.RED)
    
    FBI_Finds_Out() # runs after all the events (unless game ends)

def reject_bribe(): # Storyline 2

    utils.type_text("Your jaw tightens. You push the briefcase back across the desk.", color=Fore.RED)
    utils.type_text("\n\nThe fixer smirks. ‘You'll regret this,' he says before disappearing into the night.")
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
            utils.type_text("\nYou hold a press conference, exposing the corruption. The world watches.\n", color=Fore.GREEN)
            utils.type_text("But the company fights back with every tool at their disposal. \nThey paint you as a fraud, fabricate evidence, and soon, an arrest warrant is issued—against you.")
            utils.type_text("\nWith nowhere left to run, you must decide: flee or fight?\n\n")
            final_decision = input(Fore.YELLOW + "Do you flee the country or fight the case in court? (flee/fight): ").strip().lower()

            if final_decision == 'flee':

                utils.type_text("\nYou disappear under a new identity, living in exile.\n", color=Fore.RED)
                utils.type_text("Justice was never served, but at least you're alive with your millions.\n")
                game_over()

            elif final_decision == 'fight':

                utils.type_text("\nYou stand trial. The evidence is overwhelming, but a whistleblower from inside the company testifies on your behalf.", color=Fore.GREEN)
                
                utils.type_text("\nAll you need, the one little piece of evidence to put this company down, is the first date on that suspicious evidence you compiled\n")
                utils.type_text("\nDamn, that was destroyed by the pharmaceutical company. You have to go off memory", color=Fore.RED)

                date = input("\nWhat was the first date listed on that suspicious evidence? (yyyy-mm-dd or Month Date Year): ")
                
                if (date == "2003-01-15" or date.lower().strip() == "january 15 2003"):
                    utils.type_text("\nThe courtroom erupts as the truth finally comes out. You win, although at a heavy cost.")
                    utils.type_text("\nVindex Pharmaceuticals has been ordered to pay your clients a settlement of $150,000,000, with a 25% fee, of which $20M is going straight to your bank account.")
                    utils.type_text("\nThe case makes history, but the danger never truly leaves you.\n")
                    game_over(win=True)

                else:
                    utils.type_text("\nYou fail to recall the correct date and can't find the evidence in time. The judge rules in the company's favour and you are forced to pay restitution to the amount of $3,000,000,\n for slander, malicious prosecution and a dozen other civil claims that will sink both your finances and reputation.")
                    newPlayer.networth -= 3600000
                    print(f"Networth: {newPlayer.networth}")
                    game_over()


        elif decision == 'quiet':
            utils.type_text("\nYou lay low, hoping the storm passes. But it doesn't.", color=Fore.BLUE)
            utils.type_text("\nOne night, there's a knock at your door. It's the police.")
            utils.type_text("\nYou are arrested on fabricated charges and thrown into a legal battle you can't win.\n")
            game_over()

        else:
            utils.type_text("Invalid choice. Defaulting to staying quiet.", color=Fore.RED)
            game_over()

def fight_or_flight():

    # CHOICE
    quiet_or_public = input("\nYou are being constantly harrassed by people who you presume are federal law enforcement agents. Do you go public or stay quiet? (public/quiet): ")
    
    if quiet_or_public == "quiet":
        
        utils.type_text("You don't go public with the harrassment out of fear for your life.\n")
        utils.type_text("\nThe harrassment gets worse and one day, as you walk past a dark, D.C alleyway...")
        utils.type_text("POP! POP! POP!", color=Fore.RED, bold=True)

        game_over()

    else: # not elif == "public" because 
        
        utils.type_text("You talk to a reporter at The Washington Post and recount the harrassment by federal law enforement.")
        utils.type_text("\nThe FBI is angered by this, but killing you now would be too obvious. They're scheming and you know it.")

        flee_or_fight = input("Do you flee the country or fight the law on this? (flee/fight): ")
        
        if flee_or_fight == "flee":
            utils.type_text("You catch the next flight out of the U.S. You land in Germany and fly from there to Italy, where you have a citizenship.")
            utils.type_text("You live your life quietly in Bologna with your millions, but still have that feeling like someone is watching you...", color=Fore.RED)
        elif flee_or_fight == "fight":
            utils.type_text("\nYou choose to stay in D.C and fight the law.")
            utils.type_text("\nYou're suddenly awaken in the middle of the night. You check your clock, and see that it's 1:52AM.")
            utils.type_text("\n\"Clay Carter, this is the FBI! We have a warrant for your arrest! \"", color=Fore.RED)
            game_over()
    
    

def FBI_Finds_Out():

    chance = random.randint(1,4)

    utils.type_text("\nAs you are walking to your car from your home, a black Cadillac Escalade pulls up quickly. Two men in suits get out of the car, flash their badges and tell you to hop in.", color=Fore.RED)
    
    # CHOICE
    get_in = input(Fore.YELLOW + "\nDo you get in? (yes/no): ").strip().lower()

    if get_in == "no":

        if chance == 1: # 1/4 chance they let you go
        
            utils.type_text("You don't hop in the car and immediately call your lawyer. The men look frustrated but get back in the car and park just across the street. At least now you know you're being watched.\n")
            fight_or_flight()

        else:

            utils.type_text("\nThe men refuse to let you go, citing they're with federal law enforcement and that you have to go with them.\n")
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
    
    utils.type_text("\n\nIn the quiet of an empty conference room deep in the FBI Headquarters, a team of field agents, lead by the Executive Assistant Director of the head office meet you.")
    utils.type_text("\nAfter a few moments of silence, the AD breaks the silence. \"We know what you've done.\"")
    utils.type_text("\nYou stay calm because you know you've covered your tracks well.")
    utils.type_text("\n\"If you confess to all your crimes now, we can offer you protective custody at the best white collar prison in the country as well as a reduced sentence.\"")

    # CHOICE
    offer = input(Fore.RED + "\n\nDo you take the bait and accept the deal or do you decline? (accept/decline): ")

    if offer.strip().lower() == "accept":
    
        utils.type_text("\nYou confess to all your crimes, the bribery, malpractice and everything in between.", color=Fore.LIGHTRED_EX)
        utils.type_text("\nThe AD smiles, nods to the field agents, and exits the room without a word.", color=Fore.LIGHTRED_EX)
        utils.type_text("\nYou're promptly handcuffed by the agents and taken to an in-house jail, where you will wait until your trial starts.", color=Fore.LIGHTRED_EX)
        
        game_over()

    else:

        utils.type_text("\n\"Alright, Mr.Carter, just know that we're coming after you whether you choose to confess or not. You'd better watch your back. Get him out of here.\"\n")
        utils.type_text("The field agents drag you out of the building and you're left to catch a cab home.\n\n")
        
        # CHOICE
        call_lawyer = (input(Fore.YELLOW + "Once you get home, do you call your lawyer, or ignore what happened? (lawyer/ignore): "))

        if call_lawyer.strip().lower() == "lawyer":
            
            utils.type_text("You immediately call your lawyer, who is enraged by the fact that the FBI pulled you into their building without him present.")
            utils.type_text("\nHe schedules a meeting with a prominent journalist for tomorrow to publicize this information.")
        
            # CHOICE
            publicize_or_not = input('\n' + Fore.YELLOW + "Do you want to go public? (yes/no): ")
            
            if publicize_or_not.strip().lower() == "yes":

                utils.type_text("\nMultiple groups whose sole purpose is to kill you catch wind that you're headed to a \"secret\" meeting with a journalist. They don't know who's being targeted so they all \nwant you dead\n")
                utils.type_text("As you wait at a traffic light, just a few blocks from the journal's office, you hear a car's tires screech behind you\n")
                utils.type_text("Suddenly, everything goes black. ", color=Fore.RED)
                game_over()
            
            else: 

                utils.type_text("\nYou decide not to go public with the FBI's harassment.\n")
                utils.type_text("Maybe it's paranoia, but you feel like someone's watching you everywhere you go.\n")
                utils.type_text("You start noticing small things: your car parked slightly differently than you left it, a black SUV idling near your office, and your phone acting strangely.\n")
                
                utils.type_text("\nThen, one night, you're jolted awake by a loud noise outside your apartment...\n")
                
                time.sleep(3)
                utils.type_text("You cautiously peek through the blinds. The SUV is still there, engine running.\n", color=Fore.RED)

                time.sleep(2)
                utils.type_text("\nA text message suddenly appears on your phone from an unknown number: 'You should have taken the deal.'\n", color=Fore.RED, bold=True)

                action = input(Fore.YELLOW + "Do you leave the city immediately or stay put? (leave/stay): ").strip().lower()

                if action == "leave":
                    utils.type_text("\nYou grab your essentials, book a last-minute flight, and disappear from Washington D.C.\n")
                    utils.type_text("A month later, you're living in an undisclosed location, but you know they'll never stop looking for you...\n")
                    game_over()

                else:
                    utils.type_text("\nYou decide to stay and act like nothing happened.\n")
                    utils.type_text("That's when they make their move.\n")
                    utils.type_text("The next morning, as you step out of your apartment, a van screeches to a stop in front of you.\n")
                    utils.type_text("Men in tactical gear jump out. Before you can react, a black bag is thrown over your head.\n", color=Fore.RED, bold=True)

                    game_over()
            
        else:

            utils.type_text("\nYou decide not to tell your lawyer. Maybe if you ignore it, it'll go away.\n")
            utils.type_text("Days pass. Nothing happens. No calls, no visits, no threats. Maybe you were just being paranoid.\n")
            
            utils.type_text("\nThen, one night, you wake up to the sound of your front door creaking open.\n")
            utils.type_text("A shadow moves in the hallway. Your heart pounds.\n")

            hide_or_fight = input(Fore.YELLOW + "\nDo you hide or grab something to defend yourself? (hide/fight): ").strip().lower()

            if hide_or_fight == "hide":
                
                utils.type_text("\nYou slip into your closet, barely breathing. Heavy footsteps echo in your apartment.\n")
                utils.type_text("A flashlight beam sweeps across the room. Then, silence. Minutes pass. Finally, the intruder leaves.\n")
                utils.type_text("When you check your desk, your documents and laptop are gone. Someone wanted something. And they got it.\n")
                utils.type_text("You're in deeper than you thought...\n")

                game_over()

            elif hide_or_fight == "fight":
                utils.type_text("\nGrabbing a heavy lamp, you creep into the hallway. The moment the intruder steps into view, you swing.\n")
                utils.type_text("CRACK. He drops, but he's not alone. Another figure rushes in from behind, slamming something against your head.\n")
                utils.type_text("Everything fades to black...\n")
                game_over()

            else:
                utils.type_text("\nYou freeze, doing nothing. A mistake.\n")
                utils.type_text("The last thing you hear is a gun being cocked.\n", color=Fore.RED)
                game_over()


def game_over(win=False):

    if (win):
        utils.type_text("\nYOU WIN!.\n\n", color=Fore.GREEN, bold=True)
    else:
        utils.type_text("\nGAME OVER.\n\n", color=Fore.RED, bold=True)

    retry = input(Fore.GREEN + "Would you like to try again? (yes/no): ").strip().lower()
    
    if retry == 'yes':
        intro() # Go right back to start (skipping loader)

    else:
        utils.type_text("Thanks for playing!", color=Fore.CYAN, bold=True)
        os.abort() # Kills the current process

if __name__ == "__main__":    
    
    # Try-Catch block here so I can easily capture any KeyboardInterrupts throughout the program

    try:
        intro()
    except KeyboardInterrupt:
        utils.print_normal_text("\nGame Exited. Thanks for playing!\n", color=Fore.RED, bold=True)