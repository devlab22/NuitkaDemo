from heapq import merge
from requests import request
import json
import meraki

def printJson(data):
    print(json.dumps(data, indent=4))

def talk(message):
    return "Talk " + message

def getCountry(name:str):
    
    url = f'https://restcountries.com/v3.1/name/{name}'
    response = request("GET", url).json()
    for item in response:
        printJson(item)


def main():
    print(meraki.__version__)
    print(talk("Hello World"))

    


if __name__ == "__main__":
    main()
    