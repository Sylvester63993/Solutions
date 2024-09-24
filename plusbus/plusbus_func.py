from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import extract

import plusbus_data as pbd
import plusbus_sql as pbsql

# One could argue that function1 and function2 should be in the SQL layer,
# because they interact with the database. But since they are specifically written for
# function3 and function4 respectively, and are not called by other functions,
# it is also a good choice to keep them in the function layer.

def booked_cargo(aircraft, date_):
    # returns the already booked cargo on an aircraft at a certain date
    with Session(pbsql.engine) as session:
        records = session.scalars(select(pbd.Booking).where(pbd.Booking.aircraft_id == aircraft.id).where(extract('day', pbd.Booking.date) == date_.day).where(extract('month', pbd.Booking.date) == date_.month).where(extract('year', pbd.Booking.date) == date_.year))
        weight = 0
        for record in records:
            weight += pbsql.get_record(pbd.Container, record.container_id).weight
    return weight


def capacity_available(aircraft, date_, new_container):
    # do the already booked cargo plus the new container weigh less than the aircraft's maximum cargo weight?
    booked = booked_cargo(aircraft, date_)
    # print(f'{aircraft.max_cargo_weight=} {booked=} {new_container.weight=}')
    return aircraft.max_cargo_weight >= booked + new_container.weight


def find_destination(aircraft, date_):
    # return an aircraft's destination at a certain date in the transport table
    with Session(pbsql.engine) as session:
        records = session.scalars(select(pbd.Booking).where(pbd.Booking.aircraft_id == aircraft.id).where(extract('day', pbd.Booking.date) == date_.day).where(extract('month', pbd.Booking.date) == date_.month).where(extract('year', pbd.Booking.date) == date_.year))
        for record in records:
            return pbsql.get_record(pbd.Container, record.container_id).destination
        return None


def max_one_destination(aircraft, date_, new_container):
    # is the aircraft's destination at a certain date identical to the new container's destination?
    destination = find_destination(aircraft, date_)
    return destination is None or destination == new_container.destination  # returns also True if aircraft had no destination yet
