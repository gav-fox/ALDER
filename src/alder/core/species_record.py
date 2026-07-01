class SpeciesRecord: 
    def __init__(self, common_name: str, latin_name: str):
        self.common_name = common_name
        self.latin_name = latin_name
        self.species_data = {}
        
        