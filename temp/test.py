import json

FILE_PATH = "json/creds.json"

with open(FILE_PATH, "r") as file:
    data = json.load(file)
    accounts = data["pasword"]

    print(accounts[0])
