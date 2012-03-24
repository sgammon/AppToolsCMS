from google.appengine.ext import db
from project.models.page import SitePage


class SiteInfo(db.Model):

    ''' Represents a content fragment that can be edited. '''

    # Basic Stuff
    name = db.StringProperty(default='AppTools CMS', indexed=False)
    basepath = db.StringProperty(default='/', indexed=True)

    # Security Stuff
    adminonly = db.BooleanProperty(default=False, indexed=False)
    httpsonly = db.BooleanProperty(default=False, indexed=False)
    published = db.BooleanProperty(default=False, indexed=False)

    # Routing Stuff
    homepage = db.ReferenceProperty(SitePage, collection_name='site')
    subpages = db.ListProperty(db.Key)


class SiteMetaTag(db.Model):

    ''' Represents a meta tag that is injected site-wide. '''

    site = db.ReferenceProperty(SiteInfo, collection_name='metatags')
    name = db.StringProperty(indexed=False)
    value = db.StringProperty(indexed=False)


class SiteStylesheet(db.Model):

    ''' Attaches a stylesheet to be injected site-wide. '''

    name = db.StringProperty(indexed=False)
    site = db.ReferenceProperty(SiteInfo, collection_name='stylesheets')
    media = db.StringProperty(choices=['all', 'screen', 'print', 'handheld', 'embossed', 'braille', 'speech', 'tty', 'tv'], indexed=False)
    adminonly = db.BooleanProperty(indexed=False)

    # If it's a registered asset...
    package = db.StringProperty(indexed=False)
    entry = db.StringProperty(indexed=False)

    # If it's a giant string...
    content = db.TextProperty()


class SiteJavaScript(db.Model):

    ''' Attaches a JavaScript file to be injected site-wide. '''

    name = db.StringProperty(indexed=False)
    site = db.ReferenceProperty(SiteInfo, collection_name='javascripts')

    # If it's a registered asset...
    package = db.StringProperty(indexed=True)
    entry = db.StringProperty(indexed=True)

    # If it's a giant string...
    content = db.TextProperty()