from alder.core.species_record import SpeciesRecord
from alder.core.wrapped_value import WrappedValue
def test_wrapped_value_species_record():
    red_clover = SpeciesRecord ("Red Clover", "Trifolium pratense",)
    red_clover.species_data["Nitrogen Fixing Amount"]= WrappedValue (200, "KG/HA", "AHDB", "High")
    assert red_clover.common_name == "Red Clover"
    assert red_clover.latin_name == "Trifolium pratense"
    assert red_clover.species_data["Nitrogen Fixing Amount"].value == 200
    assert red_clover.species_data["Nitrogen Fixing Amount"].units == "KG/HA"
    assert red_clover.species_data["Nitrogen Fixing Amount"].source == "AHDB"
    assert red_clover.species_data["Nitrogen Fixing Amount"].confidence == "High"
    