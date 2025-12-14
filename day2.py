from flask import Flask, request, url_for
import day1

app = Flask(__name__)

@app.route('/')
def status():
    return 0

@app.route('/beranda')
def home():
    return "Hello from day1!"

if __name__ == '__main__':
    app.run(debug=True)
