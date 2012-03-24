from protorpc import messages


class GetContentRequest(messages.Message):

    ''' Retrieve a content snippet. '''

    snippet_key = messages.StringField(1)
    snippet_keyname = messages.StringField(2)


class SaveContentRequest(messages.Message):

    ''' Request to save a new version of a content snippet. '''

    snippet_keyname = messages.StringField(1)
    snippet_key = messages.StringField(2)
    inner_html = messages.StringField(3)


class ContentResponse(messages.Message):

    ''' Respond to a request to save a new version of a content snippet. '''

    snippet_key = messages.StringField(1)
    snippet_keyname = messages.StringField(2)
    inner_html = messages.StringField(3)


class AssetRequest(messages.Message):
    pass


class AssetResponse(messages.Message):
    pass


class GetAssetsResponse(messages.Message):
    pass
