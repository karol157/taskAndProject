import os
import json

class UserConsole:
    def __init__(self):
        pass

    @staticmethod
    def clear():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

class Files:
    @staticmethod
    def open(path, type='str'):
        file = open(path)
        file = file.read()
        if type == 'int':
            try:
                file = int(file)
            except:
                print("Can't parse to int!")
        return file
    @staticmethod
    def jsonOpen(path, method='r', data=None):
        if method == 'r':  # Read mode
            with open(path, method) as file:
                return json.load(file)
        elif method == 'w':  # Write mode
            with open(path, method) as file:
                json.dump(data, file)  # Write data to file
        else:
            raise ValueError("Invalid method! Use 'r' for read or 'w' for write.")



File = Files
Console = UserConsole