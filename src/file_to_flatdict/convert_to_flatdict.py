import yaml
import json
from configparser import ConfigParser


def to_flatdict(file_path):
    raw_file_path = file_path.replace("\t","\\t").replace("\n","\\n").replace("\b","\\b").replace("\f","\\f").replace("\r","\\r")
    if file_path.endswith(".yaml") or file_path.endswith(".yml"):
        return yaml_to_flatdict(raw_file_path)
    elif file_path.endswith(".cfg"):
        return cfg_to_flatdict(raw_file_path)


# yaml to flatdict
def yaml_to_flatdict(file_path):
    d1 = {}
    with open(file_path) as file:
        documents = yaml.safe_load(file)
    # value_yaml = flatdict.FlatDict(documents)
    return convert_flatdict(documents)


# .cfg(.ini) to flatdict
def cfg_to_flatdict(file_path):
    config = ConfigParser()
    config.read(file_path)
    sections = config._sections
    return convert_flatdict(sections)


def convert_flatdict(file_obj):
    d1 = {}
    for x in file_obj:
        for y in file_obj[x]:
            k = x+"_"+y
            d1[k] = file_obj[x][y]
    return d1

"""out = to_flatdict("D:\Aishwarya_Work\pythonProject5\examples\conf2.yml")
print(out)
out1 = to_flatdict("D:\Aishwarya_Work\pythonProject5\examples\conf1.cfg")
print(out1)"""