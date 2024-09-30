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

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to type Kunde
        kunde = Kunde(id=tuple_[0], efternavn=tuple_[1], kontakt=tuple_[2])
        return kunde

    def valid(self):
        return self.efternavn != "#deleted"


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

    # @staticmethod
    # def convert_from_tuple(tuple_):  # Convert tuple to type Rejse
        # rejse = Rejse(id=tuple_[0], rute=tuple_[1], dato=tuple_[2], pladskapacitet=tuple_[3])
        # return rejse

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to type rejse
        try:
            if tuple_[0] != '':
                id_ = int(tuple_[0])
            else:
                id_ = 0
            rute = str(tuple_[1])
            dato = parser.parse(tuple_[2])
            pladskapacitet = int(tuple_[3])
            rejse = Rejse(id=id_, rute=rute, dato=dato, pladskapacitet=pladskapacitet)
            return rejse
        except:
            messagebox.showwarning("", "Entries could not be converted to rejse!")

    def valid(self):
        try:
            # if self.pladskapacitet:
            value = int(self.pladskapacitet)
            # else:
                # value = 0
        except ValueError:
            return False
        return value >= 0


class Booking(Base):
    __tablename__ = "booking"
    id = Column(Integer, primary_key=True)
    kunde_id = Column(Integer, ForeignKey("kunde.id"), nullable=False)
    rejse_id = Column(Integer, ForeignKey("rejse.id"), nullable=False)
    pladser = Column(Integer)
    
    def __repr__(self):  # Optional. Only for test purposes.
        return f"Rejse({self.id=:4}    {self.kunde_id=:5}    {self.rejse_id=}    {self.pladser=})"

    def convert_to_tuple(self):  # Convert type Booking to a tuple
        return self.id, self.kunde_id, self.rejse_id, self.pladser

    @staticmethod
    def convert_from_tuple(tuple_):  # Convert tuple to object-type rejse
        try:
            # if tuple_[0] != '':  # unnecessary precaution
            #     id_ = int(tuple_[0])
            # else:
            #     id_ = 0
            pladser = int(tuple_[3])
            if pladser < 0:
                messagebox.showwarning("", "Pladser kan ikke være en negativ værdi!")
            else:
                booking = Booking(id=tuple_[0], kunde_id=tuple_[1], rejse_id=tuple_[2], pladser=pladser)
                # rejse = Rejse(id=id_, max_cargo_weight=max_cargo_weight, registration=tuple_[2])
                return booking
        except:
            messagebox.showwarning("", "Entries could not be converted to booking!")

    def valid(self):
        try:
            value = int(self.pladser)
        except ValueError:
            return False
        return value >= 0
    
    