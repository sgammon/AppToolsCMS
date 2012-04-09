from google.appengine.ext import ndb
from project.models.site import Site


class Page(ndb.Model):

    ''' Represents a content fragment that can be edited. '''

    # Basic Stuff
    name = ndb.StringProperty(indexed=False)
    title = ndb.StringProperty(indexed=False)
    site = ndb.KeyProperty()

    # Security Stuff
    adminonly = ndb.BooleanProperty(default=False, indexed=False)
    httpsonly = ndb.BooleanProperty(default=False, indexed=False)
    published = ndb.BooleanProperty(default=False, indexed=False)

    # Display Stuff
    wrapper = ndb.StringProperty(default='__base.html')

    # Routing Stuff
    urlpaths = ndb.StringProperty(indexed=True, repeated=True)
    primary_path = ndb.StringProperty(indexed=True)


class PageMetaTag(ndb.Model):

    ''' Represents a meta tag that is injected into a page. '''

    page = ndb.KeyProperty()
    name = ndb.StringProperty(indexed=False)
    value = ndb.StringProperty(indexed=False)


class PageStylesheet(ndb.Model):

    ''' Attaches a stylesheet to be injected into a page. '''

    page = ndb.KeyProperty()
    name = ndb.StringProperty(indexed=False)
    media = ndb.StringProperty(choices=['all', 'screen', 'print', 'handheld', 'embossed', 'braille', 'speech', 'tty', 'tv'], indexed=False)
    adminonly = ndb.BooleanProperty(indexed=False)

    # If it's a registered asset...
    package = ndb.StringProperty(indexed=False)
    entry = ndb.StringProperty(indexed=False)

    # If it's a giant string...
    content = ndb.TextProperty()


class SiteJavaScript(ndb.Model):

    ''' Attaches a JavaScript to be injected into a page. '''

    name = ndb.StringProperty(indexed=False)
    site = ndb.KeyProperty()

    # If it's a registered asset...
    package = ndb.StringProperty(indexed=True)
    entry = ndb.StringProperty(indexed=True)

    # If it's a giant string...
    content = ndb.TextProperty()
