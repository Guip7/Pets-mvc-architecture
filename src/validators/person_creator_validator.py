from pydantic import BaseModel, constr, ValidationError
from ..view.hhtp_types.http_request import HttpRequest
from ..errors.error_type.http_unprocessable_entity import HttpUnprocessableEntity


def person_creator_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        first_name: constr(min_length=5)  # type: ignore
        last_name: constr(min_length=5)   # type: ignore
        age: int
        pet_id: int

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntity(e.errors())