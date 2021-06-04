import requests
import json

def Problem1():
    URL = "https://cat-fact.herokuapp.com/facts"

    response = requests.get(url=URL)
    data = json.loads(response.text)

    print(data[0]['text'])


def Problem2():
    URL = "https://prod-36.westus.logic.azure.com:443/workflows/fc71fb3fe45549839788c7b1a12d1fb7/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=s2teoxmimXtvQqa9SNji3zmd-nFCseMAcAa3EmlK5hQ"

    headers = {
        "ApiKey": "Phil Collins",
        "Content-Type": "application/json"
    }

    body = {
        "message": "Testing the post!"
    }

    try:
        response = requests.post(url=URL, headers=headers, data=json.dumps(body))
    except Exception as e:
        print(e)


def main():
    Problem2()
    

if __name__ == '__main__':
    main()