from .person_finder_validator import person_finder_validator

class MockRequest:
    def __init__(self, param):
        self.param = param

def test_person_finder_validator():
    request = MockRequest({
        "person_id": 1
    })

    person_finder_validator(request)
