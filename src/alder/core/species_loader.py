import yaml 
from alder.core.species_record import SpeciesRecord
from alder.core.wrapped_value import WrappedValue
def load_species (file_path):
    with open (file_path, "r") as f:
        data = yaml.safe_load(f)
    species = SpeciesRecord (data["common_name"], data["latin_name"])
    for key in data:
        item = data[key]
        if isinstance(item, dict) and "value" in item:
            species.species_data[key] = WrappedValue(item["value"], item["units"], item["source"], item["confidence"])
    return species

