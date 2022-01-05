import hashlib
import hmac
import json
import math
import re
import urllib
import uuid
from datetime import datetime

import paypalrestsdk as paypalrestsdk
import utils
from urllib.request import urlopen, Request
from flask import Flask, render_template, request, url_for, redirect, session, jsonify, make_response
from flask_login import login_user, logout_user
from src import app, login
from src.admin import *
import requests


@app.context_processor
def repos():
    return {
        "cart": len(utils.total_room_by_receiptId(0))
    }


@app.route('/', methods=['post', 'get'])
def home_page():
    filter_room_list = []
    type_room_id = ""
    quantity_bed = ""
    price_sort = ""

    if request.method.__eq__('POST'):
        type_room_id = request.form.get('type-room-id')
        quantity_bed = request.form.get('quantity-bed')
        price_sort = request.form.get('price-sort')

    page = request.args.get('page', 1)
    filter_room_list = utils.filters_room(type_room_id=type_room_id,
                                          quantity_bed=quantity_bed,
                                          price_order_by=price_sort,
                                          page=int(page))

    print('len', utils.count_rooms(type_room_id=type_room_id,
                                   quantity_bed=quantity_bed,
                                   price_order_by=price_sort))

    page_counter = utils.count_rooms(type_room_id=type_room_id,
                                     quantity_bed=quantity_bed,
                                     price_order_by=price_sort)

    current_page = math.ceil(page_counter / app.config['PAGE_SIZE'])

    return render_template('index.html',
                           filter_room_list=filter_room_list,
                           pages=current_page,
                           type_room_id=type_room_id,
                           price_sort=price_sort)


@app.route('/about')
def about_us_page():
    return render_template('about-us.html')


def admin_stats_page():
    pass


@app.route('/register', methods=['post', 'get'])
def user_register():
    err_msg = ""
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        email = request.form.get('email')
        try:
            if password.strip().__eq__(confirm.strip()):

                utils.add_user(username=username,
                               password=password, email=email)
                return redirect(url_for('user_signin'))
            else:
                err_msg = "Xác nhận mật khẩu không trùng khớp với Mật khẩu !!! "
        except Exception as ex:
            err_msg = "Có lỗi xảy ra rồi !! " + str(ex)

    return render_template('register.html', err_msg=err_msg)


@app.route('/user-login', methods=['post', 'get'])
def user_signin():
    err_msg = ''

    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = utils.check_login(username=username, password=password)
        if user:
            login_user(user=user)
            return redirect(url_for('home_page'))
        else:
            err_msg = 'Username hay password không đúng, vui lòng kiểm tra lại'

    return render_template('login.html', err_msg=err_msg)


@app.route('/user-logout')
def user_signout():
    logout_user()
    return redirect(url_for('home_page'))


@login.user_loader
def user_load(user_id):
    return utils.get_user_by_id(user_id=user_id)


@app.route('/my-room')
def cart():
    err = ""
    try:
        cart = utils.get_list_receipt_detail(0)
        total_money = utils.total_money(user_id=0)
    except:
        err = "Trang web lỗi! Vui lòng thử lại sau"
    return render_template('cart.html', list_cart=cart, total_money=total_money, err=err)


@app.route('/delete-cart', methods=['post'])
def delete_cart():
    data = json.loads(request.data)
    id = str(data.get("id"))
    tb = "Đã xóa thành công"
    try:
        utils.delete_Receipt_detail(id=id)
    except:
        tb = "Lỗi databasse! Vui lòng thử lại sau!"

    # update cart

    return jsonify(tb, len(utils.total_room_by_receiptId(0)))


@app.route("/rooms/<int:room_id>")
def room_detail_page(room_id):
    room = utils.get_room_by_id(room_id)
    type_room = utils.get_type_room_by_room_id(room_id)
    return render_template('room-detail.html', room=room, type_room=type_room)


@app.route('/api/cart', methods=['post'])
def add_to_cart():
    if 'cart' not in session:
        session['cart'] = {}

    cart = session['cart']

    data = json.loads(request.data)
    id = str(data.get("id"))
    name = data.get("name")
    price = data.get("price", 0)

    receive_day = data.get("receive-day")
    pay_day = data.get("pay-day")
    person_amount = str(data.get("person-amount"))

    cart = session.get('cart')

    if id in cart:
        cart[id]['quantity'] = cart[id]['quantity'] + 1
    else:
        cart[id] = {
            "id": id,
            "name": name,
            "price": price,
            "quantity": 1,
        }

    session['cart'] = cart

    booking_infor = {
        "receive_day": receive_day,
        "pay_day": pay_day,
        "person_amount": person_amount
    }

    quantity, price = utils.cart_stats(cart)
    utils.add_receipt_detail(room_id=int(id),
                             room_name=name,
                             price=float(price),
                             quantity=float(quantity),
                             receive_day=receive_day,
                             pay_day=pay_day,
                             person_amount=int(person_amount))
    print('person_amount', person_amount)

    return jsonify(utils.cart_stats(cart), cart, booking_infor, len(utils.total_room_by_receiptId(0)))


