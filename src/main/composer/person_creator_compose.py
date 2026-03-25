from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.models.sqlite.settings.connection import db_connection_handler
from src.controller.person_create_controller import PersonCreatorControler
from src.view.person_creator_view import PersonCreatorView

def person_creator_compose():
    model = PeopleRepository(db_connection_handler)
    controler = PersonCreatorControler(model)
    view = PersonCreatorView(controler)

    return view