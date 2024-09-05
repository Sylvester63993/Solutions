from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from plusbus_data import Kunde, Base

# add the following 7 lines to make foreign key constraints work  https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#sqlite-foreign-keys
from sqlalchemy.engine import Engine
from sqlalchemy import event
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

Database = 'sqlite:///plusbus.db'  # first part: database type, second part: file path

def create_test_data():  # Optional. Used to test database functions before gui is ready.
    with Session(engine) as session:
        new_items = []
        new_items.append(Kunde(efternavn="Nielsen", kontakt="nielsen@mail.dk"))
        new_items.append(Kunde(efternavn="Larsen", kontakt="larsen@mail.dk"))
        new_items.append(Kunde(efternavn="Hansen", kontakt="+4510203040"))
        new_items.append(Kunde(efternavn="Jørgensen", kontakt="11223344"))
        session.add_all(new_items)
        session.commit()

