from..controller.person_create_controller import PersonCreatorControlerInterface
from .interface.view_interface import ViewInterface
from .hhtp_types.http_request import HttpRequest
from .hhtp_types.http_response import HttpResponse
from src.validators.person_creator_validator import person_creator_validator

class PersonCreatorView(ViewInterface):
    def __init__(self, controller: PersonCreatorControlerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_creator_validator(http_request)
        person_info = http_request.body
        body_response = self.__controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response)