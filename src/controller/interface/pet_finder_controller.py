from abc import ABC, abstractmethod

class PetListControllerInterface:

    @abstractmethod
    def petfinder(self) -> dict:
        pass