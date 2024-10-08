"""
Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Anvend det, du har lært i dette kapitel om databaser, på en første opgave.

Trin 1:
Opret en ny SQLite database "S2311_my_second_sql_database.db" i din solutions mappe.
Denne database skal indeholde 2 tabeller.
Den første tabel skal hedde "customers" og repræsenteres i Python-koden af en klasse kaldet "Customer".
Tabellen bruger sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "name", "address" og "age".
Definer selv fornuftige datatyper for attributterne.

Trin 2:
Den anden tabel skal hedde "products" og repræsenteres i Python-koden af en klasse kaldet "Product".
Denne tabel bruger også sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "product_number", "price" og "brand".

Trin 3:
Skriv en funktion create_test_data(), der opretter testdata for begge tabeller.

Trin 4:
Skriv en metode __repr__() for begge dataklasser, så du kan vise poster til testformål med print().

Til læsning fra databasen kan du genbruge de to funktioner select_all() og get_record() fra S2240_db_class_methods.py.

Trin 5:
Skriv hovedprogrammet: Det skriver testdata til databasen, læser dataene fra databasen med select_all() og/eller get_record() og udskriver posterne til konsollen med print().

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

from sqlalchemy.orm import declarative_base, Session  # install sqlalchemy with the command "pip install SQLAlchemy" in a terminal.
from sqlalchemy import Column, String, Integer  # the library sqlalchemy helps us to work with a database
from sqlalchemy import create_engine, select

# The next 2 lines are needed _before_ data classes / sql tables are defined
Database = 'sqlite:///S2311_my_first_sql_database.db'  # first part: database type, second part: file path
Base = declarative_base()  # creating the registry and declarative base classes - combined into one step. Base will serve as the base class for the ORM mapped classes we declare.

class Customer(Base):
    # this class declaration does 2 important things at once:
    # 1. as usual, it declares a class we can store data in, inside our python program.
    # 2. it creates a table in a sql database with the specified columns
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    age = Column(Integer)

    def __repr__(self):  # Only for testing/debugging purposes.
        return f"Customer({self.id=}    {self.name=}    {self.address=}    {self.age=})"

    def convert_to_tuple(self):  # Convert Customer to tuple
        return self.id, self.name, self.address, self.age

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Customer
        customer = Customer(id=tuple_[0], name=tuple_[1], address=tuple_[2], age=tuple_[3])
        return customer

    def valid(self):  # is this object a valid record of a person?
        try:
            value = int(self.age)
        except ValueError:
            return False
        return value >= 0


class Product(Base):
    # this class declaration does 2 important things at once:
    # 1. as usual, it declares a class we can store data in, inside our python program.
    # 2. it creates a table in a sql database with the specified columns
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    product_number = Column(Integer)
    price = Column(Integer)
    brand = Column(String)

    def __repr__(self):  # Only for testing/debugging purposes.
        return f"Product({self.id=}    {self.product_number=}    {self.price=}    {self.brand=})"

    def convert_to_tuple(self):  # Convert Product to tuple
        return self.id, self.product_number, self.price, self.brand

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Product
        product = Product(id=tuple_[0], name=tuple_[1], address=tuple_[2], age=tuple_[3])
        return product

    def valid(self):  # is this object a valid record of a person?
        try:
            value = int(self.price)
        except ValueError:
            return False
        return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to Product
        product = Product(id=tuple_[0], product_name=tuple_[1], price=tuple_[2], brand=tuple_[3])
        return product


def select_all(classparam):  # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result

def get_record(classparam, record_id):  # return the record in classparams table with a certain id   https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    with Session(engine) as session:
        # in the background this creates the sql query "select * from persons where id=record_id" when called with classparam=Person
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record

def create_test_data():  # Optional. Used to test data base functions before gui is ready.
    with Session(engine) as session:
        new_items = []
        new_items.append(Customer(id=61, name="John", address="Vej 123", age=50))
        # new_items.append(Product(id=20, product_name="tablet", price=200, brand="Samsung"))
        session.add_all(new_items)
        session.commit()


# https://docs.sqlalchemy.org/en/14/tutorial/engine.html   The start of any SQLAlchemy application is an object called the Engine.
# This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space
# called a connection pool for these database connections. The engine is typically a global object created just once for a particular
# database server, and is configured using a URL string which will describe how it should connect to the database host or backend.

# The next 2 lines are needed _after_ data classes / sql tables were defined
engine = create_engine(Database, echo=False, future=True)  # define engine
Base.metadata.create_all(engine)  # establish connection to database (and create if it does not exist yet)

# create_test_data()  # write some test data into the database

print(select_all(Customer))
print(get_record(Customer, 61))
print(Customer.convert_from_tuple((1, "name", "addresse", 21)))
# print(Customer.convert_to_tuple((2)))