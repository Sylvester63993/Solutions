from sqlalchemy.orm import Session
from sqlalchemy import select

import plusbus_data as pbd
import plusbus_sql as pbsql

# One could argue that function1 and function2 should be in the SQL layer,
# because they interact with the database. But since they are specifically written for
# function3 and function4 respectively, and are not called by other functions,
# it is also a good choice to keep them in the function layer.


def booked_seats(rejse):
    # returnerer hvor mange pladser der allerede er booket på en specifik rejse.
    with Session(pbsql.engine) as session:
        records = session.scalars(select(pbd.Booking).where(pbd.Booking.rejse_id == rejse.id))
        pladser = 0
        for record in records:
            pladser += pbsql.get_record(pbd.Booking, record.rejse_id).pladser
        return pladser


def capacity_available(rejse, new_booking):
    # overskrider de allerede bookede pladser plus den nye booking(new_booking) rejsens maksimale pladskapacitet?
    booked = booked_seats(rejse)
    # print(f'{rejse.pladskapacitet=} {booked=} {new_booking.pladser=}')
    return rejse.pladskapacitet >= booked + new_booking.pladser
