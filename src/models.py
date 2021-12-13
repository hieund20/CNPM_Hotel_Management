from sqlalchemy import Column, Integer, String, Float, Boolean, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src import db
from datetime import datetime
from enum import Enum as UserEnum


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class UserRole(UserEnum):
    ADMIN = 1
    USER = 2

class User(BaseModel):
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    joined_date = Column(DateTime, default=datetime.now())
    user_role = Column(Enum(UserRole), default=UserRole.USER)

class ChangePolicyNumber(BaseModel):
    foreign_visitor_number = Column(Float, nullable=True)
    domestic_visitor_number = Column(Float, nullable=True)
    quantity_types_visitors = Column(Integer, nullable=True)
    quantity_types_rooms = Column(Integer, nullable=True)
    max_visitors_in_a_room = Column(Integer, nullable=True)
    number_price = Column(Float, nullable=True)
    amount_extra = Column(Float, nullable=True)

class TypeVisit(BaseModel):
    type_visit_name = Column(String(50), nullable= False)

    rentalVoucherDetails = relationship('RentalVoucherDetail', backref='typeVisit', lazy=False)

class RentalVoucher(BaseModel):
    start_date = Column(DateTime, default=datetime.now())

    rooms = relationship('Room', backref='rentalVoucher', lazy=False)
    # def __str__(self):
    #     return self.id

class RentalVoucherDetail(BaseModel):
    visit_name = Column(String(50), nullable=True)
    type_visit_id = Column(Integer, ForeignKey(TypeVisit.id), primary_key=True, nullable=False)
    cart_id = Column(Integer, nullable=True)
    address = Column(String(100), nullable=True)
    phone_number = Column(Integer, nullable=True)
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

    receiptDetails = relationship('ReceiptDetail', backref='room', lazy=True)

class Receipt(BaseModel):
    visitor_name = Column(String(50), nullable=False)
    address = Column(String(100))
    price = Column(Float, default=0)

    receiptDetails = relationship('ReceiptDetail', backref='receipt', lazy=False)

class ReceiptDetail(BaseModel):
    receipt_id = Column(Integer, ForeignKey(Receipt.id), primary_key=True, nullable=False)
    room_id = Column(Integer, ForeignKey(Room.id), primary_key=True, nullable=False)
    rental_date = Column(DateTime, default=datetime.now())
    price = Column(Float, default=0)
    total = Column(Float, default=0)


if __name__ == '__main__':
    db.create_all()