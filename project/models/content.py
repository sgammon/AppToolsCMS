from google.appengine.ext import db


class ContentSnippet(db.Model):

    ''' Represents a content fragment that can be edited. '''

    content = db.TextProperty()
