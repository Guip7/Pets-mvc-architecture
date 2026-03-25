from .pet_creator_validator import pet_creator_validator

class MockRequest:
    def __init__(self, body):
        self.body = body

def test_pet_creator_validator():
    request = MockRequest({
        "name": "Fluffy",
        "type": "Dog"
    })

    pet_creator_validator(request)
