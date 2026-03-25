from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.controller.person_finder_controller import PersonFinderControler
from src.view.find_person_view import PersonFinderView

def person_finder_compose():
    model = PeopleRepository(db_connection_handler)
    controller = PersonFinderControler(model)
    view = PersonFinderView(controller)

    return view
