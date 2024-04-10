from flask import Flask, render_template, request, redirect
from data import db_session
from data.user import User
from data.purchase import Purchase
from send_email import send_email
from data.login_form import LoginForm
from data.register_form import RegisterForm
from flask_login import LoginManager, login_user
from datetime import datetime, timedelta
import locale

locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"  # Note: do not use "de_DE" as it doesn't work
)
from request import get_weather, weather_map
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    # db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')



@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


# главная страница
@app.route('/')
def index():  # страница 1
    is_weather = True
    weather_info = None
    try:
        weather_info = get_weather()
        # создание резервного сохранения
        with open('weather_backup.json', 'w') as file:
            json.dump(weather_info, file, ensure_ascii=False)
    except Exception as e:
        # использование резервного сохранения
        print('Произошла ошибка:', e)
        print('Загрузка последнего сохранения')
        try:
            with open('weather_backup.json') as file:
                f = file.read()
                weather_info = json.loads(f)
                if weather_info['daily']['time'][0] != str(datetime.today()).split()[0]:
                    is_weather = False
        except json.decoder.JSONDecodeError as js_error:
            print('Ошибка при загрузке сохранения json:', js_error)
            is_weather = False
    return render_template('index.html', main=True, date=datetime.now(), timedelta=timedelta,
                           weather_info=weather_info, weather_map=weather_map, round=round, is_weather=is_weather)


@app.route('/order', methods=['POST', 'GET'])
def order(image=''):
    if request.method == 'GET':
        return render_template('order.html', main=False, date=datetime.now())
    elif request.method == 'POST':
        f = request.files['file']
        print(f)
        #send_email('Алексей', 'Берим', 'alex@288', f.read(), f.content_type.split('/')[1])
        '''with open(request.form['file'], 'rb') as fp:
            img_data = fp.read()
        print(img_data)
        # send_email()
        print(request.form['surname'])
        print(request.form['surname'])'''
        return None


@app.route('/account', methods=['POST', 'GET'])
def account():
    if request.method == 'GET':
        return render_template('account.html', main=False, date=datetime.now())
    '''elif request.method == 'POST':
        send_email()'''


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form, date=datetime.now())
    return render_template('login.html', title='Авторизация', form=form, date=datetime.now())


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            print('Пароли не совпадают')
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            print('Такой пользователь уже есть')
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form, date=datetime.now())


if __name__ == '__main__':
    main()
    # app.run(port=8080, host='127.0.0.1')
