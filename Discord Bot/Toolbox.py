import os.path
from os import path
import random

# this is for a later function that will be added to the bot
# it will be an Awards function where you can gift individuals a certain amount of 'money' in response to a post they liked


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





