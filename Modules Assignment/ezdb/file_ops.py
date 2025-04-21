'''
Name: Ritesh Sivanathan
Date: April 17 2025
Description: Easily read, write and modify data in a NoSQL like database that uses csv files to store data. Just call the functions and provide the required parameters.
'''

'''
Indexes (ids) in the csv start with 1
'''

from functools import partial

class ReadOPS:

    BUFFER = 2**16

    def config() -> dict: # Show config file contents

        dict = {
            "Name": "",
            "Collections": []
        } # Dict is the config file as a dictionary

        f = open("../ezdb_u/config.txt", "r")
        
        content = f.read()
        lines = content.split("\n") # Do we really need to do this??
        
        for line in lines:
            
            line = line.split(":") # Split the line into key and value
            
            # Assuming we only have "collections" and "name"

            if line[0] == "Collections": 
                dict[line[0]] = line[1].split(",")
            else:
                dict[line[0]] = line[1]

        return dict # Dict is the config file as a dictionary

    def collections() -> int: # Show names of all created collections + related data
        
        dict = ReadOPS.config()
        
        print("Collections")

        for index, collection in enumerate(dict["Collections"]):
            
            with open(f"../ezdb_u/collections/{collection}.csv") as f:
                num_lines = sum(x.count("\n") for x in iter(partial(f.read, ReadOPS.BUFFER), ""))
            
            print(f"{index}: {collection} | {num_lines-1} entries")

        print("")

        return 0

    def collection(collection: str) -> int: # Show all the data in a collection
        
        collection_data = open(f"../ezdb_u/collections/{collection}.csv")
        
        data = collection_data.readlines()
        
        for index, line in enumerate(data):
            if index == 0:
                for index, field in enumerate(line.split(',')):
                    if index != (len(line.split(','))-1):
                        print(f"{field} | ", end="")
                    else:
                        print(f"{field}")
            else:
                print(' | '.join(line.split(',')), end="")
        return 0

    def collection_categories(collection: str) -> int:

        collection_header = next(open(f"../ezdb_u/collections/{collection}.csv"))
        # print(collection_header.read().split('\n')[0])
        print(f"Collection `{collection}` data fields: {collection_header}")

class CategoryOPS: # Add categories to existing files

    def add_category(collection: str, new_category: str) -> int:
        
        WriteOPS.precheck(collection, new_category)

        file = open(f"../ezdb_u/collections/{collection}.csv", "r")
        data = file.readlines()
        data[0] = data[0].rstrip('\n') 
        data[0] += f",{new_category}\n"
        overwrite = open(f"../ezdb_u/collections/{collection}.csv", "w")
        overwrite.write(''.join(data))

        print(f"Added field {new_category} to collection `{collection}.`")

class WriteOPS:

    def precheck(collection, row):
        
        config = ReadOPS.config()

        if collection not in config["Collections"]:
            print(f"Collection \"{collection}\" does not exist.")
            return 1

        if not row:
            print("Cannot add empty row.")
            return 1

        return 0
    
    def create_collection(collection: str) -> int:

        config = ReadOPS.config()

        if collection in config["Collections"]:
            print("There is already a collection with this name!")
            return 1

        path = f"../ezdb_u/collections/{collection}.csv"
        
        try:
            file = open(path, "x")
            print(f"Created Collection `{collection}`")
            return 0
        
        except:
            print("An error occured!")
            return 1

        # create new directory
    
    def single(collection: str, row: str) -> int:
        
        WriteOPS.precheck(collection, row)

        read_file = open(f"../ezdb_u/collections/{collection}.csv", "r")
        prev_id = int(read_file.readlines()[-1].split(',')[0])
        
        file = open(f"../ezdb_u/collections/{collection}.csv", "a+")
        file.write(f'\n{prev_id+1},{row}')
        
        print(f"Added 1 line to collection \"{collection}\"")
        
        return 0
    
    def multiple(collection: str, rows:str) -> int: # Rows should be separated by \n (newlines)

        WriteOPS.precheck(collection,rows)
        
        file = open(f"../ezdb_u/collections/{collection}.csv", "a")

        read_file = open(f"../ezdb_u/collections/{collection}.csv", "r")
        prev_id = int(read_file.readlines()[-1].split(',')[0])
        print(prev_id)
        count = 0

        for index, row in enumerate(rows.split('\n')):
            prev_id += 1

            file.write(f'\n{prev_id},{row}')
            count += 1
        
        print(f"Added {count} lines to collection \"{collection}\"")
    
class ModOPS:
    
    def delete_entry(collection: str, id: int) -> int: # Delete a specific data entry by its id
        
        file = open(f"../ezdb_u/collections/{collection}.csv", "r")
        data = file.readlines()
        data.pop(id)
        new_data = []

        for index, row in enumerate(data):
            
            if (row.split(',')[0] != "id"):
                
                if index in range(1,3): print(row)
                
                new_row = row.split(',')
                new_row[0] = str(index)
                row = ','.join(new_row)

                if index in range(1,3): print(row)
            
            new_data.append(row)
        
        overwrite = open(f"../ezdb_u/collections/{collection}.csv", "w")
        overwrite.write(''.join(new_data))

        print(f"Deleted entry id {id} in collection `{collection}`")