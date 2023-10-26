import click
from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///dofas.db')


Base = declarative_base()

all_user = Table(
    'all_users',
    Base.metadata,
    user_id = Column(Integer(), ForeignKey('users.id')),
    menus_id = Column(Integer(), ForeignKey('menus.id')),
    extend_existing=True,
)

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    email = Column(String())
    phone_number = Column(Integer())
    
    menu = relationship('Menus', secondary= all_user, back_populates='users')
    restuarant = relationship('Restuarant', backref=backref('user'))
     
def __repr__(self):
        return f'Users(id={self.id}, ' + \
            f'fisrt_name={self.first_name}, ' + \
            f'last_name={self.last_name}, ' + \
            f'email={self.email}, ' + \
            f'phone_number={self.phone_number},)' 
            
            
class Menus(Base):
    __tablename__ = 'menus'

    id = Column(Integer(), primary_key=True)
    breakfast = Column(String())
    lunch = Column(String())
    dinner=Column(String())
    ethnic = Column(String())
    
    users = relationship('Users', secondary=all_user, back_populates='menus')
    restuarant = relationship('Restuarant', backref=backref('menu'))

def __repr__(self):
        return f'Menus(id={self.id}, ' + \
            f'breakfast={self.breakfast}, ' + \
            f'lunch={self.lunch}, ' + \
            f'dinner={self.dinner}, ' + \
            f'ethnic={self.ethnic},)' 


class Restuarant(Base):
    __tablename__ = 'restuarant'

    id = Column(Integer(), primary_key=True)
    soft_drink = Column(String())
    alcholic_drink = Column(String())
    wine =Column(String())

    user_id = Column(Integer(), ForeignKey('users.id'))
    menus_id = Column(Integer(), ForeignKey('menus.id'))

def __repr__(self):
        return f'Restuarant(id={self.id}, ' + \
            f'soft_drink={self.soft_drink}, ' + \
            f'alcholic_drink={self.alcholic_drink}, ' + \
            f'wine={self.wine},)' 

Base.metadata.create_all(engine)