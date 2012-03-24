import hashlib

from protorpc import remote
from protorpc import message_types

from apptools import BaseService

from apptools.services import RequestError

from project.messages import content as messages
from project.models.content import ContentSnippet


class SnippetNotFoundError(RequestError):
    pass


class ContentService(BaseService):

    ''' Server-side backend for content management features. '''

    #### ++++ Snippet Methods ++++ ####
    @remote.method(messages.SaveContentRequest, messages.ContentResponse)
    def save_snippet(self, request):

        ''' Save a new version of a content snippet. '''

        if request.snippet_keyname is not None:
            self.api.memcache.delete('Snippet//' + hashlib.sha256(request.snippet_keyname).hexdigest())

        if request.snippet_key is not None:
            self.api.memcache.delete('Snippet//' + hashlib.sha256(request.snippet_key).hexdigest())

        snippet = ContentSnippet(key_name=request.snippet_keyname, content=request.inner_html)
        snippet.put()

        if snippet.key().name() is not None:
            self.api.memcache.set('Snippet//' + hashlib.sha256(snippet.key().name()).hexdigest(), snippet.content)
        self.api.memcache.set('Snippet//' + hashlib.sha256(str(snippet.key())).hexdigest(), snippet.content)

        return messages.ContentResponse(snippet_key=str(snippet.key()), snippet_keyname=str(snippet.key().name()), inner_html=request.inner_html)

    @remote.method(messages.GetContentRequest, messages.ContentResponse)
    def get_snippet(self, request):

        ''' Retrieve a named or keyed snippet. '''

        if request.snippet_keyname is not None:
            snippet = ContentSnippet.get_by_key_name(request.snippet_keyname)
        else:
            snippet = ContentSnippet.get(self.api.db.Key(request.snippet_key))

        if snippet is not None:
            return messages.ContentResponse(snippet_key=str(snippet.key()), snippet_keyname=snippet.key().name(), inner_html=snippet.content)
        else:
            raise SnippetNotFoundError('Could not resolve snippet.')

    @remote.method()
    def revert_snippet(self, request):

        ''' Revert a snippet to an earlier version. '''

        pass

    #### ++++ Asset Methods ++++ ####
    @remote.method(message_types.VoidMessage, messages.GetAssetsResponse)
    def get_assets(self, request):

        ''' '''

        pass

    @remote.method(messages.AssetRequest, messages.AssetResponse)
    def new_asset(self, request):

        ''' '''

        pass

    @remote.method(messages.AssetRequest, messages.AssetResponse)
    def edit_asset(self, request):

        ''' '''

        pass

    @remote.method(messages.AssetRequest, message_types.VoidMessage)
    def delete_asset(self, request):

        ''' '''

        pass

    @remote.method(messages.AssetRequest, messages.AssetResponse)
    def place_asset(self, request):

        ''' '''

        pass
