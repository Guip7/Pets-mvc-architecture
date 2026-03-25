from ..controller.pet_deleter_controller import PetDeleterControllerInterface
from .interface.view_interface import ViewInterface
from .hhtp_types.http_request import HttpRequest
from .hhtp_types.http_response import HttpResponse

class PetDeleterView(ViewInterface):
    def __init__(self, controller: PetDeleterControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.param["name"]
        self.__controller.delete(name)

        return HttpResponse(status_code=204)