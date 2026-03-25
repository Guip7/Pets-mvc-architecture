from abc import ABC, abstractmethod

class PersonCreatorControlerInterface:

    @abstractmethod
    def create(self, person_info: dict) -> dict:
        pass