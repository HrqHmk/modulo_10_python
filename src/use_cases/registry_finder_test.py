from src.main.http_types.http_request import HttpRequest
from .registry_finder import RegistryFinder

class OrderRepositoryMock():
    def __init__(self):
        self.called_with = None

    def select_by_object_id(self, order_id: str)-> dict:
        self.called_with = order_id
        return { "_id": 1 }

def test_finder():
    repository = OrderRepositoryMock()
    use_case = RegistryFinder(repository)
    order_id = 1
    mock_finder = HttpRequest(
        path_params={
            "order_id":order_id
        }
    )

    response = use_case.find(mock_finder)

    assert response.body["data"]["attributes"] == { "_id": '1' }
    assert repository.called_with == order_id
