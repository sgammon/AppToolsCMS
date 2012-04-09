# -*- coding: utf-8 -*-
## Project Models Init

###### ====== Shortcuts ====== ######
from apptools.model import db, ndb
from apptools.model import BaseModel, NDBModel
from apptools.model import BaseExpando, NDBExpando

from google.appengine.ext import ndb as nndb


class TouchedCreated(object):

    ''' Adds timestamps for last touched / created. '''

    touched = nndb.DateTimeProperty(auto_now=True)
    created = nndb.DateTimeProperty(auto_now_add=True)
