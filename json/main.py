


import json

# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist

with open('test.json') as f:
    d = json.load(f)

    # {'a': True, 'b': 2, 'c': 'str', 'd': [{'change': False}, {'change': False}], 'e': None}

    print("pre ->")
    print(d)

    for el in d['d']:

        # print(el['change'])
        el['change'] = True

print("post ->")
print(d)

f = open('test.json', "w")
f.write(json.dumps(d, indent=4, sort_keys=True))
f.close()













# end
