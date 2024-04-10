import datetime
import sqlalchemy
from sqlalchemy import orm, Boolean
from .db_session import SqlAlchemyBase


class Purchase(SqlAlchemyBase):
    __tablename__ = 'purchases'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    id_user = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('users.id'))
    id1_user = orm.relationship('User', foreign_keys=[id])
    colour = sqlalchemy.Column(Boolean, unique=True, default=False)
    ornament = sqlalchemy.Column(Boolean, unique=True, default=False)
    made_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    birth_day = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    death_day = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    comment = sqlalchemy.Column(sqlalchemy.String)
    size = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    deadline = sqlalchemy.Column(sqlalchemy.DateTime)
    cost = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    format = sqlalchemy.Column(sqlalchemy.String, nullable=True)
