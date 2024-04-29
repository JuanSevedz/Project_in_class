"""# Read text file
def read_text_file(file_path):
    with open(file_path, 'r') as file_alias:
        content = file_alias.read()
    return content

# Write text file
def write_text_file(file_path, contennt):
    with open(file_path, 'w') as file:
        file.write(contennt)
    
# expample usage
file_path = 'example.txt'
content =  read_text_file(file_path)
print(content)

new_content = 'This is the new content.'
write_text_file(file_path, new_content)"""
"""import json
from pprint import pprint
# Read JSON file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Write JSON file
def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file)

#Example usage
file_path = 'anscombe.json'

# Read JSON file
data = read_json_file(file_path)
print(type(data))
pprint(data)

# Modify data in positions 
data[2]['name'] = 'hola'
data[2]['age'] = 27

# modify data, add a new list
new_data = {}
new_data['name'] = 'new name'
new_data['age'] = 28
data.append(new_data)


# Write JSON file
write_json_file(file_path, data)"""

import pickle
import sys
import os

#Decorator to get object and pickle size

def get_pickle_size(func):
    def wrapper(*args, **kwargs):
        # Get object
        object_size = sys.getsizeof(args[1])
        
        # Call the function
        result = func(*args, **kwargs)

        # Get pickle size
        pickle_size = os.path.getsize(args[0])

        print(f'Object size: {object_size} bytes')
        print(f'Pickle size: {pickle_size} bytes')

        return result
    return wrapper

# Read object from pickle file
def read_pickle_file(pickle_file):
    with open(pickle_file, 'rb') as file:
        obj = pickle.load(file)
    return obj

# Write object to pickle file
@get_pickle_size
def write_pickle_file(pickle_file, obj):
    with open(pickle_file, 'wb') as file:
        pickle.dump(obj, file)

#Example usage
data = {'name': 'Alice', 'age' : 25, 'gender': 'f'}
pickle_file = 'data.pickle'

# Write pickle file
write_pickle_file(data, pickle_file)

# Read object from pickle file
read_data = read_object_from_pickle(pickle_file)
print(read_data)