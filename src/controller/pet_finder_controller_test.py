from .pet_finder_controller import PetListController
from ..models.sqlite.entities.pets import PetsTable
class MockListPets:
    def list_pets(self):
        return [
            PetsTable(name="Fluffy", type="cat", id=4),
            PetsTable(name="Doug", type="dog", id=22),
        ]


    def test_list(self):
        controller = PetListController(MockListPets())
        response = controller.petfinder()

        expected_response = {
            "data": {
                "type": "Pets",
                "count": 2,
                "atributtes": [
                    {"name": "Fluffy", "type": "cat", "id": 4},
                    {"name": "Doug", "type": "dog", "id": 22}
                ]
            }
        }

        assert response == expected_response