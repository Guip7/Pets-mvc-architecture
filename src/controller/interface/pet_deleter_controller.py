from abc import ABC, abstractmethod

class PetDeleterControllerInterface:

    @abstractmethod
    def delete(self, name: str) -> None:
        pass