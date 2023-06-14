import json
import os
import getopt
import sys

from pathlib import Path


def get_env(key):
    data = None
    my_file = "C:\Personal\Vinodh\MyProjects\PythonProjects\Workspace\Gift\Resources\env_properties.json"
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


def get_ip_count():
    my_file = os.path.abspath("../../Resources/ip_file.txt")
    with open(my_file, "r") as file_obj:
        file_content = file_obj.read()
    ips = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', file_content)
    octects = set()
    for ip in ips:
        octect = re.findall(r'(^\d{1,3})', ip)
        octects.add(octect[0])
    # print("IPs :", ips)
    print("Number of Ips :", len(ips))
    # print("Octects :", octects)


def get_rec_count(search_str):
    print("Number of Ips :")


def get_json_obj(my_file, key, value):
    with open(my_file, 'r') as file_obj:
        python_obj=json.load(file_obj)
    filtered_list = [
        dictionary for dictionary in python_obj
        if dictionary[key] == value
    ]
    print(filtered_list)


all_args = sys.argv[1:]
print(all_args[0])
print(all_args[1])
print(all_args[2])
try:
    # Gather the arguments
    opts, arg = getopt.getopt(all_args, 'f:k:v:')
    my_file=''
    key=''
    value=''
    if len(opts) < 1:
        print('usage: args_demo.py -f <filename> -k <key> -v <value>' )
    else:
        # Iterate over the options and values
        for opt, arg_val in opts:
            if(opt=='-f'):
                my_file=arg_val
            elif(opt=='-k'):
                key=arg_val
            elif(opt=='-v'):
                value=arg_val

    get_json_obj(my_file, key, value)

except getopt.GetoptError:
    print('usage: args_demo.py -a <first_value> -b <second_value>')
    sys.exit(2)


