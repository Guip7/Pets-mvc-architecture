from..controller.person_finder_controller import PersonFinderControlerInterface
from .interface.view_interface import ViewInterface
from .hhtp_types.http_request import HttpRequest
from .hhtp_types.http_response import HttpResponse

class PersonFinderView(ViewInterface):
    def __init__(self, controller: PersonFinderControlerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.param.get("person_id")
        body_response = self.__controller.find(person_id)

        return HttpResponse(status_code=200, body=body_response)