from flask import request
from sqlalchemy import text, func, extract

from src import app, db
from src.models import Room, TypeRoom, ReceiptDetail, User, Receipt, ChangePolicyNumber, RentalVoucher, RentalVoucherDetail, TypeVisit
from sqlalchemy.orm import Session
from datetime import datetime


def get_all_type_rooms():
    return TypeRoom.query.all()


# Get used quantity type room in current month
def get_used_quantity_type_room_in_month():
    query = db.session.query(TypeRoom.id, TypeRoom.type_room_name, func.count(TypeRoom.id), ).filter(Room.type_room_id == TypeRoom.id).filter(Room.id == ReceiptDetail.room_id).filter(extract('month', ReceiptDetail.rental_date) == datetime.now().month).group_by(TypeRoom.id, TypeRoom.type_room_name)
    return query.all()