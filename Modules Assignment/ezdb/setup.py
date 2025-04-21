'''

Run this program once before trting to use the ezdb_u module. 

Name:
Date:
Description:
'''

import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

ezdb_u_path = os.path.join(base_dir, "ezdb_u")
collections_path = os.path.join(ezdb_u_path, "collections")
config_file_path = os.path.join(ezdb_u_path, "config.txt")

os.makedirs(collections_path, exist_ok=True)

if not os.path.exists(config_file_path):
    with open(config_file_path, 'w') as config_file:
        config_file.write("Name:\nCollections:")