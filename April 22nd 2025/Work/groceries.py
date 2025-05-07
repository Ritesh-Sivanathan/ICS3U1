
def add_groceries():
    
    with open("groceries.txt", "a") as grocery_file:
        
        number = int(input("How many groceries would you like to add?: "))
        
        for i in range(1, number+1):
            grocery_file.write(str(input(f"#{i}: ")).strip()+"\n") # Avoid any whitespaces user may have left at start or end
        
def see_groceries():
    
    with open("groceries.txt", "r") as grocery_file:
        
        for line in grocery_file:
            print(line.strip())

add_groceries()
see_groceries()