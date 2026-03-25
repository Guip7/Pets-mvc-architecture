from src.models.sqlite.entities.pets import PetsTable
from .pets_repository import PetsRepository
from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock

class MockConnection():
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
    data=[
        (
            [mock.call.query(PetsTable)],
            [
                PetsTable(name="dog", type="dog"),
                PetsTable(name="cat", type="cat")
            ]
        )
    ]
)

    def __enter__(self): 
        return self
    def __exit__(self, exc_type, exc, tb): 
        pass

def test_list_pet():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable) # metodo para ver cada um dos metodos
    mock_connection.session.all.assert_called_once_with()
    #mock_connection.session.filter.assert_called_once_with()

    assert response[0] == "dog"

def test_delete_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)

    repo.delete_pets("PetName")

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(PetsTable.name == "PetName")
    mock_connection.session.delete.assert_called_once_with()
