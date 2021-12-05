from flask import Flask, render_template, request
from src import app


@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == "__main__":
    # debug to view debugging in the future
    app.run(debug=True)