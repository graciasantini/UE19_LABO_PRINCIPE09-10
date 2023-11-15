import requests

def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        joke = data["joke"]
        print(f"Dad Joke: {joke}")
    else:
        print(f"Erreur lors de la requête à l'API. Code d'erreur : {response.status_code}")

if __name__ == "__main__":
    get_dad_joke()
