import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Purchase(SqlAlchemyBase):
    __tablename__ = 'purchases'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    format = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # данные о покойнике
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    patronymic = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    birth_day = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    death_day = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    # данные о заказе
    ornament = sqlalchemy.Column(sqlalchemy.String, default=False)  # наличие орнамента
    colour = sqlalchemy.Column(sqlalchemy.String, default=False)
    shape = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # форма керамики
    size = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    deadline = sqlalchemy.Column(sqlalchemy.Date)  # дата сдачи заказа
    comment = sqlalchemy.Column(sqlalchemy.String)
    made_date = sqlalchemy.Column(sqlalchemy.Date, default=datetime.datetime.now)  # дата заказа
    user = orm.relationship('User')

    def __repr__(self):
        return f'<Order> {self.id} {self.id_user} {self.format}'
