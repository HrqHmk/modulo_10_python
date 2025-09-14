from bson import ObjectId
from .orders_repository import OrdersRepository

class CollectionMock:
    def __init__(self)-> None:
        self.insert_one_attributes = {}
        self.find_attributes = {}
        self.edit_attrbitutes = {}

    def insert_one(self, input_data: any)-> None:
        self.insert_one_attributes["dict"] = input_data

    def find(self, *args):
        self.find_attributes["args"] = args
    
    def update_one(self, *args):
        self.edit_attrbitutes["args"] = args
    
class DbCollectionMock:
    def __init__(self, collection)-> None:
        self.get_collection_attributes = {}
        self.collection = collection
        
    def get_collection(self, collection_name):
        self.get_collection_attributes["name"] = collection_name
        return self.collection

def test_insert_documents():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repository = OrdersRepository(db_connection)

    document = { "test": "test" }
    repository.insert_document(document)

    assert collection.insert_one_attributes["dict"] == document

def test_select_many_with_properties():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repository = OrdersRepository(db_connection)

    document = { "test": "find" }
    repository.select_many_with_properties(document)

    assert collection.find_attributes["args"][0] == document
    assert collection.find_attributes["args"][1] == {'_id': 0, 'cupom': 0}

def test_edit_registry():
    collection = CollectionMock()
    db_connection = DbCollectionMock(collection)
    repository = OrdersRepository(db_connection)

    object_id = "68c1559c21f0c5b3d9789dd7"
    repository.edit_registry(object_id)

    assert collection.edit_attrbitutes["args"][0]["_id"] == ObjectId(object_id)
