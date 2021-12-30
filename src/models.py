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
    image = Column(String(150), nullable=False)
    descriptions = Column(String(200), nullable=False)
    comments = relationship('Comment', backref='room', lazy=True)

    receiptDetails = relationship('ReceiptDetail', backref='room', lazy=True)

class Receipt(BaseModel):
    visitor_name = Column(String(50), nullable=False)
    address = Column(String(100))
    price = Column(Float, default=0)

    receiptDetails = relationship('ReceiptDetail', backref='receipt', lazy=False)



class ReceiptDetail(db.Model):
    id = Column(Integer, ForeignKey(Receipt.id), primary_key=True, nullable=False, autoincrement=True)
    room_id = Column(Integer, ForeignKey(Room.id), primary_key=True, nullable=False)
    room_name = Column(String(100), nullable=False)
    price = Column(Float, default=0)
    quantity = Column(Integer, default=0)
    receive_day = Column(String(50), default=datetime.now())
    pay_day = Column(String(50), default=datetime.now())
    person_amount = Column(Integer)


class Comment(BaseModel):
    content = Column(String(255), nullable=False)
    room_id = Column(Integer, ForeignKey(Room.id), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    created_date = Column(DateTime, default=datetime.now())

    def __str__(self):
        return self.content


if __name__ == '__main__':
    db.create_all()
    # rooms = [
    #     {
    #         "quantity_bed": 2,
    #         "price": 70,
    #         "status": "Trống",
    #         "type_room_id": 1,
    #         "rental_voucher": 2
    #     },
    #     {
    #         "quantity_bed": 2,
    #         "price": 50,
    #         "status": "Trống",
    #         "type_room_id": 2,
    #         "rental_voucher": 1
    #     },
    #     {
    #         "quantity_bed": 3,
    #         "price": 70,
    #         "status": "Trống",
    #         "type_room_id": 3,
    #         "rental_voucher": 2
    #     },
    #     {
    #         "quantity_bed": 3,
    #         "price": 80,
    #         "status": "Trống",
    #         "type_room_id": 1,
    #         "rental_voucher": 2
    #     },
    #     {
    #         "quantity_bed": 3,
    #         "price": 80,
    #         "status": "Trống",
    #         "type_room_id": 2,
    #         "rental_voucher": 2
    #     },
    #     {
    #         "quantity_bed": 3,
    #         "price": 70,
    #         "status": "Trống",
    #         "type_room_id": 4,
    #         "rental_voucher": 2
    #     },
    #     {
    #         "quantity_bed": 3,
    #         "price": 90,
    #         "status": "Trống",
    #         "type_room_id": 3,
    #         "rental_voucher": 2
    #     }
    # ]
    # receipt_detail = [
    #     {
    #         "receipt_id": 1,
    #         "room_id": 4,
    #         "rental_date": datetime.now(),
    #         "price": 70,
    #         "total": 70
    #     },
    #     {
    #         "receipt_id": 2,
    #         "room_id": 5,
    #         "rental_date": datetime.now(),
    #         "price": 50,
    #         "total": 50
    #     },
    #     {
    #         "receipt_id": 3,
    #         "room_id": 6,
    #         "rental_date": datetime.now(),
    #         "price": 70,
    #         "total": 70
    #     },
    #     {
    #         "receipt_id": 4,
    #         "room_id": 7,
    #         "rental_date": datetime.now(),
    #         "price": 80,
    #         "total": 80
    #     },
    #     {
    #         "receipt_id": 5,
    #         "room_id": 8,
    #         "rental_date": datetime.now(),
    #         "price": 80,
    #         "total": 80
    #     },
    #     {
    #         "receipt_id": 6,
    #         "room_id": 9,
    #         "rental_date": datetime.now(),
    #         "price": 70,
    #         "total": 70
    #     },
    #     {
    #         "receipt_id": 7,
    #         "room_id": 10,
    #         "rental_date": datetime.now(),
    #         "price": 90,
    #         "total": 90
    #     },
    # ]
    #
    # for p in receipt_detail:
    #     room = ReceiptDetail(
    #                 receipt_id=p['receipt_id'],
    #                 room_id=p['room_id'],
    #                 rental_date=p['rental_date'],
    #                 price=p['price'],
    #                 total=p['total']
    #                 )
    #     db.session.add(room)
    #     db.session.commit()