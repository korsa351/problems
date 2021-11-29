import requests

api_url = "http://numbersapi.com/"
params = {"json": True}

with open("problem AL.txt", "r") as string:
    for numbers in string:
        number = numbers.strip()
        data = requests.get(api_url + str(number) + "/math", params=params)
        data = data.json()
        print("Interesting") if data["found"] else print("Boring")
