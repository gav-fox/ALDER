from alder.core.species_record import SpeciesRecord
def test_species_record():
    red_clover = SpeciesRecord ("Red Clover", "Trifolium pratense")
    assert red_clover.common_name == "Red Clover"
    assert red_clover.latin_name == "Trifolium pratense" 
    assert red_clover.species_data == {}
    

