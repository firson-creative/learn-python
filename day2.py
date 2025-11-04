from flask import Flask, request, url_for
from day1.py import a, b

app = Flask(__name__)

@app.route('/')
def status():
    return 0

@app.route('/beranda')
def home():
    return day1.py

if __name__ == '__main__':
    app.run(debug=True)