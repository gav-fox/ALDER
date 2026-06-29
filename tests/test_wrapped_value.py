from alder.core.wrapped_value import WrappedValue
def test_wrapped_value():
    alder_protein = WrappedValue (15.6, "%", "Agricology Tree Fodder Guide", "High")
    assert alder_protein.value == 15.6
    assert alder_protein.units == "%"
    assert alder_protein.source == "Agricology Tree Fodder Guide"
    assert alder_protein.confidence == "High"






