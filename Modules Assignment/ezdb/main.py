'''
CHANGE ACTIVE DIRECTORY TO ../ezdb
!!! THEN RUN main.py
'''

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

from ezdb import ReadOPS, WriteOPS, ModOPS, CategoryOPS

def main():
    ReadOPS.collection('users')
    ReadOPS.collection

main()