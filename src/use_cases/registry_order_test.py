from src.main.http_types.http_request import HttpRequest
from .registry_order import RegistryOrder

class OrderRepositoryMock():
    def __init__(self)-> None:
        self.insert_document_att = {}

    def insert_document(self, document: dict)-> None:
        self.insert_document_att["document"] = document

class OrderRepositoryMockError():
    def insert_document(self, document: dict)-> None:
        raise Exception("Error")

def test_registry():
    repository = OrderRepositoryMock()
    registry_order = RegistryOrder(repository)

    mock_registry = HttpRequest(
        body={
            "data": {
                "name": "Jhon Doe",
                "address": "Jhon Street",
                "cupom": False,
                "itens": [
                    { "item": "Refrigerante", "quantity": 2},
                    { "item": "Puzza", "quantity": 3}
                ]
            }
        }
    )

    response = registry_order.registry(mock_registry)
    
    assert "name" in repository.insert_document_att["document"]
    assert "address" in repository.insert_document_att["document"]
    assert "created_at" in repository.insert_document_att["document"]
    
    assert response.status_code == 201
    assert response.body["data"]["type"] == "Order"

def test_registry_with_error():
    repository = OrderRepositoryMockError()
    registry_order = RegistryOrder(repository)

    mock_registry = HttpRequest(
        body={
            "data": {
                "name": "Jhon Doe",
                "address": "Jhon Street",
                "cupom": False,
                "itens": [
                    { "item": "Refrigerante", "quantity": 2},
                    { "item": "Puzza", "quantity": 3}
                ]
            }
        }
    )

    response = registry_order.registry(mock_registry)
    assert response.status_code == 400
