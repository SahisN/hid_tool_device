import json


class ReadJson:
    def __init__(self):
        self.FILE_PATH = "json/creds.json"
        self.data = self.get_data()

    def get_data(self):
        # get all the accounts, username, password
        with open(self.FILE_PATH, "r") as file:
            data = json.load(file)

        return data

    # returns all the accounts
    def get_accounts(self) -> list:
        return self.data["accounts"]

    # returns specific username list depending on the account
    def get_usernames(self, account_type: str) -> list:
        return self.data["username"][account_type]

    # return one password for a specific account and username
    def get_password(self, account_type: str, username: str) -> list:
        return self.data["password"][account_type][username]
