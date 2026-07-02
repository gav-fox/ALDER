from alder.core.species_record import SpeciesRecord 
from alder.core.wrapped_value import WrappedValue
def test_nitrogen_fixation():
    red_clover = SpeciesRecord ("Red Clover", "Trifolium pratense",)
    red_clover.species_data["Nitrogen Fixing Amount"]= WrappedValue (200, "KG/HA/YR", "AHDB", "High")
    assert red_clover.common_name == "Red Clover"
    assert red_clover.latin_name == "Trifolium pratense"
    assert red_clover.species_data["Nitrogen Fixing Amount"].value == 200
    assert red_clover.species_data["Nitrogen Fixing Amount"].units == "KG/HA/YR"
    assert red_clover.species_data["Nitrogen Fixing Amount"].source == "AHDB"
    assert red_clover.species_data["Nitrogen Fixing Amount"].confidence == "High"
    assert red_clover.nitrogen_fixation(3) == 600
    



