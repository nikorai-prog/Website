import datetime
import sqlalchemy
from sqlalchemy import orm, Boolean
from .db_session import SqlAlchemyBase


class Purchase(SqlAlchemyBase):
    __tablename__ = 'purchases'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_user = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    format = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    patronymic = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    birth_day = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    death_day = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    ornament = sqlalchemy.Column(Boolean, default=False)
    # id1_user = orm.relationship('User', foreign_keys=[id])
    colour = sqlalchemy.Column(sqlalchemy.String, default=False)
    shape = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    size = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    deadline = sqlalchemy.Column(sqlalchemy.DateTime)
    comment = sqlalchemy.Column(sqlalchemy.String)
    made_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)  # дата заказа
    # cost = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    user = orm.relationship('User')

    def __repr__(self):
        return f'<Order> {self.id} {self.id_user} {self.format}'
