from abc import ABC, abstractmethod
from src.models.sqlite.entities.pets import PetsTable

class PetsRepositoryinterface(ABC):
    
    @abstractmethod
    def list_pets(self) -> list[PetsTable]:
        pass

    @abstractmethod
    def delete_pets(self, name: str) -> None:
        pass

    @abstractmethod
    def get_pet(self, pet_id: int) -> PetsTable:
        pass