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


if __name__ == "__main__":  # Executed when invoked directly
# The next 2 lines are needed _after_ data classes / sql tables were defined
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
    # create_test_data()
    print(select_all(Kunde))
    print(get_record(Kunde, 2))





