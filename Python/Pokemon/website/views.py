from flask import Blueprint, render_template, request, flash, jsonify
from . import db
import random
import requests
from .models import Pokemon
import json

POKEMON_URL = "https://pokeapi.co/api/v2/pokemon"  # Base URL for the pokemon API.

views = Blueprint("views", __name__)

@views.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@views.route("/pokemon", methods=["GET", "POST"])
def pokemon():
    if request.method == "POST":
        response = requests.get(f"{POKEMON_URL}/{random.randint(1,151)}")
        if response.status_code == 200:
            new_pokemon = parse_pokemon_data(response.json())
            print(new_pokemon.name)
        
            try:
                db.session.add(new_pokemon)
                db.session.commit()
            except:
                pass
            #flash("Pokemon added!", category="success")
    pokemon = Pokemon.query.order_by(Pokemon.created_at).all()
    
    return render_template("pokemon.html", pokemon=pokemon)


@views.route("/delete-pokemon", methods=["POST"])
def delete_pokemon():
    pokemon = json.loads(request.data)
    pokemon_id = pokemon["id"]
    pokemon = Pokemon.query.get(pokemon_id)
    if pokemon:
        db.session.delete(pokemon)
        db.session.commit()
        #flash("Pokemon deleted!", category="success")
        
    return jsonify({})


# Format the output
def parse_pokemon_data(record):
    # Pokemon can have multiple types, format into a single line before adding to final output.
    types = record["types"]
    poke_types = ""
    for type in types:
        poke_types += f"{type['type']['name']} "
    
    data = Pokemon(name=record["name"],number=record["id"],height=record["height"],weight=record["weight"],type=poke_types)
    return data