def Q2():
    
    marks = {}

    for i in range(2):
        student_name = input(f"Student {i}: ")
        grade = int(input("Marks: "))
        marks[student_name] = grade 
    
    print(marks)

def Q3():
    
    def acceptLogin(users, username, password):
        return True if username in users and users[username] == password else False
    
def Q4():

    def wordFrequencies(mylist):
        
        new_dict = {}

        for word in mylist:
            if word not in new_dict:
                new_dict[word] = mylist.count(word)

        print(new_dict)

    wordFrequencies(["A", "B", "C", "A", "D"]) 

def Q5():
    
    geek = {
        "404": "clueless",
        "googling": "Searching the internet for background information",
        "keyboard plaque": "Collection of debris on the keyboard",
        "link rot": "the process by which web pages become obsolete",
        "percussive maintenance": "the act of striking an electronic device"
    }

    choices = {
        1: 'Search Term',
        2: 'Add Term',
        3: 'Redefine Term',
        4: 'Delete Term',
        5: 'Quit'
    }

    def process_text(text):
        return (text.lower()).strip()

    def search():
        
        term = input("Search... ")
        term = process_text(term)

        if term in geek:
            print(geek[term])
            menu()
        else:
            print("Sorry, I don't know that term")
            menu()
    
    def add():
        
        term = input("New Term: ")
        definition = input("Definition: ")

        term = process_text(term)
        definition = process_text(definition)

        if term in geek:
            if geek[term] == definition:
                print("That term already exists! Try redefining it")
        
        geek[term] = definition

        print(f'The term "{term}" has been added!')

        menu()

    def redefine():
        
        term = input("Term: ")
        
        term = process_text(term)

        if term not in geek:
            print("That term doesn't exist! Try adding it")
            menu()

        geek[term] = input(f'Definition of "{term}": ').lower()

        print(f'Term "{term}" has been redefined')

        menu()

    def delete():

        term = input("Term: ")

        term = process_text(term)

        if term not in geek:
            print("Sorry, I don't know that term.")
            menu()

        del geek[term]
        menu()
    
    def menu():

        for key, value in choices.items():
            print(f"{key} - {value}")
        
        choice = int(input("Key: "))

        while choice not in range(len(choices)):
            
            choice = int(input("Key: "))
        
        match choice:
            case 1:
                search()
            case 2:
                add()
            case 3:
                redefine()
            case 4:
                delete()
            case 5:
                exit()
    
    menu()

Q5()