from flask import Flask, render_template
from data import db_session
from data.user import User
from data.purchase import Purchase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


# def main():
#     db_session.global_init("db/blogs.db")
#     app.run()


# главная страница
@app.route('/')
def index():  # страница 1
    return render_template('base.html')


if __name__ == '__main__':
    # main()
    app.run(port=8080, host='127.0.0.1')
