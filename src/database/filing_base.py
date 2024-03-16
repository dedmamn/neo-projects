
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from sqlalchemy import Column, Integer, String, ForeignKey, Date, SmallInteger, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

from src.database.base_models import Customers

Base = declarative_base

engine = create_engine("postgresql://postgres:qaz@localhost:5433/anton", echo=True)
session = Session(bind=engine)

def addcustomer(name, company_name, user_tg, password_hash):

    test = Customers(name= name, company_name=company_name, user_tg = user_tg, password_hash=password_hash)
    session.add(test)
    session.commit()
addcustomer("NAME","qwe", 'wer', 123)