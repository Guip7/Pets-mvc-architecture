from .pet_finder_validator import pet_finder_validator

class MockRequest:
    def __init__(self, param):
        self.param = param

def test_pet_finder_validator():
    request = MockRequest({
        "pet_id": 1
    })

    pet_finder_validator(request)
