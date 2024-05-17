# import requests

# def combat (name1, name2) :
#     combatant1 = requests.get(name1).json()['id'];
#     combatant2 = requests.get(name2).json()['id'];

#     if combatant1 > combatant2 :
#         return requests.get(name1).json()['forms'][0]['name']
#     else :
#         return requests.get(name2).json()['forms'][0]['name']

# url_data = 'https://pokeapi.co/api/v2/pokemon/1';
# url_data2 ='https://pokeapi.co/api/v2/pokemon/2';

# result = combat(url_data, url_data2)
# print(result)
# # print(pokemons_data)
# print(pokemons_data.json()['abilities'][1]['slot'])

import requests

# url = "https://swapi.dev/api/people/2"

# payload = {}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

from flask import Flask

app = Flask(__name__)

@app.route("/hannibal/<valeur>/<Identifiant>")
def hello_world(valeur, Identifiant):
    # url = "https://pokeapi.co/api/v2/pokemon/"+valeur

    # payload = {}
    # headers = {}

    # try:
    #     response = requests.request("GET", url, headers=headers, data=payload)
    #     response.raise_for_status()  # Raises HTTPError for non-2xx responses
    #     return "True"
    # except requests.exceptions.HTTPError as e:
    #     return "False"
    # except Exception as e:
    #     print("An error occurred:", e)
    #     return "False"

    if valeur == "sw":
        url = "https://swapi.dev/api/people/"+Identifiant

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text

    elif valeur == "pk":
        url = "https://pokeapi.co/api/v2/pokemon/"+Identifiant

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text
    
    else:
        return 'Univers not found'

app.run(debug=True)

