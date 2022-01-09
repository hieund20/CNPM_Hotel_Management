from jinja2 import meta
from sqlalchemy import Column, Integer, String, Float, Boolean, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src import db
from datetime import datetime
from enum import Enum as UserEnum
from flask_login import UserMixin


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class UserRole(UserEnum):
    ADMIN = 1
    USER = 2
    EMPLOYEE = 3


class User(BaseModel, UserMixin):
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    avatar = Column(String(200), default='')
    joined_date = Column(DateTime, default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    comments = relationship('Comment', backref='user', lazy=True)


class ChangePolicyNumber(BaseModel):
    foreign_visitor_number = Column(Float, nullable=True)
    domestic_visitor_number = Column(Float, nullable=True)
    quantity_types_visitors = Column(Integer, nullable=True)
    quantity_types_rooms = Column(Integer, nullable=True)
    max_visitors_in_a_room = Column(Integer, nullable=True)
    number_price = Column(Float, nullable=True)
    amount_extra = Column(Float, nullable=True)


class TypeVisit(BaseModel):
    type_visit_name = Column(String(50), nullable=False)

    rentalVoucherDetails = relationship('RentalVoucherDetail', backref='typeVisit', lazy=False)


class RentalVoucher(BaseModel):
    booking_date = Column(DateTime, default=datetime.now())
    rooms = relationship('Room', backref='rentalVoucher', lazy=False)


class RentalVoucherDetail(BaseModel):
    visit_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    visit_name_id = Column(Integer, nullable=False)
    nation = Column(String(100), nullable=True)
    phone_number = Column(Integer, nullable=True)
    type_visit_id = Column(Integer, ForeignKey(TypeVisit.id), primary_key=True, nullable=False)
    rental_voucher_id = Column(Integer, ForeignKey(RentalVoucher.id), primary_key=True, nullable=False)


class TypeRoom(BaseModel):
    type_room_name = Column(String(50), nullable=False)

    rooms = relationship('Room', backref='typeRoom', lazy=False)

    def __str__(self):
        return self.type_room_name


class Room(BaseModel):
    quantity_bed = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String(50), default="GOOD")
    type_room_id = Column(Integer, ForeignKey(TypeRoom.id), nullable=False)
    rental_voucher = Column(Integer, ForeignKey(RentalVoucher.id), default=0)
    image = Column(String(150), nullable=False)
    descriptions = Column(String(20000), nullable=False)
    comments = relationship('Comment', backref='room', lazy=True)

    receiptDetails = relationship('ReceiptDetail', backref='room', lazy=True)


class Receipt(BaseModel):
    visitor_name = Column(String(50), nullable=False)
    address = Column(String(100))
    price = Column(Float, default=0)
    user_id = Column(Integer, nullable=False)


class ReceiptDetail(db.Model):
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    room_id = Column(Integer, ForeignKey(Room.id), primary_key=True, nullable=False)
    room_name = Column(String(100), nullable=False)
    price = Column(Float, default=0)
    quantity = Column(Integer, default=0)
    receive_day = Column(String(50), default=datetime.now())
    pay_day = Column(String(50), default=datetime.now())
    person_amount = Column(Integer)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=True)


class BookingRoom(db.Model):
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    room_id = Column(Integer, ForeignKey(Room.id), primary_key=True, nullable=False)
    room_name = Column(String(100), nullable=False)
    image = Column(String(150), nullable=False)
    price = Column(Float, default=0)
    receive_day = Column(String(50), default=datetime.now())
    pay_day = Column(String(50), default=datetime.now())
    person_amount = Column(Integer)
    rental_voucher_detail_id = Column(Integer, ForeignKey(RentalVoucherDetail.id), nullable=True)


class Comment(BaseModel):
    content = Column(String(2000), nullable=False)
    room_id = Column(Integer, ForeignKey(Room.id), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    created_date = Column(DateTime, default=datetime.now())

    def __str__(self):
        return self.content


if __name__ == '__main__':
    db.create_all()
