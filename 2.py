import argparse
import os
import configparser
import pickle


class Data:
    def __init__(self, age="", name="", fav_animal="", fav_drink=""):
        self.age = age

    self.name = name
    self.fav_food = fav_animal
    self.fav_drink = fav_drink


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-f", "--file", default="default.ini", help="Input settings file name")
    parser.add_argument("-a", "--action", default="", help="Describe an action: read or write")
    args = parser.parse_args()

    data = Data()

    if os.path.isfile(args.file) == True:

    config = configparser.ConfigParser()
    config.read(args.file, encoding="UTF-8")
    data.name = config["Info"]["name"]
    data.age = config["Info"]["age"]
    data.fav_food = config["Info"]["fav_food"]
    data.fav_drink = config["Info"]["fav_drink"]
    pickled_data = pickle.dumps(data)

    config["Data"]["data"] = str(pickled_data)

    with open(f"{args.file}", "w") as configfile:
        config.write(configfile)

    print(config["Data"]["data"])
    new_data = pickle.loads(pickled_data)
    print("Age from settings:", new_data.age)
    else:
    print("File has not been found")

""" picklefile = open("data", "rb") 
 data = pickle.load(picklefile) 
 picklefile.close() 
 print()"""
