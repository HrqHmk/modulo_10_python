import pytest
from .registry_order_validator import registry_order_validator

def test_registry_order_validator():
    body = {
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

    registry_order_validator(body)

def test_registry_order_validator_with_error():
    body = {
        "data": {
            "name": "Jhon Doe",
            "address": "Jhon Street",
            "cupom": "error",
            "itens": [
                { "item": "Refrigerante", "quantity": 2},
                { "item": "Puzza", "quantity": 3}
            ]
        }
    }

    with pytest.raises(Exception):
        registry_order_validator(body)
