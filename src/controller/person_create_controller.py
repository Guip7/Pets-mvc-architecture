from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
import re
from ..errors.error_type.hhtp_bad_request import HhtpBadRequest
from .interface.person_create_controller import PersonCreatorControlerInterface

class PersonCreatorControler(PersonCreatorControlerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def create(self, person_info: dict) -> dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__verify_name(first_name, last_name)
        self.__insert_person_in_db(first_name,  last_name, age, pet_id)
        formated_response = self. __format_response(person_info)
        return formated_response



    def __verify_name(self, first_name: str, last_name: str) -> None:
        non_valid_caracters = re.compile(r'[^a-zA-Z]')

        if non_valid_caracters.search(first_name) or non_valid_caracters.search(last_name):
            raise HhtpBadRequest("Caracter Invalido")
        

    def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int):
        self.__people_repository.insert_people(first_name, last_name, age, pet_id)

    def __format_response(self, person_info: dict) -> dict:
        return {
            "data":{
                "type": "Person",
                "count": 1,
                "attributes": person_info
                }
        }