from flask import json

"""read config from config.json"""
def readConfig():
    file = "config.json"

    with open (file, 'r') as file:
        config = json.loads(file.read())

    print(config)

    return config