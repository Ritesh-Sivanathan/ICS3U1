'''
Name:
Date:
Description:
'''

from functools import partial

BUFFER = 2**16

def full_read(): # Show config file contents

    dict = {
        "Name": "",
        "Collections": []
    }

    f = open("../ezdb_u/config.txt", "r")
    
    content = f.read()
    lines = content.split('\n')
    
    for line in lines:
        
        line = line.split(':')
        
        if line[0] == "Collections":
            dict[line[0]] = line[1].split(',')
        else:
            dict[line[0]] = line[1]

    return dict

def show_collections(): # Show names of all created collections + related metadata
    
    dict = full_read()

    print(f"\n{dict["Name"]}\n")
    print("Collections")

    for index, collection in enumerate(dict["Collections"]):
        
        with open(f"../ezdb_u/collections/{collection}.csv") as f:
            num_lines = sum(x.count('\n') for x in iter(partial(f.read, BUFFER), ''))
        
        print(f"{index}: {collection} | {num_lines-1} entries")


    print("")

def collection_read(collection: str):
    
    collection_data = open(f'../ezdb_u/collections/{collection}.csv')
    
    print(collection_data.read())

def handle_error(code):
    pass