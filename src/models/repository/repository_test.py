import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip(reason="interaction with db")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"something": "something", "valor": 4}
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason="interaction with db")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_doc = [{"elem1": "valor1"}, {"elem2": "valor2"}, {"elem3": "valor3"}]
    orders_repository.insert_list_of_documents(my_doc)

@pytest.mark.skip(reason="interaction with db")
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "cupom": False }
    response = orders_repository.select_many(doc_filter)
    print()
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="interaction with db")
def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "cupom": False }
    response = orders_repository.select_one(doc_filter)
    print()
    print(response)

@pytest.mark.skip(reason="interaction with db")
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "cupom": False }
    response = orders_repository.select_many_with_properties(doc_filter)
    print()
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="interaction with db")
def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_property_exists()
    print()
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="interaction with db")
def test_select_many_with_multiple_filters():
    orders_repository = OrdersRepository(conn)
    doc_filter = { 
        "cupom": True,
        "itens.refrigerante": { "$exists": True }
    } # semelhante a busca And em sql
    response = orders_repository.select_many(doc_filter)
    print()
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="interaction with db")
def test_select_many_with_or_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = { 
        "$or": [
            { "address": { "$exists": True}},
            { "itens.refrigerante.tipo": "coca"}
        ]
    } # semelhante a busca Or em sql
    response = orders_repository.select_many(doc_filter)
    print()
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="interaction with db")
def test_select_by_object_id():
    orders_repository = OrdersRepository(conn)
    object_id = "68c1559c21f0c5b3d9789dd7"
    response = orders_repository.select_by_object_id(object_id)
    print()
    print(response)

@pytest.mark.skip(reason="interaction with db")
def test_edit_registry():
    orders_repository = OrdersRepository(conn)
    object_id = "68c157e321f0c5b3d9789ddc"
    orders_repository.edit_registry(object_id)

@pytest.mark.skip(reason="interaction with db")
def test_edit_many_rehistries():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_many_registries()

@pytest.mark.skip(reason="interaction with db")
def test_edit_registry_with_increment():
    orders_repository = OrdersRepository(conn)
    object_id = "68c157e321f0c5b3d9789ddc"
    orders_repository.edit_registry_with_increment(object_id)
