from sqlalchemy import text, func

from src import app, db
from src.models import Room, TypeRoom, ReceiptDetail, User, Receipt, ChangePolicyNumber, RentalVoucher, RentalVoucherDetail, TypeVisit
from sqlalchemy.orm import Session


def get_all_type_rooms():
    return TypeRoom.query.all()


def get_used_quantity_type_room_in_month():
    query = db.session.query(func.count(TypeRoom.id), TypeRoom.type_room_name).filter(Room.type_room_id == TypeRoom.id).filter(Room.id == ReceiptDetail.room_id).group_by(TypeRoom.type_room_name)
    return query.all()