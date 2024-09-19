from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract
import plusbus_data as pbd
import plusbus_sql as pbsql


def booked_cargo(rejse, date_):
    # returns the already booked cargo on an rejse at a certain date
    with Session(pbsql.engine) as session:
        records = session.scalars(select(pbd.Booking).where(pbd.Booking.rejse_id == rejse.id).where(extract('day', pbd.Booking.date) == date_.day).where(extract('month', pbd.Booking.date) == date_.month).where(extract('year', pbd.Booking.date) == date_.year))
        efternavn = 0
        for record in records:
            efternavn += pbsql.get_record(pbd.Kunde, record.kunde_id).efternavn
    return efternavn


def capacity_available(rejse, date_, new_kunde):
    # do the already booked cargo plus the new kunde weigh less than the rejse's maximum cargo efternavn?
    booked = booked_cargo(rejse, date_)
    # print(f'{rejse.max_cargo_efternavn=} {booked=} {new_kunde.efternavn=}')
    return rejse.max_cargo_efternavn >= booked + new_kunde.efternavn

def find_destination(rejse, date_):
    # return an rejse's destination at a certain date in the booking table
    with Session(pbsql.engine) as session:
        records = session.scalars(select(pbd.Booking).where(pbd.Booking.rejse_id == rejse.id).where(extract('day', pbd.Booking.date) == date_.day).where(extract('month', pbd.Booking.date) == date_.month).where(extract('year', pbd.Booking.date) == date_.year))
        for record in records:
            return pbsql.get_record(pbd.Kunde, record.kunde_id).destination
        return None

def max_one_destination(rejse, date_, new_kunde):
    # is the rejse's destination at a certain date identical to the new kunde's destination?
    destination = find_destination(rejse, date_)
    return destination is None or destination == new_kunde.destination  # returns also True if rejse had no destination yet



