# About

EzDb is a mock database that utilizes csv files to store data.
You can create collections which are just different csv files

# Setup

Manually create a directory called "ezdb" in the location you want to run this program.
Then, move the `setup.py` and `fileops.py` files to this directory and run `setup.py`. You should have a new directory called "ezdb_u" that appears one directory back from your current directory.

# Utilization

To use EzDb, create a `main.py` file in the "ezdb" directory (the one with the `setup.py` file). From here, you can import commands like so:

`from ezdb import ReadOPS, WriteOPS, ModOPS, CategoryOPS`

# Code

The code for EzDb is all in the ezdb.py file. The different operations (Read, Write, Modify) are all separated by classes. Each of these classes have their own custom functions.