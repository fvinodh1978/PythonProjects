import json

file= "/PythonTutorials/Resources/site_file.json"
try:
    python_obj = open(file, "r")
except (FileNotFoundError) as e:
    print("File doesnt exists in the folder...")
else:
    # json_obj = json.dumps(python_obj)
    print(python_obj)
