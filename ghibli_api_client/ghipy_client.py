import requests
import json
from modelos import Movie

url = "https://ghibliapi.vercel.app/films/"
url_personaje = ""

response = requests.get(url)


json_text = response.text

json_dict = json.loads(json_text)
for pelicula in json_dict:
    #print('Nombre: {}  - Anho {}. Productor {}'.format(pelicula["title"], pelicula["release_date"], pelicula["producer"]))
    movie = Movie(**pelicula)
    print("\n ------PELICULA------")
    print(movie.title)
    print("\n ------PERSONAJES------")
    print(movie.people)
    for url_personaje in movie.people:
        #print(url_personaje)
        response = requests.get(url_personaje)
        json_text = response.text
        json_per = json.loads(json_text)
        try:
            print(json_per["name"])
        except:
            pass