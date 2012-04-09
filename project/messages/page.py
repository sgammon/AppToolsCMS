from apptools.services import messages


class MetaTag(messages.Message):

    ''' One key=>value meta tag pair. '''

    key = messages.StringField(1)
    value = messages.StringField(2)


class SetMetaTags(messages.Message):

    ''' A set of key=>value MetaTag pairs. '''

    tags = messages.MessageField(MetaTag, 1, repeated=True)


class SetTitle(messages.Message):

    ''' Set a page's title. '''

    title = messages.StringField(1)


class SetParent(messages.Message):

    ''' Set a page's parent. '''

    pass


class SetAssets(messages.Message):

    ''' Set a page's assets. '''

    pass


class SetOpenGraph(messages.Message):

    ''' Set a page's Open Graph details. '''

    pass


class SetSecurity(messages.Message):

    ''' Set a page's security settings. '''

    pass


class GetPage(messages.Message):

    ''' Get a page. '''

    key = messages.StringField(1)


class ChangeWrapper(messages.Message):

    ''' Change a page's wrapper. '''

    pass


class Page(messages.Message):

    ''' A page. '''

    key = messages.StringField(1)
    name = messages.StringField(2)
    title = messages.StringField(3)
    site = messages.StringField(4)
    parent = messages.StringField(5)
    adminonly = messages.BooleanField(6)
    httpsonly = messages.BooleanField(7)
    published = messages.BooleanField(8)
    wrapper = messages.StringField(9)
    urlpaths = messages.StringField(10, repeated=True)
    primary_path = messages.StringField(11)


class Pages(messages.Message):

    ''' A list of pages. '''

    keys = messages.StringField(1, repeated=True)
    pages = messages.MessageField(Page, 2, repeated=True)
    count = messages.IntegerField(3)
