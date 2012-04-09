# -*- coding: utf-8 -*-
from protorpc import messages


class Visibility(messages.Enum):

    ''' Sets the visbility status of an object. '''

    PRIVATE = 0
    ADMIN = 100
    REGISTERED = 300
    AUTHENTICATED = 500
    PUBLIC = 999


class PostStatus(messages.Enum):

    ''' Describes the status of a blog post. '''

    ARCHIVED = 0
    DRAFT = 1
    PUBLISHED = 2


class PrivacyOptions(messages.Message):

    ''' Sets privacy options for an object. '''

    acl = messages.StringField(1, repeated=True)
    visbility = messages.EnumField(Visibility, 2)
    admin_acl = messages.StringField(3, repeated=True)
    editor_acl = messages.StringField(4, repeated=True)
    commenting = messages.BooleanField(5)


class Blog(messages.Message):

    ''' Represents a Blog model. '''

    key = messages.StringField(1)
    slug = messages.StringField(2)
    name = messages.StringField(3)
    byline = messages.StringField(4)
    authors = messages.StringField(5, repeated=True)
    urlbase = messages.StringField(6)
    privacy = messages.MessageField(PrivacyOptions, 7)
    touched = messages.StringField(8)
    created = messages.StringField(9)
    creator = messages.StringField(10)


class BlogPost(messages.Message):

    ''' Represents a BlogPost, which belongs to a Blog. '''

    key = messages.StringField(1)
    slug = messages.StringField(2)
    blog = messages.StringField(3)
    title = messages.StringField(4)
    author = messages.StringField(5)
    status = messages.EnumField(PostStatus, 6, default='DRAFT')
    byline = messages.StringField(7)
    body = messages.StringField(8)
    excerpt = messages.StringField(9)
    published = messages.BooleanField(10)
    privacy = messages.MessageField(PrivacyOptions, 11)
    tags = messages.StringField(12)


class Blogs(messages.Message):

    ''' Represents multiple Blogs. '''

    keys = messages.StringField(1, repeated=True)
    count = messages.IntegerField(2)
    blogs = messages.MessageField(Blog, 3, repeated=True)


class BlogPosts(messages.Message):

    ''' Represents multiple BlogPosts. '''

    keys = messages.StringField(1, repeated=True)
    blogs = messages.MessageField(Blog, 2, repeated=True)
    posts = messages.MessageField(BlogPost, 3, repeated=True)
    count = messages.IntegerField(4)
