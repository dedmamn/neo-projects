from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from sqlalchemy import Column, Integer, String, ForeignKey, Date, SmallInteger, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

from src.database.base_models import Customers, Specialist

Base = declarative_base

engine = create_engine("postgresql://postgres:qaz@localhost:5433/anton", echo=True)
session = Session(bind=engine)


def add_customer(fio: str, company_name: str, user_tg: int, password_hash: str):
    fio = fio.split()
    customer = Customers(fio[0], fio[1], fio[2], company_name, user_tg, password_hash)
    session.add(customer)
    session.commit()


def add_specialist(fio, skills, user_tg, grade, password_hash, ):
    fio = fio.split()
    specialist = Specialist(fio[0], fio[1], fio[2], str(skills), user_tg, grade, password_hash)
    session.add(specialist)
    session.commit()

