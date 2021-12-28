from flask import Flask, render_template, request, url_for, redirect, session, jsonify
from src import app, login
from src.admin import *
import utils
from flask_login import login_user, logout_user

@app.context_processor
def repos():
    return{
        "cart": utils.count_cart(session.get('cart'))
    }

@app.route('/')
def home_page():
    return render_template('index.html')


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

@app.route('/api/add-cart', methods=['post'])
def add_cart():
    dt = request.json
    room_id = str(dt.get('id'))
    name_room =dt.get('name')
    price = dt.get('price')
    name_user = dt.get('name_user')

    if name_user:
        receipt  = utils.is_name_in_receipt(name=name_user)
        user = utils.get_user_by_name(name=name_user)
        if receipt:
            pass
        else:
            utils.add_receipt(name=name_user, address="Quảng Nam", price=price)

        # utils.add_receipt_detail(receipt_id=33, room_id=room_id, price=price, user_id=2)


    #
    # cart =  session.get('cart')
    #
    # if not cart:
    #     cart ={}
    # if id in cart:
    #     cart[id]['quantity'] = cart[id]['quantity'] + 1
    # else:
    #     cart[id]= {
    #         'id' : id,
    #         'name' : name,
    #         'price' : price,
    #         'quantity': 1
    #
    #     }
    # session['cart'] = cart
    return name_user


@app.route('/cart')
def cart():
    return render_template('cart.html', stats = utils.count_cart(session['cart']))

@app.route('/update-cart')
def update_cart():
    data = request.json()
    id = str(data.get('id'))
    quantity = data.get('quantity')

    cart = session.get('cart')
    if cart and id in cart:
        cart[id]['quantity'] = quantity
        session['cart'] = cart

    return jsonify(utils.count_cart(cart = cart))

if __name__ == "__main__":
    from src.admin import *
    # debug to view debugging in the future
    app.run(debug=True)