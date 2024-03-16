from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from sqlalchemy import Column, Integer, String, ForeignKey, Date, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine("postgresql://postgres:12345@localhost:5432/postgres", echo=True)

class Skill(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    specialists = relationship('Specialist', secondary='specialists_skills')


class SpecialistSkill(Base):
    __tablename__ = 'specialists_skills'
    specialist_id = Column(Integer, ForeignKey('specialists.id'), primary_key=True)
    skill_id = Column(Integer, ForeignKey('skills.id'), primary_key=True)


class Specialist(Base):
    __tablename__ = 'specialists'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    position = Column(String)
    availability = Column(SmallInteger)
    user_id = Column(Integer, ForeignKey('users.id'))
    skills = relationship('Skill', secondary='specialists_skills')
    projects = relationship('Project', secondary='specialists_projects')


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


class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    client_id = Column(Integer, ForeignKey('clients.id'))
    specialists = relationship('Specialist', secondary='specialists_projects')


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    company_name = Column(String)
    contact_person = Column(String)
    projects = relationship('Project')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id_tt = Column(String)
    role = Column(String)
    password_hash = Column(Integer)
    specialist = relationship('Specialist')


class Feedback(Base):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True)
    score = Column(SmallInteger)
    comments = Column(String)
    specialist_project_id = Column(Integer, ForeignKey('specialists_projects.id'))
    specialist_project = relationship('SpecialistProject', back_populates='feedback')


# Set up the engine and create all tables
Base.metadata.create_all(engine)

with Session(engine) as session:
    with session.begin():
        Base.metadata.create_all(engine)
