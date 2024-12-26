from .connection import DBConnetionHandler

def test_create_database_engine():
    connection = DBConnetionHandler()

    engine = connection.get_engine()

    assert engine is not None