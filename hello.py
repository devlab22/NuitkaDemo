
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
    return response[0]


def main():
    print(meraki.__version__)
    print(talk("Hello World"))
    printJson(getCountry('germany'))

    


if __name__ == "__main__":
    main()
    