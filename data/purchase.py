import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Purchase(SqlAlchemyBase):
    __tablename__ = 'purchases'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('users.name'))
    name_user = orm.relationship('User', foreign_keys=[name])
    surname = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('users.surname'))
    surname_user = orm.relationship('User', foreign_keys=[surname])
    years = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    comment = sqlalchemy.Column(sqlalchemy.String)
    cost = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