@app.route('/payment', methods=['post', 'get'])
def payment_page():
    list_booking_room = utils.get_list_receipt_detail(0)
    total_price = utils.total_money(user_id=0)

    # Default variable
    fullname = "default"
    email = "default"
    nation = "default"
    identify = "default"
    phone_number = "default"

    # Validate variable
    fullname_validate = ""
    email_validate = ""
    nation_validate = ""
    identify_validate = ""
    phone_number_validate = ""

    # Open success modal
    is_open_modal = False

    if request.method.__eq__('POST'):
        fullname = request.form.get('payment-fullname')
        email = request.form.get('payment-email')
        nation = request.form.get('payment-nation')
        identify = request.form.get('payment-identify')
        phone_number = request.form.get('payment-phone-number')

    # Validate fullname (thêm dâu cách và Tiếng việt thì check sai)
    if fullname == "":
        fullname_validate = "Hãy nhập họ và tên!"
    else:
        if re.match(r'[a-zA-Z\s]+$', fullname) is None:
            fullname_validate = "Họ tên không hợp lệ!"

    # Validate email
    if email == "":
        email_validate = "Hãy nhập email!"
    else:
        if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email) is None and email != "default":
            email_validate = "Email không hợp lệ!"

    # Validate nation (thêm dâu cách và Tiếng việt thì check sai)
    if nation == "":
        nation_validate = "Hãy nhập tên quốc gia/khu vực!"
    else:
        if re.match(r'[a-zA-Z\s]+$', nation) is None:
            nation_validate = "Tên quốc gia/khu vực không hợp lệ!"

    # Validate identify
    if identify == "":
        identify_validate = "Hãy nhập số CMND/Passport!"
    else:
        if re.match('^[0-9]+$', identify) is None and email != "default":
            identify_validate = "Số CMND/Passport không hợp lệ!"

    # Validate phone number (not work)
    if phone_number == "":
        phone_number_validate = "Hãy nhập số điện thoại!"
    else:
        if re.match(r"[\d]{3}[\d]{3}[\d]{3}", phone_number) is None and email != "default":
            phone_number_validate = "Số điện thoại không hợp lệ!"

    print('run this after that')
    print('fullname', fullname)
    print('email', email)
    print('nation', nation)
    print('identify', identify)
    print('phone_number', phone_number)

    # Check modal will be open
    if fullname != "default" and fullname_validate == "" and \
            email != "default" and email_validate == "" and \
            nation != "default" and nation_validate == "" and \
            identify != "default" and identify_validate == "" and \
            phone_number != "default" and phone_number_validate == "":
        is_open_modal = True

    # Check data before add to database
    if fullname != "default" and fullname != "" and fullname_validate == "" and \
            email != "default" and email != "" and email_validate == "" and \
            nation != "default" and nation != "" and nation_validate == "" and \
            identify != "default" and identify != "" and identify_validate == "" and \
            phone_number != "default" and phone_number != "" and phone_number_validate == "":
        print("run this")
        utils.add_rental_voucher_detail(visit_name=fullname,
                                        type_visit_id=1,
                                        phone_number=phone_number,
                                        rental_voucher_id=1,
                                        email=email,
                                        visit_name_id=1,
                                        nation=nation)
        utils.add_rental_voucher(booking_date=datetime.now())

    return render_template('payment.html',
                           list_booking_room=list_booking_room,
                           total_price=total_price,
                           fullname_validate=fullname_validate,
                           email_validate=email_validate,
                           nation_validate=nation_validate,
                           identify_validate=identify_validate,
                           phone_number_validate=phone_number_validate,
                           is_open_modal=is_open_modal)


@app.route('/payment/success')
def payment_success_page():
    # Delete all receipt detail when payment success
    utils.delete_all_receipt_detail()
    return render_template("payment-success.html")


if __name__ == "__main__":
    from src.admin import *

    app.run(debug=True)
