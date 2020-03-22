import json
import os
import pickle


def read_json(path):
    file_name = path
    with open(file_name) as f:
        data = json.load(f)
        return data


#     print(data)
# read_json('/Users/amishra/DEV/PythonFundamentals.Exercises.Part9/data/super_smash_bros/mario.json')

list_of_json_fl = []


def read_all_json_files(path):
    for root, dir, files in os.walk(path):
        for j in files:
            if j.endswith('.json'):
                result = read_json(os.path.join(path, j))
                list_of_json_fl.append(result)
            return list_of_json_fl


def write_pickle(file_path, data):
    with open(file_path, "wb") as file_handler:
        pickle.dump(data, file_handler)


def load_pickle(file_path):
    with open(file_path, 'rb') as file_handler:
        data = pickle.load(file_handler)
    return data