from abc import ABC, abstractmethod
from ..hhtp_types.http_request import HttpRequest
from ..hhtp_types.http_response import HttpResponse

@abstractmethod
class ViewInterface(ABC):
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass