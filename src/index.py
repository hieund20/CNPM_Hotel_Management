from flask import Flask, render_template, request, url_for, redirect
from src import app, login
from src.admin import *
import utils
from flask_login import login_user, logout_user



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

@app.route('/contact-page')
def contact_page():
    return render_template("contactPage.html")

if __name__ == "__main__":
    from src.admin import *
    # debug to view debugging in the future
    app.run(debug=True)