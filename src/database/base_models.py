from decimal import Decimal

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from sqlalchemy import Column, Integer, String, ForeignKey, Date, SmallInteger, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()
engine = create_engine("postgresql://postgres:qaz@localhost:5433/anton", echo=True)

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    expected_result = Column(String)
    bottom_budget = Column(DECIMAL)
    top_budget = Column(DECIMAL)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    specialists = relationship('Specialist', secondary='specialists_projects')

class SpecialistProject(Base):
    __tablename__ = 'specialists_projects'
    id = Column(Integer, primary_key=True)
    specialist_id = Column(Integer, ForeignKey('specialists.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))
    role = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)
    feedback = relationship('Feedback', back_populates='specialist_project')


class Specialist(Base):
    __tablename__ = 'specialists'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    skills = Column(String)
    user_tg = Column(String)
    password_hash = Column(Integer)
    projects = relationship('Project', secondary='specialists_projects')



class Feedback(Base):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True)
    score = Column(SmallInteger)
    comments = Column(String)
    specialist_project_id = Column(Integer, ForeignKey('specialists_projects.id'))
    specialist_project = relationship('SpecialistProject', back_populates='feedback')


class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    company_name = Column(String)
    user_tg = Column(String)
    password_hash = Column(Integer)
    projects = relationship('Project')



# Set up the engine and create all tables
Base.metadata.create_all(engine)

with Session(engine) as session:
    with session.begin():
        Base.metadata.create_all(engine)