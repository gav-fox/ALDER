# This file is the bridge your whitepaper describes: Godot will talk to this
# over plain HTTP, and this file is the only thing that touches your Python
# backend directly. Godot never imports Python; it just sends a request here.

from fastapi import FastAPI

from alder.core.species_loader import load_species
from alder.modules.calculators import trees_per_cow

# FastAPI() creates the actual web application object. Everything below
# registers "routes" on it — rules for "when a request arrives at this
# URL, run this function and send back what it returns."
app = FastAPI()


# @app.get(...) is a decorator: it wraps the function below it and
# registers it as the handler for GET requests to /trees-per-cow.
# A GET request is the kind your browser sends just by visiting a URL.
@app.get("/trees-per-cow")
def get_trees_per_cow(browse_percent: float = 20.0):
    # browse_percent above is a query parameter with a default value.
    # A request to /trees-per-cow?browse_percent=15 sets it to 15;
    # a request to plain /trees-per-cow uses the default, 20.0.

    cow = load_species("data/species/english_longhorn_cattle.yaml")
    tree = load_species("data/species/goat_willow.yaml")

    trees_needed = trees_per_cow(cow, tree, browse_percent)

    # FastAPI automatically converts this dict into JSON before sending it
    # back — JSON is just a text format for structured data that both
    # Python and GDScript (and basically every language) can read.
    return {
        "trees_needed": trees_needed,
        "browse_percent": browse_percent,
    }
