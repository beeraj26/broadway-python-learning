import json
import os
filename = "stds.json"


def create_std(): 
    id = input("Enter std id")
    name = input("Enter std name")
    age = input("Enter std age")
    address = input("Enter std address")

    std = dict(id = id, name = name, age = age, address = address)
    if not os.path.exists(filename):
        with open(filename, "w") as fp:
            data = json.dumps([std], indent= 2)
            fp.write(data)

    else:
        with open(filename, "r+") as fp:
            stds = json.loads(fp.read())
            stds.append(std)
            fp.seek(0)
            data = json.dumps(stds, indent=2)
    print("Student Added Successfully !!")
    repeat = input("Do You want to continue?(y/n)")
    return True if repeat.lower() == "y" else False



