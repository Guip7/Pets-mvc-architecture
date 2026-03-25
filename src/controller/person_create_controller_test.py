import pytest
from .person_create_controller import PersonCreatorControler

class MockPeopleRepository:
    def insert_people(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass


def test_create_person_success():
    person_info = {
        "first_name": "Fulano",
        "last_name": "deTal",
        "age": 30,
        "pet_id": 123
    }

    controller = PersonCreatorControler(MockPeopleRepository())

    response = controller.create(person_info)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info


def test_create_person_invalid_name():
    person_info = {
        "first_name": "Fulano123",
        "last_name": "deTal",
        "age": 30,
        "pet_id": 123
    }

    controller = PersonCreatorControler(MockPeopleRepository())

    with pytest.raises(Exception) as exc:
        controller.create(person_info)

    assert str(exc.value) == "Caracter Invalido"