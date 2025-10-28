#!/usr/bin/env python3

# Connect to the Pokemon API and get a random pokemon. Only from the original 151 pokemon!

from datetime import datetime
import json
import logging
import random
import requests

output_path = "Pokemon"      # Root directory of output files. Change here.
base_url = "https://pokeapi.co/api/v2/pokemon"      # Base URL for the pokemon API.
logging.basicConfig(level=logging.DEBUG, filename=f"{output_path}/logs/pokemon.log", format="%(asctime)s - %(levelname)s - %(message)s") # Setup log file details

# Make API call and get pokemon data
def get_pokemon_info(id):
    response = requests.get(f"{base_url}/{id}")    #   make API call
    
    if response.status_code == 200:
        return parse_pokemon_data(response.json())

# Format the output
def parse_pokemon_data(pokemon):
    # Pokemon can have multiple types, format into a single line before adding to final output.
    types = pokemon["types"]
    poke_types = []
    for type in types:
        poke_types.append(type["type"]["name"])
    
    data = {
        "name": f"{pokemon['name']}",
        "id": f"{pokemon['id']}",
        "height": f"{pokemon['height']}",
        "weight": f"{pokemon['weight']}",
        "type": poke_types
    }
    return data
   
def write_pokemon_data(pokemon):
    try:
        filename = f"{output_path}/pokemon/{datetime.now().strftime('%Y%m%d')}_{pokemon['name']}.json"
        with open(filename, "x") as f:
            json.dump(pokemon, f)
            logging.info(f"Created file: {filename}")
    except (FileNotFoundError):
        logging.error(f"Could not write file: {filename}.")

if __name__ == "__main__":
    has_errors = False  # If set to true, will create the error file.
    poke_id = random.randint(1, 151) # Generate a random ID. This is the ID of the pokemon we are retrieving.

    pokemon = get_pokemon_info(poke_id)
    write_pokemon_data(pokemon)