from flask import Flask, render_template, request, redirect, session
from data import db_session
from data.user import User
from data.purchase import Purchase
from send_email import send_email

'''from data.login_form import LoginForm
from data.register_form import RegisterForm'''
from data.forms import LoginForm, RegisterForm
from data.order_form import OrderForm
from flask_socketio import SocketIO
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from datetime import datetime, timedelta
import locale

locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"  # Note: do not use "de_DE" as it doesn't work
)
from request import get_weather, weather_map
import json
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
login_manager = LoginManager()
login_manager.init_app(app)


"""@app.before_request
def make_session_permanent():
    session.permanent = False


socketio = SocketIO(app)


@socketio.on('disconnect')
def disconnect_user():
    session.pop('id', None)"""


def main():
    db_session.global_init("db/tverobrad.db")
    '''print(type(User.id))
    print(type(Purchase.id_user))
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.email == 'kolia9038072204@gmail.com').first()
    print('пассворд', user.check_password('asdds'))
    user.set_password('asdds')
    db_sess.commit()
    print('пассворд', user.check_password('asdds'))'''
    app.run(port=8080, host='127.0.0.1')
    '''db_sess = db_session.create_session()
    purchase = Purchase(
        name='хз',
        id_user=1,
        colour=True,
        ornament=True,
        surname='фыв',
        birth_day=11,
        death_day=12,
        size=10,
        cost=1002,
        format='TP'
    )
    db_sess.add(purchase)
    purchase = Purchase(
        name='фывфывя',
        id_user=1,
        colour=False,
        ornament=True,
        surname='фыв',
        birth_day=1,
        death_day=2,
        size=10,
        cost=1002,
        format='TP'
    )
    db_sess.add(purchase)
    purchase = Purchase(
        name='ыыя',
        id_user=2,
        colour=True,
        ornament=False,
        surname='фыв',
        birth_day=1,
        death_day=2,
        size=10,
        cost=1002,
        format='TP'
    )
    db_sess.add(purchase)
    db_sess.commit()'''
    '''db_sess = db_session.create_session()
    user = User(
        name='ник',
        email='kolia',
        surname='кфр',
    )
    user.set_password('asd123')
    db_sess.add(user)
    db_sess.commit()'''
    '''db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.email == 'kolia9038072204@gmail.com').first()
    print(user.check_password(user.hashed_password))'''
    # if user and user.check_password('123'):
    # login_user(user, remember=form.remember_me.data)
    # return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    #return db_sess.query(User, int(user_id))
    return db_sess.query(User).get(user_id)
    # return User.query.get(user_id)


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
    form = OrderForm()
    if request.method == 'GET':
        return render_template('order.html', main=False, date=datetime.now(), form=form)
    elif request.method == 'POST':
        print(request.form['colour'])
        print(request.form['shape'])
        '''if current_user.is_authenticated:
            db_sess = db_session.create_session()
            if request.files['text']:
                surname = request.files['dead_surname']
                name = request.files['dead_surname']
                patronymic = request.files['dead_surname']
                birth_day = request.files['dead_birth_day']
                death_day = request.files['dead_death_day']
                if request.files['image']:
                    order_format = 'Текст и картинка'
                else:
                    order_format = 'Текст'
            else:  # request.files['image']
                surname = '-'
                name = '-'
                patronymic = '-'
                birth_day = datetime('00.00.0000')
                death_day = datetime('00.00.0000')
                order_format = 'Картинка'
            if 
  
            purchase = Purchase(
                user_id=current_user.id,
                surname=surname,
                name=name,
                patronymic=patronymic,
                birth_day=birth_day,
                death_day=death_day,
                ornament=request.files['ornament'],
                colour=request.files['colour'],
            )
            user.set_password(form.password.data)
            db_sess.add(user)
            db_sess.commit()'''
        '''f = request.files['file']
        print(f)'''
        # send_email('Алексей', 'Берим', 'alex@288', f.read(), f.content_type.split('/')[1])
        '''with open(request.form['file'], 'rb') as fp:
            img_data = fp.read()
        print(img_data)
        # send_email()
        print(request.form['surname'])
        print(request.form['surname'])'''
        return 'Крут'


@app.route('/account', methods=['POST', 'GET'])
@login_required
def account():
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        purchase = db_sess.query(Purchase).filter(
            (Purchase.id_user == current_user.id)).all()
        print(type(purchase))
    if request.method == 'GET':
        return render_template('account.html', main=False, date=datetime.now(), purchases=purchase)
    '''elif request.method == 'POST':
        send_email()'''


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('v')
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/account")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form, date=datetime.now())
    return render_template('login.html', title='Авторизация', form=form, date=datetime.now())


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('asd')
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают", date=datetime.now())
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть", date=datetime.now())
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form, date=datetime.now())


@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'GET':
        return render_template('render.html', main=False, date=datetime.now())
    elif request.method == 'POST':
        pass


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    main()
    # app.run(port=8080, host='127.0.0.1')
