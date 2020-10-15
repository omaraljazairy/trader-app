from models.datainterface import DataManagerInterface

def test_has_attrib_get_query():
    """ test if the interface has a method called get_query."""

    assert hasattr(DataManagerInterface, 'get_query')