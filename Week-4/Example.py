import requests
import json


def Problem1():

    URL = "http://www.boredapi.com/api/activity/"

    response = requests.get(url=URL)

    jsonData = json.loads(response.text)

    print(jsonData['activity'])



def main():
    Problem1()

if __name__ == '__main__':
    main()