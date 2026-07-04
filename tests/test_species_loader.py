from alder.core.species_loader import load_species
def test_species_loader ():
    goat_willow = load_species("data/species/goat_willow.yaml")
    assert goat_willow ["common_name"] == "Goat Willow"


