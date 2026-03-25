from ..models.sqlite.interfaces.pets_repository import PetsRepositoryinterface
from ..models.sqlite.entities.pets import PetsTable
from .interface.pet_finder_controller import PetListControllerInterface
class PetListController(PetListControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryinterface) -> None:
        self.__pet_repository = pet_repository # Pega todos os metodos do nosso repository

    def petfinder(self) -> dict:
        pets = self.__find_pet_in_db()
        response = self.__format_response(pets)
        return response
    
    def __find_pet_in_db(self) -> list[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets
    
    def __format_response(self, pets: list[PetsTable]) -> dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({"name": pet.name, "type": pet.type, "id": pet.id})
        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pets),
                "atributtes": formatted_pets
            }
        }