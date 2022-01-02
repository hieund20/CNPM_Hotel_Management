import hashlib
import hmac
import json
import urllib
import uuid

import utils
from urllib.request import urlopen, Request
from flask import Flask, render_template, request, url_for, redirect, session, jsonify, make_response
from flask_login import login_user, logout_user
from src import app, login
from src.admin import *
import requests

@app.context_processor
def repos():
    return{
        "cart": len(utils. total_room_by_receiptId(0))
    }



@app.route('/', methods=['post', 'get'])
def home_page():
    filter_room_list = None
    if request.method.__eq__('POST'):
        type_room_id = request.form.get('type-room-id')
        quantity_bed = request.form.get('quantity-bed')
        price_sort = request.form.get('price-sort')
        filter_room_list = utils.filters_room(type_room_id=type_room_id,
                                              quantity_bed=quantity_bed,
                                              price_order_by=price_sort)

    room_list = utils.get_all_rooms()
    print('room list', room_list)

    return render_template('index.html', room_list=room_list,
                           filter_room_list=filter_room_list)


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
    err =""
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
    tb ="Đã xóa thành công"
    try:
       utils.delete_Receipt_detail(id = id)
    except:
        tb="Lỗi databasse! Vui lòng thử lại sau!"

    # update cart

    return jsonify(tb, len(utils. total_room_by_receiptId(0)))



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



    return jsonify(utils.cart_stats(cart), cart, booking_infor, len(utils. total_room_by_receiptId(0)))

@app.route('/payment')
def payment_page():
    # parameters send to MoMo get get payUrl
    endpoint = "https://test-payment.momo.vn/gw_payment/transactionProcessor"
    partnerCode = "MOMOO49X20220102"
    accessKey = "6nibheuSbyrskJHk"
    secretKey = "opITjJHgVfL3Ylf7bQMVPJLMcfOFd7mY"
    orderInfo = "pay with MoMo"
    redirectUrl = "https://webhook.site/b3088a6a-2d17-4f8d-a383-71389a6c600b"
    ipnUrl = "https://webhook.site/b3088a6a-2d17-4f8d-a383-71389a6c600b"
    amount = "50000"
    orderId = str(uuid.uuid4())
    requestId = str(uuid.uuid4())
    requestType = "captureWallet"
    extraData = ""  # pass empty value or Encode base64 JsonString

    # before sign HMAC SHA256 with format: accessKey=$accessKey&amount=$amount&extraData=$extraData&ipnUrl=$ipnUrl&orderId=$orderId&orderInfo=$orderInfo&partnerCode=$partnerCode&redirectUrl=$redirectUrl&requestId=$requestId&requestType=$requestType
    rawSignature = "accessKey=" + accessKey + "&amount=" + amount + "&extraData=" + extraData + "&ipnUrl=" + ipnUrl + "&orderId=" + orderId + "&orderInfo=" + orderInfo + "&partnerCode=" + partnerCode + "&redirectUrl=" + redirectUrl + "&requestId=" + requestId + "&requestType=" + requestType

    # puts raw signature
    print("--------------------RAW SIGNATURE----------------")
    print(rawSignature)
    # signature
    h = hmac.new(bytes(secretKey, encoding='utf8'), bytes(rawSignature, encoding='utf8'), hashlib.sha256)
    signature = h.hexdigest()
    print("--------------------SIGNATURE----------------")
    print(signature)

    # json object send to MoMo endpoint

    data = {
        'partnerCode': partnerCode,
        'partnerName': "Test",
        'storeId': "MomoTestStore",
        'requestId': requestId,
        'amount': amount,
        'orderId': orderId,
        'orderInfo': orderInfo,
        'redirectUrl': redirectUrl,
        'ipnUrl': ipnUrl,
        'lang': "vi",
        'extraData': extraData,
        'requestType': requestType,
        'signature': signature
    }
    print("--------------------JSON REQUEST----------------\n")
    data = json.dumps(data)
    print(data)

    clen = len(data)
    req = urllib.request.Request(endpoint, data, {'Content-Type': 'application/json', 'Content-Length': clen})
    f = urllib.request.urlopen(req)

    response = f.read()
    f.close()
    print("--------------------JSON response----------------\n")
    print(response + "\n")

    print("payUrl\n")
    print(json.loads(response)['payUrl'] + "\n")

    return render_template('payment.html')


if __name__ == "__main__":
    from src.admin import *

    app.run(debug=True)
