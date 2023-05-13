import json

file="C:\Personal\Vinodh\MyProjects\PythonProjects\Workspace\PythonTutorials\Resources\createfile.txt"
try:
    file_obj = open(file, "w")
except (FileNotFoundError) as e:
    print("File doesnt exists in the folder...")
else:
    # json_obj = json.dumps(python_obj)
    file_obj.write("This is a New File!")
finally:
    print("File Reading Completed")
    file_obj.close()

try:
    file_obj = open(file, "r")
except (FileNotFoundError) as e:
    print("File doesnt exists in the folder...")
else:
    # json_obj = json.dumps(python_obj)
    print(file_obj.read())
finally:
    print("File Writing Completed")
    file_obj.close()