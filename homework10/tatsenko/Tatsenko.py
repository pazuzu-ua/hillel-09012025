import requests
import json

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
res = requests.get(url)
data = res.json()

pikachu_height = data['height']
pikachu_weight = data['weight']

with open("IMPORTANT_DATA.txt", "w") as file:
    file.write(f"{pikachu_height},{pikachu_weight}")

ability_url = data['abilities'][1]['ability']['url']
res2 = requests.get(ability_url)
ability_data = res2.json()

with open("ability_data.json", "w", encoding="utf-8") as f:
    json.dump(ability_data, f, indent=4)
