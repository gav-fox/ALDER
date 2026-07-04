import yaml 
from alder.core.species_record import SpeciesRecord
from alder.core.wrapped_value import WrappedValue
def load_species (file_path):
    with open (file_path, "r") as f:
        data = yaml.safe_load(f)
    species = SpeciesRecord (data["common_name"], data["latin_name"])
    species.species_data["crude_protein"] = WrappedValue(data["crude_protein"]["value"], data["crude_protein"]["units"], data["crude_protein"]["source"], data["crude_protein"]["confidence"])
    species.species_data["moisture"] = WrappedValue(data["moisture"]["value"], data["moisture"]["units"], data["moisture"]["source"], data["moisture"]["confidence"])
    species.species_data["fibre"] = WrappedValue(data["fibre"]["value"], data["fibre"]["units"], data["fibre"]["source"], data["fibre"]["confidence"])
    species.species_data["edible_yield"] = WrappedValue(data["edible_yield"]["value"],data["edible_yield"]["units"],data["edible_yield"]["source"],data["edible_yield"]["confidence"])
    species.species_data["mature_edible_yield"] = WrappedValue(data["mature_edible_yield"]["value"],data["mature_edible_yield"]["units"],data["mature_edible_yield"]["source"],data["mature_edible_yield"]["confidence"])
    species.species_data["pollard_edible_yield_5_year_regrowth"] = WrappedValue(data["pollard_edible_yield_5_year_regrowth"]["value"],data["pollard_edible_yield_5_year_regrowth"]["units"],data["pollard_edible_yield_5_year_regrowth"]["source"],data["pollard_edible_yield_5_year_regrowth"]["confidence"])
    species.species_data["cattle_palatability"] = WrappedValue(data["cattle_palatability"]["value"],data["cattle_palatability"]["units"],data["cattle_palatability"]["source"],data["cattle_palatability"]["confidence"])
    return species
