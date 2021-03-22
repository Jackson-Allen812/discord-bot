from os import path
import random


def write_to_file(id_, amount):

    file_name = "Awards\\" + str(id_) + ".txt"

    if path.exists(file_name):
        with open(file_name, "r") as file:
            temp = int(file.read())
            temp += int(amount)
        with open(file_name, "w") as file:
            file.writelines(str(temp))
    else:
        with open(file_name, "w") as file:
            print("Account Created")
            file.writelines(str(amount))


def account_balance(id_):

    file_name = "Awards\\" + str(id_) + ".txt"

    if path.exists(file_name):
        with open(file_name, "r") as file:
            return int(file.read())
    else:
        return None


def format_id(id_):
    temp = str(id_)
    remove = "<@!>"

    for char in remove:
        temp = temp.replace(char, "")

    return temp





