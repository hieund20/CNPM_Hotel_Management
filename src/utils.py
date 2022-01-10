from sqlalchemy import func, extract
import hashlib
from datetime import datetime

import mysql.connector
from sqlalchemy import desc, asc
from sqlalchemy import func, extract

from src import app, db
from src.models import Room, TypeRoom, ReceiptDetail, User, Receipt, RentalVoucher, \
    RentalVoucherDetail, BookingRoom

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database="hotel"
)


def get_all_type_rooms():
    return TypeRoom.query.all()


# Get used quantity type room in current month
def get_used_quantity_type_room_in_month():
    query = db.session.query(TypeRoom.id, TypeRoom.type_room_name, func.count(TypeRoom.id), ).filter(
        Room.type_room_id == TypeRoom.id).filter(Room.id == ReceiptDetail.room_id).filter(
        extract('month', ReceiptDetail.receive_day) == datetime.now().month).group_by(TypeRoom.id,
                                                                                      TypeRoom.type_room_name)
    return query.all()


def add_user(username, password, email):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    user = User(username=username.strip(), password=password,
                email=email)

    db.session.add(user)
    db.session.commit()


def check_login(username, password):
    if username and password:
        password = str(hashlib.md5(password.strip().encode(
            'utf-8')).hexdigest())  # hash bằng md5 khi create password thì cũng hash bằng md5 khi login

        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password)).first()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def count_cart(cart):
    quantity, amount = 0, 0
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
    new = Receipt(visitor_name=name, address=address, price=price)
    db.session.add(new)
    db.session.commit()


def get_user_by_name(name):
    return User.query.filter(User.username.__eq__(name)).first()


def get_all_rooms(page):
    page_size = app.config['PAGE_SIZE']
    start = (page - 1) * page_size
    end = start + page_size

    query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id,
                             Room.rental_voucher, Room.image, Room.descriptions, TypeRoom.type_room_name).filter(
        Room.type_room_id == TypeRoom.id)

    return query.slice(start, end).all()


def get_room_by_id(room_id):
    return Room.query.get(room_id)


def get_type_room_by_room_id(room_id):
    query = db.session.query(TypeRoom.type_room_name).filter(Room.type_room_id == TypeRoom.id).filter(
        Room.id == room_id)
    return query.all()


def cart_stats(cart):
    total_amount, total_quantity = 0, 0
    if cart:
        for p in cart.values():
            total_quantity += p["quantity"]
            total_amount = p["price"]

    return total_quantity, total_amount


def add_receipt_detail(room_id, room_name, price, quantity, receive_day, pay_day, person_amount):
    receipt_detail = ReceiptDetail(room_id=room_id,
                                   room_name=room_name,
                                   price=price,
                                   quantity=quantity,
                                   receive_day=receive_day,
                                   pay_day=pay_day,
                                   person_amount=person_amount)
    db.session.add(receipt_detail)
    db.session.commit()


def get_user_by_name(name):
    return User.query.filter(User.username.__eq__(name)).first()


def total_room_by_receiptId(receipt_id):
    # receipt=ReceiptDetail.query.filter(ReceiptDetail.user_id.__eq__(user_id))
    # receipt=ReceiptDetail.query.all()
    # return  db.session.query(func.count(ReceiptDetail.id))

    return ReceiptDetail.query.all()


def get_list_receipt_detail():
    # list=ReceiptDetail.query.filter(ReceiptDetail.receipt_id.__eq__(receipt_id))
    query = db.session.query(Room.image, ReceiptDetail.room_name, ReceiptDetail.id, ReceiptDetail.pay_day,
                             ReceiptDetail.price, ReceiptDetail.quantity, ReceiptDetail.receive_day,
                             ReceiptDetail.person_amount, Room.id).filter(Room.id == ReceiptDetail.room_id)
    print('query default', query)
    return query.all()


def total_money(user_id):
    # rd = ReceiptDetail.query.filter(ReceiptDetail.user_id.__eq__(user_id))
    rd = ReceiptDetail.query.all()
    total = 0
    for r in rd:
        total += r.price
    return total


def delete_Receipt_detail(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM receipt_detail WHERE id = " + id
    mycursor.execute(sql)
    mydb.commit()


def count_rooms(type_room_id, quantity_bed, price_order_by):
    query = ""
    if (type_room_id == '' and quantity_bed == '' and price_order_by == '') or \
            (type_room_id is None and quantity_bed is None and price_order_by is None):
        query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                 Room.descriptions, TypeRoom.type_room_name).filter(
            Room.type_room_id == TypeRoom.id).order_by(asc(Room.price))
    if price_order_by == 'asc':
        if quantity_bed == '' and type_room_id == '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).order_by(asc(Room.price))
        if quantity_bed == '' and type_room_id != '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).filter(Room.type_room_id == type_room_id).order_by(asc(Room.price))
        if quantity_bed != '' and type_room_id == '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).filter(Room.quantity_bed == quantity_bed).order_by(asc(Room.price))
        if type_room_id != '' and quantity_bed != '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).filter(Room.type_room_id == type_room_id).filter(
                Room.quantity_bed == quantity_bed).order_by(asc(Room.price))
    if price_order_by == 'desc':
        if quantity_bed == '' and type_room_id == '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).order_by(desc(Room.price))
        if quantity_bed == '' and type_room_id != '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).filter(Room.type_room_id == type_room_id).order_by(desc(Room.price))
        if quantity_bed != '' and type_room_id == '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).filter(Room.quantity_bed == quantity_bed).order_by(desc(Room.price))
        if type_room_id != '' and quantity_bed != '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).filter(Room.type_room_id == type_room_id).filter(
                Room.quantity_bed == quantity_bed).order_by(desc(Room.price))

    return len(query.all())


