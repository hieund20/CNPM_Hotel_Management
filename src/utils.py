from flask import request
from sqlalchemy import text, func, extract

from src import app, db
from src.models import Room, TypeRoom, ReceiptDetail, User, Receipt, ChangePolicyNumber, RentalVoucher, RentalVoucherDetail, TypeVisit
from sqlalchemy.orm import Session
from datetime import datetime
import hashlib


def get_all_type_rooms():
    return TypeRoom.query.all()


# Get used quantity type room in current month
def get_used_quantity_type_room_in_month():
    query = db.session.query(TypeRoom.id, TypeRoom.type_room_name, func.count(TypeRoom.id), ).filter(Room.type_room_id == TypeRoom.id).filter(Room.id == ReceiptDetail.room_id).filter(extract('month', ReceiptDetail.rental_date) == datetime.now().month).group_by(TypeRoom.id, TypeRoom.type_room_name)
    return query.all()


def add_user(username, password, email):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(username=username.strip(), password=password,
                email=email)

    db.session.add(user)
    db.session.commit()



def check_login(username, password):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest()) #hash bằng md5 khi create password thì cũng hash bằng md5 khi login

        return User.query.filter(User.username.__eq__(username.strip()),
                                User.password.__eq__(password)).first()



def get_user_by_id(user_id):
    return User.query.get(user_id)

def count_cart(cart):
    quantity, amount= 0, 0
    if cart:
        for i in cart.values():
            quantity += i['quantity']
            amount += i['quantity'] * i['price']
    return {
        'totalQuantity': quantity,
        'totalAmount': amount
    }

def is_name_in_receipt(name):
    return Receipt.query.filter(Receipt.visitor_name.__eq__(name)).first()



def add_receipt(name, address, price):
    new = Receipt(visitor_name = name, address= address, price = price)
    db.session.add(new)
    db.session.commit()

def add_receipt_detail(receipt_id, room_id, price, user_id):
    new = ReceiptDetail(receipt_id= receipt_id, room_id= room_id, price = price, user_id = user_id)
    db.session.add(new)
    db.session.commit()

def get_user_by_name(name):
    return User.query.filter(User.username.__eq__(name)).first()