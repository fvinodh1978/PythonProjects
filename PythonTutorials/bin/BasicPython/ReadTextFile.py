import json

file= "/PythonTutorials/Resources/demofile.txt"
try:
    file_obj = open(file, "r")
except (FileNotFoundError) as e:
    print("File doesnt exists in the folder...")
else:
    # json_obj = json.dumps(python_obj)
    print(file_obj.read())
finally:
    print("File Reading Completed")
    file_obj.close()

try:
    file_obj = open(file, "a")
except (FileNotFoundError) as e:
    print("File doesnt exists in the folder...")
else:
    # json_obj = json.dumps(python_obj)
    file_obj.write("\nThis is New End!")
finally:
    print("File Writing Completed")
    file_obj.close()
    file_obj = open(file, "r")
    print(file_obj.read())
