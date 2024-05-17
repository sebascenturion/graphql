import requests
import json

url = "https://api.thecatapi.com/v1/favourites"


#se utiliza un token autorizado por el API
headers = {
	"X-Api-Key": "DEMO-API-KEY"
}

response = requests.request("GET", url, headers=headers)
if response.status_code == 200:
    json_dict = json.loads(response.text)
    print(json_dict[0])
else:
    print(response.status_code)