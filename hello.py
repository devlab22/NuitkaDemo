
from requests import request
import json

def printJson(data):
    print(json.dumps(data, indent=4))

def talk(message):
    return "Talk " + message

def getUsers():
    
    url = f'https://jsonplaceholder.typicode.com/users'
    response = request("GET", url).json()
    return response


def main():
    print(talk("Hello World"))
    printJson(getUsers())

    


if __name__ == "__main__":
    main()
    