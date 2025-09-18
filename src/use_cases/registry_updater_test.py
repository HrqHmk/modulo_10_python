from src.main.http_types.http_request import HttpRequest
from .registry_updater import RegistryUpdater

class OrderRepositoryMock():
    def __init__(self):
        self.order_id = None
        self.document = {}

    def edit_registry(self, order_id: str, update_fields: dict)-> dict:
        self.order_id = order_id
        self.document["document"] = update_fields

def test_update():
    repository = OrderRepositoryMock()
    use_case = RegistryUpdater(repository)
    order_id = 1
    mock_finder = HttpRequest(
        path_params={
            "order_id":order_id
        },
        body={
            "data": {
                "address": "teste"
            }
        }
    )

    response = use_case.update(mock_finder)

    assert response.status_code == 200
    assert "address" in repository.document["document"]
 