'''
Name:
Date:
Description:
'''

def full_read():

    dict = {
        "Name": "",
        "Collections": ""
    }

    f = open("../ezdb_u/config.txt", "r")
    
    content = f.read()
    lines = content.split('\n')
    
    for line in lines:
        line = line.split(':')
        dict[line[0]] = line[1]
    
    return dict

def show_collections():
    
    dict = full_read()

    for collection in dict["Collections"].

def collection_read(collection: str):

    if not collection:
        return 0
    
def handle_error(code):
    pass

full_read()