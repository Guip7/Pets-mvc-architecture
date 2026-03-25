#pylint: disable=unused-argument
from .find_person_controller import PersonFinderControler

class MockerPerson:
    def __init__(self, first_name, last_name, pet_name, pet_type):
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type
     
class MockPeopleRepository:
    def get_person(self, person_id: int):
        return MockerPerson(
            "Joe",
            "Doe",
            "Fluffy",
            "cat"
        )

def test_find():
    controller = PersonFinderControler(MockPeopleRepository())
    response = controller.find(123)

    expected_response = {
        "data": {
            "type": "Person",
            "count": 1,
            "atributtes": {
                "first_name": "Joe",
                "last_name": "Doe",
                "pet_name": "Fluffy",
                "pet_type": "cat"
            }
        }
    }

    assert response == expected_response