def filters_room(type_room_id, quantity_bed, price_order_by, page):
    page_size = app.config['PAGE_SIZE']
    start = (page - 1) * page_size
    end = start + page_size

    query = ""
    if (type_room_id == '' and quantity_bed == '' and price_order_by == '') or \
            (type_room_id is None and quantity_bed is None and price_order_by is None):
        query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                 Room.descriptions, TypeRoom.type_room_name).filter(
            Room.type_room_id == TypeRoom.id).order_by(asc(Room.price))
    if price_order_by == 'asc':
        if quantity_bed == '' and type_room_id == '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).order_by(asc(Room.price))
        if quantity_bed == '' and type_room_id != '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).filter(Room.type_room_id == type_room_id).order_by(asc(Room.price))
        if quantity_bed != '' and type_room_id == '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).filter(Room.quantity_bed == quantity_bed).order_by(asc(Room.price))
        if type_room_id != '' and quantity_bed != '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).filter(Room.type_room_id == type_room_id).filter(
                Room.quantity_bed == quantity_bed).order_by(asc(Room.price))
    if price_order_by == 'desc':
        if quantity_bed == '' and type_room_id == '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).order_by(desc(Room.price))
        if quantity_bed == '' and type_room_id != '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).filter(Room.type_room_id == type_room_id).order_by(desc(Room.price))
        if quantity_bed != '' and type_room_id == '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).filter(Room.quantity_bed == quantity_bed).order_by(desc(Room.price))
        if type_room_id != '' and quantity_bed != '':
            query = db.session.query(Room.id, Room.quantity_bed, Room.price, Room.status, Room.type_room_id, Room.image,
                                     Room.descriptions, TypeRoom.type_room_name).filter(
                Room.type_room_id == TypeRoom.id).filter(Room.type_room_id == type_room_id).filter(
                Room.quantity_bed == quantity_bed).order_by(desc(Room.price))

    return query.slice(start, end).all()


# Add cart
def add_rental_voucher(booking_date):
    rental_voucher = RentalVoucher(booking_date=booking_date)
    db.session.add(rental_voucher)
    db.session.commit()


# Payment
def add_rental_voucher_detail(visit_name, type_visit_id, phone_number, rental_voucher_id, email, visit_name_id, nation):
    rental_voucher_detail = RentalVoucherDetail(visit_name=visit_name,
                                                type_visit_id=type_visit_id,
                                                phone_number=phone_number,
                                                rental_voucher_id=rental_voucher_id,
                                                email=email,
                                                visit_name_id=type_visit_id,
                                                nation=nation)
    db.session.add(rental_voucher_detail)
    db.session.commit()


def get_new_record_rental_voucher_detai():
    query = db.session.query(RentalVoucherDetail.id).order_by(RentalVoucherDetail.id.desc())
    return query.first()

def get_info_payer(id):
    query = db.session.query(RentalVoucherDetail.visit_name, RentalVoucherDetail.phone_number,
                             RentalVoucherDetail.email,RentalVoucherDetail.nation).filter(RentalVoucherDetail.id == id)
    return query.first()

def delete_all_receipt_detail():
    query = db.session.query(ReceiptDetail).delete()
    db.session.commit()


def add_booking_room(room_id,
                     room_name,
                     price,
                     image,
                     receive_day,
                     pay_day,
                     person_amount,
                     rental_voucher_detail_id):
    booking_room = BookingRoom(room_id=room_id,
                               room_name=room_name,
                               price=price,
                               image=image,
                               receive_day=receive_day,
                               pay_day=pay_day,
                               person_amount=person_amount,
                               rental_voucher_detail_id=rental_voucher_detail_id)
    db.session.add(booking_room)
    db.session.commit()

def get_info_booking_room():
    return BookingRoom.query.all()

def total_money_booking_room():
    b = BookingRoom.query.all()
    total = 0
    for i in b:
        total += i.price
    return total

def get_rental_voucher_detail_id(id):
    query = db.session.query(BookingRoom.rental_voucher_detail_id).filter(BookingRoom.id == id)
    return query.first()

def get_rental_voucher_detail(id):
    query = db.session.query(RentalVoucherDetail.visit_name, RentalVoucherDetail.phone_number,
                             RentalVoucherDetail.email, RentalVoucherDetail.nation).filter(BookingRoom.id == id).filter(
        RentalVoucherDetail.id == BookingRoom.rental_voucher_detail_id
    )
    return query.first()


def get_total_money_history(id):
    rental_voucher_detail_id = get_rental_voucher_detail_id(id)
    query = db.session.query(BookingRoom.price).filter(BookingRoom.rental_voucher_detail_id == rental_voucher_detail_id.rental_voucher_detail_id)

    total_money = 0
    for i in query:
        total_money += i.price
    return total_money

def delete_booking_room_by_id(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM booking_room WHERE id = " + id
    mycursor.execute(sql)
    mydb.commit()