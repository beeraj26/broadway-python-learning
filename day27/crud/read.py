import json
filename = "stds.json"

def read_std(std_id):
    with open(filename, 'r') as fp:
        stds = json.loads(fp.read())
    std = list(filter(lambda x: x["id"] == std_id, stds))
    if std:
        std = std[0]
        print(std)
    else:
        print("No matching std id")
    repeat = input("Do You want to continue?(y/n)")
    return True if repeat.lower() == "y" else False
    

