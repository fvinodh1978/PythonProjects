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


def count_records(file_name):
    with open(file_name, 'r') as JSONFile:
        data = json.load(JSONFile)
    count = 0
    for obj in data:
        count = count + 1
        print(count, obj['globalName'])
    return count


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def split_file(file_name, chunk_size):
    out_path = 'C:/Official/Projects/Workspace/PythonProjects/Resources/Output'
    with open(file_name, 'r') as f1:
        data = json.load(f1)
        size = len(data)
    file_list = ["cnf"]
    print(file_list[0] + ", Number of Records : " + str(size))
    print("Chunk Size : " + str(chunk_size))
    num_file = 0
    for i in range(0, len(data), chunk_size):
        num_file = num_file + 1
        # tmp_data = data[i:i + chunk_size]
        json.dump(data[i:i + chunk_size], open(out_path + '/' + file_list[0] + str(i) + '.json', 'w', encoding='utf8'),
                  ensure_ascii=False,
                  indent=True)
    print("Number of Files : " + str(num_file))


def get_json_obj(my_file, outfile, key, value):
    with open(my_file, 'r') as file_obj:
        python_obj = json.load(file_obj)
        print("Total Records : " + str(len(python_obj)))
    filtered_list = [
        dictionary for dictionary in python_obj
        if (dictionary[key] == value)
    ]
    print(str(len(filtered_list)) + " : " + str(type(filtered_list)))
    with open(outfile, "w") as outfile_obj:
        json.dump(filtered_list, outfile_obj)


def get_rec_count(path, key):
    device_types = ["physicalPort", "PhysicalPort", "Site", "Rack", "compute", "storage", "appliance", "router",
                    "switch"]
    files = os.listdir(path)
    for file in files:
        my_file = os.path.join(path, file)
        with open(my_file, "r") as file_obj:
            python_obj = json.load(file_obj)
        kinds = []
        for obj in python_obj:
            kinds.append(obj.get(key))
        # print("total Records : " + str(len(python_obj)))
        print("total Records : " + file + " : " + str(len(kinds)))

        for kind in set(kinds):
            filtered_list = ''
            filtered_list = [
                dictionary for dictionary in python_obj
                if (dictionary[key] == kind)
            ]
            print(file + " : " + kind + " : " + str(len(filtered_list)))


def get_rec_count1(my_file, out_file, key):
    with open(my_file, "r") as file_obj:
        python_obj = json.load(file_obj)
    print("total Records : " + str(len(python_obj)))
    values = []
    for obj in python_obj:
        values.append(obj.get(key))

    lst = list(set(values))

    with open(out_file, "w") as out_file_obj:
        out_file_obj.write('\n'.join([i for i in lst[0:]]))


def get_obj_count(my_file, key):
    with open(my_file, "r") as file_obj:
        python_obj = json.load(file_obj)
    print("Total Records : " + str(len(python_obj)))


def get_ip_count(my_file, out_file):
    # my_file=os.path.abspath("../../Resources/ip_file.txt")
    with open(my_file, "r") as file_obj:
        file_content = file_obj.read()
    ips = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', file_content)
    print("Number of Ips :", len(ips))

    # for ip in ips:
    #     print(ip)

    with open(out_file, "w") as out_file_obj:
        out_file_obj.write('\n'.join([i for i in ips[0:]]))

    # print("Octects :", octects)


# file = 'C:\\Users\\vf1935\\Downloads\\UIV_20221111_0045\\CNF_UIV_20221111_0045.json'
# # file = "C:/Official/Projects/Workspace/PythonProjects/Resources/Input/Sample_split.json"
# split_file(file, 3)


# all_args=sys.argv[1:]
# my_file=all_args[0]
# key=all_args[1]
# value=all_args[2]
# Site file
# my_file = "C:\Official\Projects\Service Now\Data\Chicago\\nokiacb_physicalPort_delta_20230607\\nokiacb_physicalPort_delta_20230607.json"

# Rack File
# my_file = "C:\Official\Projects\Service Now\Data\Chicago\\nokiacb_physicalPort_delta_20230607\\nokiacb_physicalPort_delta_20230607.json"

# Device File
# my_file = "C:\Official\Projects\CloudBand\Data\Original\\nokiacb_physicalEquipment_delta_20230607.json"

# Port File
# my_file = "C:\Official\Projects\CloudBand\Data\Original\\nokiacb_physicalPort_delta_20230607.json"

# VNF Device File
# my_file = "C:\Official\Projects\CloudBand\Data\Original\\nokiacb_vnfVirtualDevice_delta_20230516.json"

# VNF Component File
# my_file = "C:\Official\Projects\CloudBand\Data\Original\\nokiacb_vnfVirtualComponent_delta_20230516.json"

# VNF Port File
# my_file = "C:\Official\Projects\CloudBand\Data\Prod\\nokiacb_vnfVirtualPort_delta_20230531.json"

# VNF Interface File
my_file = "C:\Official\Projects\CloudBand\Data\Prod\\nokiacb_vnfLogicalInterface_delta_20230531.json"

# CNF Device File
# my_file = "C:\Official\Projects\CloudBand\Data\Original\\nokiacb_cnfVirtualDevice_delta_20230516.json"

# CNF Component File
# my_file = "C:\Official\Projects\CloudBand\Data\Prod\\nokiacb_cnfVirtualComponent_delta_20230602.json"

# CNF Port File
# my_file = "C:\Official\Projects\CloudBand\Data\Prod\\nokiacb_cnfVirtualPort_delta_20230602.json"

key = "kind"
# key = "name"
value = "multusPort"
temp_file = "C:\Official\Projects\CloudBand\Data\Test Data\\nokiacb_pnf-PhysicalPort.json"
out_file = "C:\Official\Projects\CloudBand\Data\Test Data\\nokiacb_pnf-PhysicalPortIPs.txt"
my_path = "C:\Official\Projects\CloudBand\Data\Prod"

# get_json_obj(my_file, temp_file, key, value)
get_rec_count(my_path, key)
key = "object_id"
# get_rec_count1(temp_file, out_file, key)
# get_ip_count(my_file, out_file)

