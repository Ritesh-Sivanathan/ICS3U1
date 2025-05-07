new_data = []

with open('groceries.txt', 'r') as file:
    
    fruit = input("Disliked fruit: ")
    data = file.readlines()

    if ((fruit.lower().strip())+'\n') in data:
        ix = data.index(fruit.lower().strip()+'\n')
        data.pop(ix)
    new_data = data

with open('groceries.txt', 'w') as file:

    for line in new_data:
        file.write(line)
    
