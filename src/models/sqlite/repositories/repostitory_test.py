import pytest
from ..settings.connection import db_connection_handler
from .people_repository import PeopleRepository
from .pets_repository import PetsRepository

# db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Interação com o banco")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)
    
@pytest.mark.skip(reason="Interação com o banco")
def test_delete_pet():
    name = "belinha"
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)

@pytest.mark.skip(reason="Interação com o banco")
def test_insert_people():
    first_name = "first_name"
    last_name = "last_name"
    age = 22
    pet_id = 2

    repo = PeopleRepository(db_connection_handler) #responsavel pela conexão do banco
    repo.insert_people(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason="Interação com o banco")
def test_get_person():
    person_id = 1
    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print()
    print(response)