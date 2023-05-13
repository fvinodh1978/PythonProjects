import json
import os
from pathlib import Path
import pyutil


def format_json(feed_file):
    data = None
    with open(feed_file, "r") as file:
        data = json.load(file)
    file.close()
    # with open("C:\Official\ELK\Data\Processed\PhysicalEquipment_UIV_20220908_0045.json", "w") as f:
    #     f.write('{}\n '.format(json.dumps(data)))
    # f.close()

    with open("C:\Official\ELK\Data\Processed\PhysicalEquipment_UIV_20220908_0045.json", "w") as f:
        json.dump(data, f)
        f.write('\n')
    f.close()


def add_newline(feed_file):
    data = None
    with open(feed_file, "r") as file:
        data = file.read()
    file.close()
    # search_text = "^\s{2,}"
    search_text = "\n"
    replace_text = ""
    data = data.replace(search_text, replace_text)
    with open("C:\Official\ELK\Data\Processed\PhysicalEquipment_UIV_20220904_0045.json", "w") as f:
        f.write(data + "\n")
        # f.write('{}\n'.format(json.dumps(data)))
    f.close()


def clean_dict(feed_file):
    with open(feed_file, "r") as file:
        data = file.read()
    file.close()
    # search_text = "^\s{2,}"
    search_text = "\n"
    replace_text = ""
    data = data.replace(search_text, replace_text)
    with open("C:\Official\ELK\Data\Processed\CNF_UIV_20220904_0045.json", "w") as file:
        file.write(data)
    # print(data)
    file.close()


def split_json_array(file):
    docs = json.load(open(file))
    # my_file = os.path.basename(file)
    my_file = Path(file).resolve().stem
    my_path = os.path.dirname(file)
    print(my_path, my_file)
    file_path="C:\Official\ELK\Data\Processed\\" + my_file
    for ii, doc in enumerate(docs):
        with open(file_path + "_" + '{}.json'.format(ii), 'w') as out:
            # json.dump(doc, out)
            out.write('{}\n\r'.format(json.dumps(doc)))

def render_files_to_logstash():
    files = []
    file_path = "C:\Official\ELK\Data\Processed"
    files = [os.path.join(file_path, f) for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]
    for file in files:
        print(file)

file = "C:\\Official\\ELK\\Data\\Unprocesed\\VNF_UIV_20220908_0045.json"
# format_json(file)
render_files_to_logstash()
# split_json_array(file)
