from flask import Flask, render_template, request
from src import app
from src.admin import *



@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/about')
def about_us_page():
    return render_template('about-us.html')


def admin_stats_page():
    pass


if __name__ == "__main__":
    from src.admin import *
    # debug to view debugging in the future
    app.run(debug=True)