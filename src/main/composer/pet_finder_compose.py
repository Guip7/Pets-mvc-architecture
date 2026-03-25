from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.controller.pet_finder_controller import PetListController
from src.view.pet_lister_vier import PetFinderView

def pet_finder_compose():
    model = PetsRepository(db_connection_handler)
    controller = PetListController(model)
    view = PetFinderView(controller)

    return view
