'''
Name:
Date:
Description:
'''

# mock database, like mongodb. info stored in text file (or csv)
# info stored in a folder
    # collections (maybe csv would be easier)
    # collections will follow as csv files with the data

# simple CRUD functionality
# uses basic external libraries

from ezdb.ops.read_db import show_collections

def main():
    show_collections()

main()