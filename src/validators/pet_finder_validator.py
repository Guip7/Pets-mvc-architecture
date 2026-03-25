from pydantic import BaseModel, ValidationError
from ..view.hhtp_types.http_request import HttpRequest
from ..errors.error_type.http_unprocessable_entity import HttpUnprocessableEntity


def pet_finder_validator(http_request: HttpRequest) -> None:

    class ParamData(BaseModel):
        pet_id: int

    try:
        ParamData(**http_request.param)
    except ValidationError as e:
        raise HttpUnprocessableEntity(e.errors())
