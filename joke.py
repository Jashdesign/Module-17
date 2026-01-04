import requests

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Joke:")
        print(data["setup"])
        print(data["punchline"])
    else:
        print("Failed to fetch joke")

if __name__ == "__main__":
    get_random_joke()