from pytest_mock import mocker
from .pet_deleter_controller import PetDeleterController


def test_delete_test(mocker):
    mock_repository = mocker.Mocker()
    controller = PetDeleterController(mock_repository)
    controller.delete("Fofinho")

    mock_repository.detele.assert_called_once_with("Fofinho")