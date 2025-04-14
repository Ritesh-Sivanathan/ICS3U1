def print_hello(name):
    print(f"Hello, {name}!")

def print_love(name):
    print(f"I 💖 {name}!")

def print_celebration(name, event):
    confetti = "🎊"
    print(confetti*3)
    print(f"Congratulations on {event}, {name}!")

def print_dance(times):
    print("🕺💃🪩"*times)

def print_end(name):
    print(f"Goodbye, {name}!")

def help():
    
    print("""
          print_hello -> (name) -> greets the name
          print_love -> (name) -> loves name
          print_celebration -> (name, event) -> congratulates name on event 
          print_dance -> (times) -> prints dance emojis [times] amount of times
          print_end -> (name) -> farewell message to name
          """)