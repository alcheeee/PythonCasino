import os
import json

def get_user_data():
    filename = 'UserData.json'
    file_check = os.path.isfile(filename)
    user_data = {"coins": 1000}

    if not file_check:
        with open(filename, 'w') as fp:
            json.dump(user_data, fp, indent=4)
        return user_data
    else:
        with open(filename, 'r') as fp:
            user_data = json.load(fp)
        return user_data

def adjust_coins(coins, filename='UserData.json'):
    if os.path.isfile(filename):
        with open(filename, 'r') as fp:
            data = json.load(fp)
        data['coins'] = coins
        with open(filename, 'w') as fp:
            json.dump(data, fp, indent=4)
        return data
    else:
        return None