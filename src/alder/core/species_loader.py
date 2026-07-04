import yaml 
from alder.core.species_record import SpeciesRecord
def load_species (file_path):
    with open (file_path, "r") as f:
        data = yaml.safe_load(f)
    species = SpeciesRecord (data["common_name"], data["latin_name"])
    return species
