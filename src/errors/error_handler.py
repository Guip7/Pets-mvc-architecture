from src.view.hhtp_types.http_response import HttpResponse
from .error_type.hhtp_bad_request import HhtpBadRequest
from .error_type.http_unprocessable_entity import HttpUnprocessableEntity
from .error_type.http_not_found import HttpNotFoundEroor

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpUnprocessableEntity, HhtpBadRequest, HttpNotFoundEroor)):
        return HttpResponse(
            status_code=error.status_code,
            body ={
                "error": [{
                    "title": error.name,
                    "detail": error.message,
                }]
                }
        )
    return HttpResponse(
            status_code=500,
            body ={
                "error": [{
                    "title": "Server Errors",
                    "detail": str(error),
                }]
                }
        )