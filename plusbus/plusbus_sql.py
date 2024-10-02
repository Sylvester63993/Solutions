from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update, delete
from plusbus_data import Kunde, Rejse, Booking, Base

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
        new_items.append(Kunde(id=1, efternavn="Nielsen", kontakt="nielsen@mail.dk"))
        new_items.append(Kunde(id=2,efternavn="Larsen", kontakt="larsen@mail.dk"))
        new_items.append(Kunde(id=3,efternavn="Hansen", kontakt="+4510203040"))
        new_items.append(Kunde(id=4,efternavn="Jørgensen", kontakt="11 22 33 44"))
        # new_items.append(Rejse(id=10, rute="København-Berlin", dato="05032024" , pladskapacitet=100))
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
        
# region kunde
def update_kunde(kunde):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # update a record in the kunde table
    with Session(engine) as session:
        session.execute(update(Kunde).where(Kunde.id == kunde.id).values(efternavn=kunde.efternavn, kontakt=kunde.kontakt))
        session.commit()  # makes changes permanent in database


def delete_hard_kunde(kunde):
    # delete a record in the kunde table
    with Session(engine) as session:
        session.execute(delete(Kunde).where(Kunde.id == kunde.id))
        session.commit()  # makes changes permanent in database


def delete_soft_kunde(kunde):
    # soft delete a record in the kunde table by setting its attribute "efternavn" to the string "#deleted" (see also method "valid" in the kunde class)
    with Session(engine) as session:
        session.execute(update(Kunde).where(Kunde.id == kunde.id).values(efternavn="#deleted", kontakt=kunde.kontakt))
        session.commit()  # makes changes permanent in database
# endregion kunde

# region rejse
def update_rejse(rejse):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # update a record in the rejse table
    with Session(engine) as session:
        session.execute(update(Rejse).where(Rejse.id == rejse.id).values(rute=rejse.rute, dato=rejse.dato, pladskapacitet=rejse.pladskapacitet))
        session.commit()  # makes changes permanent in database


def delete_hard_rejse(rejse):
    # delete a record in the rejse table
    with Session(engine) as session:
        session.execute(delete(Rejse).where(Rejse.id == rejse.id))
        session.commit()  # makes changes permanent in database


def delete_soft_rejse(rejse):
    # soft delete a record in the rejse table by setting its attribute "efternavn" to the string "#deleted" (see also method "valid" in the rejse class)
    with Session(engine) as session:
        session.execute(update(Rejse).where(Rejse.id == rejse.id).values(rute=rejse.rute, dato=rejse.dato, pladskapacitet=-1))
        session.commit()  # makes changes permanent in database
# endregion rejse

# region booking
def update_booking(booking):  # https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#orm-enabled-update-statements
    # update a record in the booking table
    with Session(engine) as session:
        session.execute(update(Booking).where(Booking.id == booking.id).values(kunde_id=booking.kunde_id, rejse_id=booking.rejse_id, pladser=booking.pladser))
        session.commit()  # makes changes permanent in database


def delete_hard_booking(booking):
    # delete a record in the booking table
    with Session(engine) as session:
        session.execute(delete(Booking).where(Booking.id == booking.id))
        session.commit()  # makes changes permanent in database


def delete_soft_booking(booking):
    # soft delete a record in the booking table by setting its attribute "pladser" to "-1" (see also method "valid" in the booking class)
    with Session(engine) as session:
        session.execute(update(Booking).where(Booking.id == booking.id).values(kunde_id=booking.kunde_id, rejse_id=booking.rejse_id, pladser=-1))
        session.commit()  # makes changes permanent in database
# endregion booking


if __name__ == "__main__":  # Executed when invoked directly
# The next 2 lines are needed _after_ data classes / sql tables were defined
    engine = create_engine(Database, echo=False, future=True)  
    Base.metadata.create_all(engine)
    create_test_data()
    print(select_all(Kunde))
    print(get_record(Kunde, 2))
    print(select_all(Rejse))
    print(get_record(Rejse, 1))
    #  print(select_all(Booking))
    #  print(get_record(Booking, 1))
else:  # Executed when imported
    engine = create_engine(Database, echo=False, future=True)  # https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine. This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a connection pool for these database connections. The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.
    Base.metadata.create_all(engine)






