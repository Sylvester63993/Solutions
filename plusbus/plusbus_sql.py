from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete
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
        new_items.append(Kunde(efternavn="Jørgensen", kontakt="11 22 33 44"))
        session.add_all(new_items)
        session.commit()


def select_all(classparam):  # https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))  # very useful for converting into our data class
        result = []
        for record in records:
            # print(record)
            result.append(record)
    return result


def get_record(classparam, record_id):  # https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    # return the record in classparams table with a certain id
    with Session(engine) as session:
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()  # very useful for converting into our data class
    return record


def create_record(record):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # create a record in the database
    with Session(engine) as session:
        record.id = None
        session.add(record)
        session.commit()  # makes changes permanent in database


def delete_hard_kunde(kunde):
    # delete a record in the kunde table
    with Session(engine) as session:
        session.execute(delete(Kunde).where(Kunde.id == kunde.id))
        session.commit()  # makes changes permanent in database

def delete_soft_kunde(kunde):
    # soft delete a record in the kunde table by setting its efternavn to -1 (see also method "valid" in the kunde class)
    with Session(engine) as session:
        session.execute(update(Kunde).where(Kunde.id == kunde.id).values(efternavn="#deleted", kontakt=kunde.kontakt))
        session.commit()  # makes changes permanent in database


if __name__ == "__main__":  # Executed when invoked directly
# The next 2 lines are needed _after_ data classes / sql tables were defined
    engine = create_engine(Database, echo=False, future=True)  
    Base.metadata.create_all(engine)
    # create_test_data()
    print(select_all(Kunde))
    print(get_record(Kunde, 2))
else:  # Executed when imported
    engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
    Base.metadata.create_all(engine)






