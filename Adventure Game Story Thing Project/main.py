import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

def type_text(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    type_text(Fore.CYAN + "Welcome to the Legal Thriller Adventure.")
    type_text("The courtroom hums with quiet chatter as you sit behind your desk, flipping through the case files.")
    type_text("The name of the defendant—a former researcher at Vindex Pharmaceuticals—glares at you from the page.")
    type_text("The evidence is damning, yet something doesn’t sit right. Witness testimonies contradict, documents appear altered, and an anonymous source has hinted at something much bigger.")
    type_text("Then, late one night, a shadowy figure steps into your office. Dressed in a sharp suit, he slides a briefcase across your desk and makes an offer.")
    
    choice = input(Fore.YELLOW + "Do you accept the bribe? (yes/no): ").strip().lower()
    
    if choice == 'yes':
        accept_bribe()
    elif choice == 'no':
        reject_bribe()
    else:
        type_text(Fore.RED + "Invalid choice. Try again.")
        intro()

def accept_bribe():
    type_text(Fore.GREEN + "Your fingers tighten around the briefcase handle as you weigh the consequences.")
    type_text("It’s more money than you’ve ever seen in your life. A way out. A fresh start.")
    type_text("You sign the settlement, and within days, the case is buried. Your career soars, promotions come fast, and soon you find yourself in the upper echelons of the legal world.")
    type_text("But secrets don’t stay buried forever.")
    
    events = [
        "A journalist starts investigating your early cases...",
        "Your partner finds something in your files and asks questions...",
        "The FBI receives an anonymous tip about illicit financial transactions..."
    ]
    random.shuffle(events)
    
    for event in events:
        type_text(Fore.MAGENTA + event)
        time.sleep(1)
        decision = input(Fore.YELLOW + "Do you cover it up or confess? (cover/confess): ").strip().lower()
        if decision == 'cover':
            type_text(Fore.GREEN + "You manipulate evidence, silence witnesses, and keep your empire intact—for now.")
        elif decision == 'confess':
            type_text(Fore.RED + "The weight of your sins is too much. You come clean in an interview, exposing everything.")
            type_text("Within days, warrants are issued for your arrest. The gavel falls. You’re sentenced to federal prison.")
            game_over()
        else:
            type_text(Fore.RED + "Invalid choice. Defaulting to cover-up.")

def reject_bribe():
    type_text(Fore.RED + "Your jaw tightens. You push the briefcase back across the desk.")
    type_text("The fixer smirks. ‘You’ll regret this,’ he says before disappearing into the night.")
    type_text("Days later, your world starts unraveling.")
    type_text("The pharmaceutical company hires an army of lawyers to crush your case. Your credibility is questioned. Your bank accounts are frozen. Your loved ones receive threats.")
    
    events = [
        "You notice a black SUV following you home...",
        "Your house is ransacked, files stolen...",
        "An FBI agent reaches out, saying you might be in danger..."
    ]
    random.shuffle(events)
    
    for event in events:
        type_text(Fore.MAGENTA + event)
        time.sleep(1)
        decision = input(Fore.YELLOW + "Do you go public or stay quiet? (public/quiet): ").strip().lower()
        if decision == 'public':
            type_text(Fore.GREEN + "You hold a press conference, exposing the corruption. The world watches.")
            type_text("But the company fights back with every tool at their disposal. They paint you as a fraud, fabricate evidence, and soon, an arrest warrant is issued—against you.")
            type_text("With nowhere left to run, you must decide: flee or fight?")
            final_decision = input(Fore.YELLOW + "Do you flee the country or fight the case in court? (flee/fight): ").strip().lower()
            if final_decision == 'flee':
                type_text(Fore.RED + "You disappear under a new identity, living in exile.")
                type_text("Justice was never served, but at least you’re alive.")
                game_over()
            elif final_decision == 'fight':
                type_text(Fore.GREEN + "You stand trial. The evidence is overwhelming, but a whistleblower from inside the company testifies on your behalf.")
                type_text("The courtroom erupts as the truth finally comes out. You win—at a heavy cost.")
                type_text("The case makes history, but the danger never truly leaves you.")
        elif decision == 'quiet':
            type_text(Fore.RED + "You lay low, hoping the storm passes. But it doesn’t.")
            type_text("One night, there’s a knock at your door. It’s the police.")
            type_text("You are arrested on fabricated charges and thrown into a legal battle you can’t win.")
            game_over()
        else:
            type_text(Fore.RED + "Invalid choice. Defaulting to staying quiet.")
            game_over()

def game_over():
    type_text(Fore.RED + "GAME OVER. Would you like to try again? (yes/no): ")
    retry = input().strip().lower()
    if retry == 'yes':
        intro()
    else:
        type_text(Fore.CYAN + "Thanks for playing.")

if __name__ == "__main__":
    intro()
