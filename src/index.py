import json

import utils
from flask import Flask, render_template, request, url_for, redirect, session, jsonify, make_response
from flask_login import login_user, logout_user
from src import app, login
from src.admin import *


@app.route('/')
def home_page():
    room_list = utils.get_all_rooms()
    return render_template('index.html', room_list=room_list)


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

    return jsonify(utils.cart_stats(cart), cart, booking_infor)


if __name__ == "__main__":
    from src.admin import *

    app.run(debug=True)
