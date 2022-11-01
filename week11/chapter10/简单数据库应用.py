# @Time: 2022/11/1 23:35
# @Author: 李树斌
# @File : 简单数据库应用.py
# @Software :PyCharm
import sys, shelve

def store_person(db):
    """让用户输入数据并将其存储到shelve对象中"""

    pid = input("Enter unique ID number:")
    person = {}
    person["name"] = input("Enter name:")
    person["age"] = input("Enter age:")
    person["phone"] = input("Enter phone number:")
    db[pid] = person

def lookup_person(db):
    """让用户输入ID和所需的字段，并从shelve对象中获取相应的数据"""

    pid = input("Enter ID number:")
    field = input("What would you like to know?(name, age, phone)")
    field = field.strip().lower()
    print(field.capitalize() + ":", db[pid][field])

def print_help():
    print("The available commands are:")
    print("store : Stores information about a person")
    print("lookup : Looks up a person from ID number")
    print("quit : Save changes and exit")
    print("? : Prints this message")

# def enter_command():
#     cmd = input("Enter command (? for help):")
#     cmd = cmd.strip().lower()
#     return cmd
def main():
    database = shelve.open("database.dat")
    try:
        while True:
            command = input("Enter command(? for help):")
            if command == "store":
                store_person(database)
            elif command == "lookup":
                lookup_person(database)
            elif command == "?":
                print_help()
            elif command == "quit":
                return
    finally:
        database.close()

if __name__ == "__main__":
    main()