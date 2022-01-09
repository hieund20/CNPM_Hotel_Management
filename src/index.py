import json
import json
import math
import re
import smtplib
from datetime import datetime

import utils
from flask import render_template, url_for, redirect, session, jsonify
from flask_login import login_user, login_required, current_user

from src import login
from src.admin import *


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


@app.route('/register', methods=['post', 'get'])
def user_register():
    err_msg = ""
    SpecialSym = ['$', '@', '#', '%']

    # Default variable
    username = "default"  # username khác rỗng, co ky tu so, phải có ít nhất 7 ký tự #
    email = "default"  # email như payment_page() #
    password = "default"  # password khác rỗng, có ký tự số, co ky tu dac biet, co chu hoa, phải có ít nhất 5 ký tự #
    confirm = "default"  # confirm khác rỗng #

    # pass: Qualoa@123

    # Validate variable
    username_validate = ""
    email_validate = ""
    password_validate = ""
    confirm_validate = ""

    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        email = request.form.get('email')

        # validate username
        if username == "":
            username_validate = "Tên đăng nhập không được để trống"
        # else:
        #     if re.match("^[a-zA-Z0-9_.-]+$", username):
        #         username_validate = "Tên đăng nhập này không hợp lệ!"

        if len(username) < 7:
            username_validate = "Tên đăng nhập quá ngắn(Tối thiểu phải có 7 ký tự)!!!"
        if not any(char.islower() for char in username):
            username_validate = "Tên đăng nhập phải có ít nhất 1 ký tự in thường"

        # validate email
        if email == "":
            email_validate = "Hãy nhập email!"
        else:
            if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email) is None and email != "default":
                email_validate = "Email không hợp lệ!"

        # validate password
        if password == "":
            password_validate = "Mật khẩu không được để trống"
        else:
            if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{5,}', password):
                pass
            else:
                password_validate = "Mật khẩu này không hợp lệ!"

        if len(password) < 5:
            password_validate = "Mật khẩu quá ngắn(Tối thiểu phải có 5 ký tự)!"
        if not any(char.isdigit() for char in password):
            password_validate = "Mật khẩu phải có ít nhất 1 ký tự số!"
        if not any(char in SpecialSym for char in password):
            password_validate = "Tên đăng nhập phải có ít nhất 1 ký tự đặc biệt trong 4 ký tự sau: '$', '@', '#', '%' "
        if not any(char.isupper() for char in username):
            username_validate = "Tên đăng nhập phải có ít nhất 1 ký tự in hoa"

        # validate confirm
        if confirm == "":
            confirm_validate = "Xác nhận mật khẩu không được để trống"

        try:
            if password.strip().__eq__(confirm.strip()):

                # Check data before add to database
                if (username != "default" and username != "" and username_validate == "" and \
                        email != "default" and email != "" and email_validate == "" and \
                        password != "default" and password != "" and password_validate == "" and \
                        confirm != "default" and confirm != "" and confirm_validate == ""):

                    utils.add_user(username=username,
                                   password=password, email=email)
                    err_msg = "Thêm đc tài khoản"
                    render_template('register.html', err_msg=err_msg)
                else:
                    err_msg = "Không thêm được tài khoản"

                redirect(url_for('user_register', err_msg=err_msg,
                                 username_validate=username_validate, email_validate=email_validate,
                                 password_validate=password_validate, confirm_validate=confirm_validate
                                 ))
            else:
                err_msg = "Xác nhận mật khẩu không trùng khớp với Mật khẩu !!! "
        except Exception as ex:
            err_msg = "Có lỗi xảy ra rồi !! " + str(ex)

    return render_template('register.html', err_msg=err_msg,
                           username_validate=username_validate, email_validate=email_validate,
                           password_validate=password_validate, confirm_validate=confirm_validate
                           )


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


@app.route('/contact-page')
def contact_page():
    return render_template("contactPage.html")


@app.route('/my-room')
def cart():
    err = ""
    cart = []
    total_money = 0
    try:
        cart = utils.get_list_receipt_detail()
        total_money = utils.total_money(user_id=0)
    except:
        err = "Trang web lỗi! Vui lòng thử lại sau"
    return render_template('cart.html', list_cart=cart, total_money=total_money, err=err)


@app.route('/delete-cart', methods=['post'])
def delete_cart():
    data = json.loads(request.data)
    id = str(data.get("id"))
    tb = True
    try:
        utils.delete_Receipt_detail_by_id(id=id)
    except:
        tb = False

    total_money = utils.total_money(user_id=0)

    return jsonify(tb, len(utils.total_room_by_receiptId(0)), total_money)


@app.route("/rooms/<int:room_id>")
def room_detail_page(room_id):
    room = utils.get_room_by_id(room_id)
    type_room = utils.get_type_room_by_room_id(room_id)
    comments = utils.get_comments(room_id=room_id, page=int(request.args.get('page', 1)))

    return render_template('room-detail.html', room=room, type_room=type_room,
                           comments=comments,
                           pages=math.ceil(utils.count_comment(room_id=room_id) / app.config['COMMENT_SIZE']))


