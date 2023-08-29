#The purpose of this consoul application is to use file-base storage system. 
#We will create "student.json" file to store the information of the students 
#We will CRUD (Create, Read, Update, Delete) in the students.json file

from create import create_std
from read import read_std
from update import update_std
from delete import delete_std




def inquiry():
    selection = input("Select your choice c/r/u/d/e")
    selection = selection.lower()

    def exit_message():
        print("Thank you, See you again")
    if selection == "c":
        repeat = create_std()
        inquiry() if repeat else exit_message()
    elif selection == "r":
        std_id = input("Enter std id")
        repeat = read_std()
        inquiry() if repeat else exit_message()
    elif selection == "u":
        update_std()
    elif selection == "d":
        delete_std()
    else:
        exit_message()

if __name__ == "__main__":
    inquiry()


    



