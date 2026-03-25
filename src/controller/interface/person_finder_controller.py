from abc import ABC, abstractmethod

class PersonFinderControlerInterface:
    @abstractmethod
    def find(self, person_id: int) -> dict:
        pass