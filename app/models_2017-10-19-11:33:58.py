# coding: utf-8
# AUTOGENERATED BY gen_script.sh from 
# Copyright (C) Nyimbi Odero, Kamiisa, Onkololeessa 19, 11:31:30 WD EAT 2017
 
from sqlalchemy import func
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn, UserExtensionMixin 
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.filemanager import ImageManager
from sqlalchemy_utils import aggregated, force_auto_coercion
from sqlalchemy.orm import relationship, query, defer, deferred

from sqlalchemy import (Column, Integer, String, ForeignKey,
    Sequence, Float, Text, BigInteger, Date,
    DateTime, Time, Boolean, CheckConstraint,
    UniqueConstraint, Numeric, LargeBinary , Table)
from datetime import timedelta, datetime, date
from sqlalchemy.dialects.postgresql import *
from .mixins import *

# Here is how to extend the User model
#class UserExtended(Model, UserExtensionMixin):
#    contact_group_id = Column(Integer, ForeignKey('contact_group.id'), nullable=True)
#    contact_group = relationship('ContactGroup')

# UTILITY CLASSES

import arrow, enum
import enum
# Initialize sqlalchemy_utils 
#force_auto_coercion()


db = SQLAlchemy()


class AgeRating(AuditMixin, Model):
    __tablename__ = 'age_rating'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    min_age = Column(Integer)


class CusDvd(AuditMixin, Model):
    __tablename__ = 'cus_dvd'

    customers = Column(ForeignKey(u'customer.id'), primary_key=True, nullable=False)
    dvds = Column(ForeignKey(u'dvd.id'), primary_key=True, nullable=False, index=True)
    date_in = Column(DateTime)
    date_out = Column(DateTime)
    lent_out = Column(Boolean)

    customer = relationship(u'Customer', primaryjoin='CusDvd.customers == Customer.id', backref=u'cus_dvds')
    dvd = relationship(u'Dvd', primaryjoin='CusDvd.dvds == Dvd.id', backref=u'cus_dvds')


class Customer(AuditMixin, Model):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(Text, nullable=False)
    lastname = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    address = Column(Text, nullable=False)
    family = Column(Text, nullable=False)
    blacklisted = Column(Boolean)


class Dvd(AuditMixin, Model):
    __tablename__ = 'dvd'

    id = Column(Integer, primary_key=True, autoincrement=True)
    movie = Column(ForeignKey(u'movie.id'), nullable=False, index=True)
    shelve = Column(ForeignKey(u'shelve.id'), nullable=False, index=True)

    movie1 = relationship(u'Movie', primaryjoin='Dvd.movie == Movie.id', backref=u'dvds')
    shelve1 = relationship(u'Shelve', primaryjoin='Dvd.shelve == Shelve.id', backref=u'dvds')


class Genre(AuditMixin, Model):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)


class Movie(AuditMixin, Model):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True, autoincrement=True)
    genre = Column(ForeignKey(u'genre.id'), nullable=False, index=True)
    age_rating = Column(ForeignKey(u'age_rating.id'), nullable=False, index=True)
    name = Column(Text, nullable=False)
    lenth = Column(Integer)
    description = Column(Text, nullable=False)
    posta = Column(Text, nullable=False)
    year_of_release = Column(Date)

    age_rating1 = relationship(u'AgeRating', primaryjoin='Movie.age_rating == AgeRating.id', backref=u'movies')
    genre1 = relationship(u'Genre', primaryjoin='Movie.genre == Genre.id', backref=u'movies')


class Shelve(AuditMixin, Model):
    __tablename__ = 'shelve'

    id = Column(Integer, primary_key=True, autoincrement=True)
    racks = Column(Integer)
    max_capacity = Column(Integer)
