
with open("groceries.txt", "a+") as file:
        
    file.seek(0)

    data = file.readlines()
    print(data)

    favourite_fruit = input("Favourite fruit?: ")

    if (favourite_fruit+"\n") not in data:
        file.write(favourite_fruit+"\n")
    
    print("Favourite fruit added")