from flask import Flask, render_template, request
from src import app


@app.route('/')
def home_page():
    return render_template('index.html')


def admin_stats_page():
    pass


if __name__ == "__main__":
    from src.admin import *
    # debug to view debugging in the future
    app.run(debug=True)