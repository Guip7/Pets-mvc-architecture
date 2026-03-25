from ..controller.interface.pet_finder_controller import PetListControllerInterface
from .interface.view_interface import ViewInterface
from .hhtp_types.http_request import HttpRequest
from .hhtp_types.http_response import HttpResponse

class PetFinderView(ViewInterface):
    def __init__(self, controller: PetListControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.petfinder()
        return HttpResponse(status_code=201, body=body_response)