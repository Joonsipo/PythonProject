import requests

try:
    pyynto = "https://api.chucknorris.io/jokes/random"
    vastaus = requests.get(pyynto)

    if vastaus.status_code == 200:
        data = vastaus.json()
        print(data["value"])
    else:
        print("Hakua ei voitu suorittaa, statuskoodi:", vastaus.status_code)

except requests.exceptions.RequestException:
    print("Hakua ei voitu suorittaa")