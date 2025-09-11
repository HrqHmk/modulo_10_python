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
