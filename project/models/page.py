from google.appengine.ext import db


class SitePage(db.Model):

    ''' Represents a content fragment that can be edited. '''

    # Basic Stuff
    name = db.StringProperty(indexed=False)
    title = db.StringProperty(indexed=False)

    # Security Stuff
    adminonly = db.BooleanProperty(default=False, indexed=False)
    httpsonly = db.BooleanProperty(default=False, indexed=False)
    published = db.BooleanProperty(default=False, indexed=False)

    # Display Stuff
    wrapper = db.StringProperty(default='__base.html')

    # Routing Stuff
    urlpaths = db.StringListProperty(indexed=True)
    primary_path = db.StringProeprty(indexed=True)


class PageMetaTag(db.Model):

    ''' Represents a meta tag that is injected into a page. '''

    page = db.ReferenceProperty(SitePage, collection_name='metatags')
    name = db.StringProperty(indexed=False)
    value = db.StringProperty(indexed=False)


class PageStylesheet(db.Model):

    ''' Attaches a stylesheet to be injected into a page. '''

    page = db.ReferenceProperty(SitePage, collection_name='stylesheets')
    name = db.StringProperty(indexed=False)
    media = db.StringProperty(choices=['all', 'screen', 'print', 'handheld', 'embossed', 'braille', 'speech', 'tty', 'tv'], indexed=False)
    adminonly = db.BooleanProperty(indexed=False)

    # If it's a registered asset...
    package = db.StringProperty(indexed=False)
    entry = db.StringProperty(indexed=False)

    # If it's a giant string...
    content = db.TextProperty()


class SiteJavaScript(db.Model):

    ''' Attaches a JavaScript to be injected into a page. '''

    name = db.StringProperty(indexed=False)
    site = db.ReferenceProperty(SitePage, collection_name='javascripts')

    # If it's a registered asset...
    package = db.StringProperty(indexed=True)
    entry = db.StringProperty(indexed=True)

    # If it's a giant string...
    content = db.TextProperty()
