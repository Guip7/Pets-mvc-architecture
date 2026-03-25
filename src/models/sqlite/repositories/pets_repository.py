from sqlalchemy.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable
from ..interfaces.pets_repository import PetsRepositoryinterface

class PetsRepository(PetsRepositoryinterface):
    def __init__(self, dbconnection) -> None:
        self.__db_connection = dbconnection

    def list_pets(self) -> list[PetsTable]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all() #retorna todos as informações da tabela em questão
                return pets
            except NoResultFound:
                return []
            
    def delete_pets(self, name: str) -> None:
        with self.__db_connection as database:
            try:
                database.session.query(PetsTable).filter(PetsTable.name == name).delete() # nomes batendo
                database.session.commit()
            except Exception as exception:
                database.session.rollback() # Reseta o banco
                raise exception
    
    def get_pet(self, pet_id: int) -> PetsTable:
        with self.__db_connection as database:
            try:
                pet = (database.session
                    .query(PetsTable)
                    .filter(PetsTable.id == pet_id)
                    .one()
                )
                return pet
            except NoResultFound:
                return None