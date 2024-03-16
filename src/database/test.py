import decimal
from decimal import Decimal
from datetime import datetime

from sqlalchemy import create_engine, text, Integer,DECIMAL, BigInteger, Column, String, MetaData, Table, select, ForeignKey
from sqlalchemy.orm import DeclarativeBase, as_declarative, Mapped, mapped_column, relationship
from sqlalchemy.orm import Session
from sqlalchemy.orm import registry

engine = create_engine("postgresql://postgres:qaz@localhost:5433/anton", echo=True)
#engine = create_engine("postgresql://anton:1234@localhost:5432/ProjectBD", echo=False)
#engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

@as_declarative()

class AbstractModel:
    id: Mapped[int]= mapped_column(autoincrement=True, primary_key=True)

class UserModel(AbstractModel):
    __tablename__ = 'users'
    user_id: Mapped[int]= mapped_column(BigInteger)
    role: Mapped[str]= mapped_column()
    pass_hash: Mapped[int]= mapped_column()
    full_name: Mapped[str] = mapped_column()
    client_id: Mapped[int]= mapped_column(ForeignKey('clients.id'))

class ClientModel(AbstractModel):
    __tablename__ = 'clients'
    company_name: Mapped[str] = mapped_column()
    user: Mapped[int] = relationship("UserModel")

class SpecialistModel(AbstractModel):
    __tablename__ = 'specialists'
    grade: Mapped[int]= mapped_column()


class SkilsModel(AbstractModel):
    __tablename__ = 'skils'
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()


class SpecialistSkilsModel(AbstractModel):
    __tablename__ = 'specialists_skils'



class SpecialistProjectModel(AbstractModel):
    __tablename__ = 'specialistproject'
    project_role: Mapped[str] = mapped_column()
    start_date: Mapped[datetime] = mapped_column()
    end_date: Mapped[datetime] = mapped_column()
    destination_status: Mapped[str] = mapped_column()


class FeedbackModel(AbstractModel):
    __tablename__ = 'feedback'
    rating: Mapped[int] = mapped_column()
    comment: Mapped[str] = mapped_column()

class ProjectsModel(AbstractModel):
    __tablename__ = 'projects'

    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    start_date: Mapped[datetime] = mapped_column()
    end_date: Mapped[datetime] = mapped_column()
    expected_result: Mapped[str] = mapped_column()
    requirements_for_specialists: Mapped[str] = mapped_column()
    processing_status: Mapped[int] = mapped_column()
    top_budget: Mapped[decimal] = mapped_column(DECIMAL)
    bottom_budget: Mapped[decimal] = mapped_column(DECIMAL)



with Session(engine) as session:
    with session.begin():
      AbstractModel.metadata.create_all(engine)
   #     user = UserModel(name='qaz')
    #    session.add(user)
   # with session.begin():
    #   res = session.execute(select(UserModel).where(UserModel.name=='qaz'))

#print(res.scalars())
#print(user.name)

