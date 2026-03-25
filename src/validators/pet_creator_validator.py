from pydantic import BaseModel, constr, ValidationError
from ..view.hhtp_types.http_request import HttpRequest
from ..errors.error_type.http_unprocessable_entity import HttpUnprocessableEntity


def pet_creator_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        name: constr(min_length=3)  # type: ignore
        type: constr(min_length=3)  # type: ignore

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntity(e.errors())
