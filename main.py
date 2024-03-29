from flask import Flask, render_template, request
from data import db_session
from data.user import User
from data.purchase import Purchase
from send_email import send_email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.run()


# главная страница
@app.route('/')
def index():  # страница 1
    return render_template('index.html', main=True)


@app.route('/order', methods=['POST', 'GET'])
def order():
    if request.method == 'GET':
        return render_template('order.html', main=False)
    elif request.method == 'POST':
        send_email(request.form['surname'])


if __name__ == '__main__':
    # main()
    app.run(port=8080, host='127.0.0.1')
