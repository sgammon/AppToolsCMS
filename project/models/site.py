from google.appengine.ext import ndb


class Site(ndb.Model):

    ''' Represents a content fragment that can be edited. '''

    # Basic Stuff
    name = ndb.StringProperty(default='AppTools CMS', indexed=False)
    basepath = ndb.StringProperty(default='/', indexed=True)

    # Security Stuff
    adminonly = ndb.BooleanProperty(default=False, indexed=False)
    httpsonly = ndb.BooleanProperty(default=False, indexed=False)
    published = ndb.BooleanProperty(default=False, indexed=False)

    # Routing Stuff
    homepage = ndb.KeyProperty()
    subpages = ndb.KeyProperty(repeated=True)


class SiteMetaTag(ndb.Model):

    ''' Represents a meta tag that is injected site-wide. '''

    site = ndb.KeyProperty()
    name = ndb.StringProperty(indexed=False)
    value = ndb.StringProperty(indexed=False)


class SiteStylesheet(ndb.Model):

    ''' Attaches a stylesheet to be injected site-wide. '''

    name = ndb.StringProperty(indexed=False)
    site = ndb.KeyProperty()
    media = ndb.StringProperty(choices=['all', 'screen', 'print', 'handheld', 'embossed', 'braille', 'speech', 'tty', 'tv'], indexed=False)
    adminonly = ndb.BooleanProperty(indexed=False)

    # If it's a registered asset...
    package = ndb.StringProperty(indexed=False)
    entry = ndb.StringProperty(indexed=False)

    # If it's a giant string...
    content = ndb.TextProperty()


class SiteJavaScript(ndb.Model):

    ''' Attaches a JavaScript file to be injected site-wide. '''

    name = ndb.StringProperty(indexed=False)
    site = ndb.KeyProperty()

    # If it's a registered asset...
    package = ndb.StringProperty(indexed=True)
    entry = ndb.StringProperty(indexed=True)

    # If it's a giant string...
    content = ndb.TextProperty()
