from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, Date

from dateutil import parser
from tkinter import messagebox


# The next 2 lines are needed _before_ data classes / sql tables are defined
Base = declarative_base()  # creating the registry and declarative base classes - combined into one step. Base will serve as the base class for the ORM mapped classes we declare.

class Kunde(Base):
    __tablename__ = "kunde"
    id = Column(Integer, primary_key=True)
    efternavn = Column(String)
    kontakt = Column(String)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Kunde({self.id=:4}    {self.efternavn=:5}    {self.kontakt=})"

    def convert_to_tuple(self):  # Convert type Kunde to a tuple
        return self.id, self.efternavn, self.kontakt

    # def valid(self):
    #     try:
    #         value = int(self.efternavn)
    #     except ValueError:
    #         return False
    #     return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to type Kunde
        kunde = Kunde(id=tuple_[0], efternavn=tuple_[1], kontakt=tuple_[2])
        return kunde

    
class Rejse(Base):
    __tablename__ = "rejse"
    id = Column(Integer, primary_key=True)
    rute = Column(String)
    dato = Column(Date)
    pladskapacitet = Column(Integer)

    def __repr__(self):  # Optional. Only for test purposes.
        return f"Rejse({self.id=:4}    {self.rute=:5}    {self.dato=}    {self.pladskapacitet=})"

    def convert_to_tuple(self):  # Convert type Rejse to a tuple
        return self.id, self.rute, self.dato, self.pladskapacitet

    # def valid(self):
    #     try:
    #         value = int(self.rute)
    #     except ValueError:
    #         return False
    #     return value >= 0

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to type Rejse
        rejse = Rejse(id=tuple_[0], rute=tuple_[1])
        return rejse

class Booking(Base):
    __tablename__ = "booking"
    kunde_id = Column(Integer, primary_key=True)
    rejse_id = Column(String)
    pladser = Column(Integer)
    
    def __repr__(self):  # Optional. Only for test purposes.
        return f"Rejse({self.kunde_id=:4}    {self.rejse_id=:5}    {self.pladser=})"

    def convert_to_tuple(self):  # Convert type Rejse to a tuple
        return self.kunde_id, self.rejse_id, self.pladser
    
    