from flask import Flask, render_template, request
from data import db_session
from data.user import User
from data.purchase import Purchase
from send_email import send_email
from datetime import datetime, timedelta
import locale
locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"  # Note: do not use "de_DE" as it doesn't work
)
from request import get_weather, weather_map

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.run()

result = get_weather()
print(result['daily']['weather_code'])

# главная страница
@app.route('/')
def index():  # страница 1
    return render_template('index.html', main=True, date=datetime.now(), timedelta=timedelta,
                           weather_info=get_weather(), weather_map=weather_map)


@app.route('/order', methods=['POST', 'GET'])
def order():
    if request.method == 'GET':
        return render_template('order.html', main=False, date=datetime.now())
    elif request.method == 'POST':
        send_email()


@app.route('/account', methods=['POST', 'GET'])
def account():
    if request.method == 'GET':
        return render_template('account.html', main=False, date=datetime.now())
    '''elif request.method == 'POST':
        send_email()'''


if __name__ == '__main__':
    # main()
    app.run(port=8080, host='127.0.0.1')
