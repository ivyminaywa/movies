# coding: utf-8
# AUTOGENERATED BY gen_script.sh from 
# Copyright (C) Nyimbi Odero, Roobii, Onkololeessa 18,  2:45:11 WB EAT 2017
 
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
