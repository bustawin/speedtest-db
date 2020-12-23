import sqlalchemy as s
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base

import config

Base = declarative_base()


def engine(uri=config.DB_URI):
    return s.create_engine(uri)


def Session(uri=config.DB_URI) -> orm.Session:
    return orm.sessionmaker(bind=engine(uri))()


class Server(Base):
    __tablename__ = "servers"

    id = s.Column(s.Unicode, primary_key=True)
    url = s.Column(s.Unicode, nullable=False)
    lat = s.Column(s.Float, nullable=False)
    lon = s.Column(s.Float, nullable=False)
    name = s.Column(s.Unicode, nullable=False)
    cc = s.Column(s.Unicode, nullable=False)
    sponsor = s.Column(s.Unicode, nullable=False)

    def __repr__(self):
        return "<Server {id} {name}>"


class Update(Base):
    __tablename__ = "updates"
    updated = s.Column(s.DateTime, nullable=False, primary_key=True)
    download = s.Column(s.BigInteger)
    upload = s.Column(s.BigInteger)
    ping = s.Column(s.Float)
    server_id = s.Column(s.Unicode, s.ForeignKey(Server.id))
    ip = s.Column(s.Unicode)
    message = s.Column(s.Unicode)
    error = s.Column(s.Boolean, nullable=False, default=False)

    server = orm.relationship(Server)


def create(e: callable = None):
    """Creates the tables at the db"""
    e = e or engine()
    Base.metadata.create_all(bind=e)


def delete(e: callable = None):
    """Deletes the tables at the db"""
    e = e or engine()
    Base.metadata.drop_all(bind=e)