@app.route('/api/cart', methods=['post'])
def add_to_cart():
    if 'cart' not in session:
        session['cart'] = {}

    cart = session['cart']

    data = json.loads(request.data)
    id = str(data.get("id"))
    name = data.get("name")
    price = data.get("price", 0)
    quantity = 1

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
    list_booking_room = utils.get_list_receipt_detail()
    total_price = utils.total_money(user_id=0)

    # Default variable
    fullname = "default"
    email = "default"
    nation = "default"
    identify = "default"
    phone_number = "default"
    offline_payment = ""
    online_payment = ""
    is_sendmail_success = False

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
        offline_payment = request.form.get('offline-payment')
        online_payment = request.form.get('online-payment')

    # Validate fullname
    if fullname == "":
        fullname_validate = "Hãy nhập họ và tên!"

    # Validate email
    if email == "":
        email_validate = "Hãy nhập email!"
    else:
        if re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email) is None and email != "default":
            email_validate = "Email không hợp lệ!"

    # Validate nation
    if nation == "":
        nation_validate = "Hãy nhập tên quốc gia/khu vực!"

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

    # Check data before add to database
    if fullname != "default" and fullname != "" and fullname_validate == "" and \
            email != "default" and email != "" and email_validate == "" and \
            nation != "default" and nation != "" and nation_validate == "" and \
            identify != "default" and identify != "" and identify_validate == "" and \
            phone_number != "default" and phone_number != "" and phone_number_validate == "":
        utils.add_rental_voucher_detail(visit_name=fullname,
                                        type_visit_id=1,
                                        phone_number=phone_number,
                                        rental_voucher_id=1,
                                        email=email,
                                        visit_name_id=1,
                                        nation=nation)
        utils.add_rental_voucher(booking_date=datetime.now())

        rental_voucher_detail_id = utils.get_new_record_rental_voucher_detai()[0]
        print('check rental voucher id', rental_voucher_detail_id)
        message = 'XÁC NHẬN ĐẶT PHÒNG THÀNH CÔNG\n\nChúng tôi xin trân trọng gửi đến quý khách thư xác nhận rằng quý khách đã thực hiện thao tác đặt phòng thành công.\nCảm ơn quý khách đã sử dụng dich vụ của Lotus Hotel.\nMã đặt phòng của quý khách là: ' + str(
            rental_voucher_detail_id) + ' \nĐể nhận phòng, quý khách vui lòng trình diện mã đặt phòng cho lễ tân tại sảnh chính khách sạn.\nXin trân trọng cảm ơn.\n\n\nLIÊN HỆ\nEmail: hotel.lotus371@gmail.com\nTổng đài: 1-548-854-8898\nĐịa chỉ: 371 Nguyễn Kiệm, quận Gò Vấp, TP. Hồ Chí Minh'

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("hotel.lotus371@gmail.com", "!Hotellotus371")
        server.sendmail("hotel.lotus371@gmail.com", email, message.encode('utf-8'))
        server.quit()
        try:
            print('check mail sending', server.sendmail("hotel.lotus371@gmail.com", email, message.encode('utf-8')))
        except (IOError, OSError):
            print("Handling OSError...")
        is_sendmail_success = True

        # Check modal will be open
        if fullname != "default" and fullname_validate == "" and \
                email != "default" and email_validate == "" and \
                nation != "default" and nation_validate == "" and \
                identify != "default" and identify_validate == "" and \
                phone_number != "default" and phone_number_validate == "" and \
                is_sendmail_success is True:
            is_open_modal = True

    return render_template('payment.html',
                           list_booking_room=list_booking_room,
                           total_price=total_price,
                           fullname_validate=fullname_validate,
                           email_validate=email_validate,
                           nation_validate=nation_validate,
                           identify_validate=identify_validate,
                           phone_number_validate=phone_number_validate,
                           is_open_modal=is_open_modal,
                           is_sendmail_success=is_sendmail_success)


@app.route('/payment/success')
def payment_success_page():
    booking_room_backup = utils.get_list_receipt_detail()

    for row in booking_room_backup:
        booking_room_id = row[8]
        booking_room_name = row[1]
        booking_room_image = row[0]
        booking_room_receive_day = row[6]
        booking_room_pay_day = row[3]
        booking_room_price = row[4]
        booking_room_person_amount = row[7]

        # Backup data receipt detail to booking room before delete receipt detail
        utils.add_booking_room(room_id=booking_room_id,
                               room_name=booking_room_name,
                               price=booking_room_price,
                               image=booking_room_image,
                               receive_day=booking_room_receive_day,
                               pay_day=booking_room_pay_day,
                               person_amount=booking_room_person_amount,
                               rental_voucher_detail_id=1)

    # Delete all receipt detail when payment success
    utils.delete_all_receipt_detail()
    return render_template("payment-success.html")


@app.route('/api/comments', methods=['post'])
@login_required
def add_comments():
    data = request.json
    content = data.get('content')
    room_id = data.get('room_id')

    try:
        c = utils.add_comment(content=content, room_id=room_id)
    except:
        return {'status': 404, 'err_msg': 'Lỗi'}

    return {'status': 201, 'comment': {
        'id': c.id,
        'content': c.content,
        'created_date': c.created_date,
        'user': {
            'username': current_user.username,
            'avatar': current_user.avatar
        }
    }}


@app.route('/history')
def history():
    id_new = utils.get_new_record_rental_voucher_detai()

    info_payer = utils.get_info_payer(id_new.id)

    list_booking_room = utils.get_info_booking_room()

    total_money = utils.total_money_booking_room()

    return render_template("history-payments.html", info_payer=info_payer, list_booking_room=list_booking_room,
                           total_money=total_money)


@app.route('/check-in', methods=['post'])
def check_in():
    flag = True
    try:
        utils.delete_Receipt_detail()
    except:
        flag = False
    return jsonify(flag)


@app.route('/gallery')
def gallery_image_page():
    return render_template('gallery.html')


@app.route('/utilities')
def utilities_page():
    return render_template('utilities.html')


@app.route('/user-information')
def user_information_page():
    current_user_login_id = current_user.id
    current_user_information = utils.get_user_by_id(current_user_login_id)

    return render_template('user-information.html',
                           current_user_information=current_user_information)


if __name__ == "__main__":
    from src.admin import *

    app.run(debug=True)
