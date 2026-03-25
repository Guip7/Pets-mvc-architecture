from ..models.sqlite.entities.people import PeopleTable
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from ..errors.error_type.http_not_found import HttpNotFoundEroor
from .interface.person_finder_controller import PersonFinderControlerInterface
class PersonFinderControler(PersonFinderControlerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def find(self, person_id: int) -> dict:
        person = self.__find_person_db(person_id)
        response = self.__format_response(person)
        return response

    def __find_person_db(self, person_id: int) -> PeopleTable:
        person = self.__people_repository.get_person(person_id)
        if not person:
            raise HttpNotFoundEroor("Pessoa nao encontrada")
        
        return person
    
    def __format_response(self, person: PeopleTable) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "atributtes": {
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name": person.pet_name,
                    "pet_type": person.pet_type
                }
            }
        }