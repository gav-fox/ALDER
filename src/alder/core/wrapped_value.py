class WrappedValue:
    def __init__(self, value: float, units: str, source: str, confidence: str):
        self.value = value
        self.units = units
        self.source = source
        self.confidence = confidence
        
