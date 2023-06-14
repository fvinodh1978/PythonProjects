import json
import os
from pathlib import Path


def get_env(key):
    data = None
    absolute_path = os.path.dirname(__file__)
    print(absolute_path)
    my_file = os.path.abspath("../Resources/env_properties.json")
    print(my_file)
    try:
        file_obj = open(my_file, "r")
    except FileNotFoundError as e:
        print("File doesnt exists in the folder...")
    else:
        python_dict = json.load(file_obj)
        return python_dict.get(key)
    file_obj.close()


def getenv(name):
    print("Started Reading JSON file")
    with open("developer.json", "r") as read_file:
        print("Converting JSON encoded data into Python dictionary")
        developer = json.load(read_file)

        print("Decoded JSON Data From File")
        for key, value in developer.items():
            print(key, ":", value)
        print("Done reading json file")
