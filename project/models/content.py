from google.appengine.ext import ndb
from project.models import TouchedCreated


# Basic Snippet Features
class ContentSnippet(ndb.Model, TouchedCreated):

    ''' Represents a content fragment that can be edited. '''

    content = ndb.TextProperty()


class VisibilityAndPrivacy(object):

    ''' A grouping of properties that specify an object's visibility and privacy. '''

    visibility = ndb.StringProperty(choices=['PRIVATE', 'ADMIN', 'REGISTERED', 'AUTHENTICATED', 'PUBLIC'])
    visible_acl = ndb.StringProperty(repeated=True)
    admin_acl = ndb.StringProperty(repeated=True)
    editor_acl = ndb.StringProperty(repeated=True)
    commenting = ndb.BooleanProperty()


# Basic Blog Features
class Blog(ndb.Model, VisibilityAndPrivacy, TouchedCreated):

    ''' Represents a blog that can be posted to, and then outputted on the site somewhere. '''

    name = ndb.StringProperty()
    shortname = ndb.StringProperty()
    byline = ndb.StringProperty()
    authors = ndb.UserProperty(repeated=True)
    urlbase = ndb.StringProperty()
    creator = ndb.UserProperty()


class BlogPost(ndb.Model, VisibilityAndPrivacy, TouchedCreated):

    ''' Represents a post in a blog. '''

    blog = ndb.KeyProperty()
    author = ndb.UserProperty()
    shortname = ndb.StringProperty()
    title = ndb.StringProperty()
    status = ndb.StringProperty(choices=['ARCHIVED', 'DRAFT', 'PUBLISHED'])
    byline = ndb.StringProperty()
    body = ndb.TextProperty()
    excerpt = ndb.StringProperty()
    published = ndb.BooleanProperty()
    tags = ndb.StringProperty(repeated=True)
    keywords = ndb.StringProperty(repeated=True)


class BlogPostComment(ndb.Model):

    ''' Represents a comment on a blog post. Not yet implemented. '''

    pass


class BlogPostContent(ndb.Model):

    ''' Represents content for a blog post. Not yet implemented. '''

    pass


class BlogPostSnippet(ndb.Model):

    ''' Represents a gisted summary of a blog post. Not yet implemented. '''

    pass
