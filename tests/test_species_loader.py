from alder.core.species_loader import load_species
def test_species_loader ():
    species = load_species("data/species/goat_willow.yaml")
    assert species.common_name == "Goat Willow"
    assert species.species_data["crude_protein"].value == 11.6


