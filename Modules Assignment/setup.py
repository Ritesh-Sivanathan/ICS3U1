'''
RUN THIS IN A DIRECTORY CALLED "ezdb"
'''

import os

base_path = os.path.join(os.getcwd(), "ezdb_u")
collections_path = os.path.join(base_path, "collections")
config_path = os.path.join(base_path, "config.txt")

if not os.path.exists(base_path):
    os.mkdir(base_path)
    print("Created directory: ezdb_u")

if not os.path.exists(collections_path):
    os.mkdir(collections_path)
    print("Created directory: collections")

if not os.path.exists(config_path):
    with open(config_path, "w") as f:
        f.write("Name:\nCollections:")
        print("Created config.txt with required content.")
else:
    print("config.txt already exists. Skipping file creation.")
