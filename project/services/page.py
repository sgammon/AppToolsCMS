from apptools import BaseService

from apptools.services import remote
from apptools.services import message_types

from project.messages import page as messages


class PageService(BaseService):

    ''' Server-side backend for page management features. '''

    @remote.method(messages.SetMetaTags, messages.Page)
    def set_meta_tags(self, request):

        ''' Set key=>value pairs as page meta tags. '''

        pass

    @remote.method(messages.SetTitle, messages.Page)
    def set_title(self, request):

        ''' Change the <title> of a page. '''

        pass

    @remote.method(messages.SetParent, messages.Page)
    def change_parent(self, request):

        ''' Change the "parent" of a page (for URL and navigation). '''

        pass

    @remote.method(messages.SetAssets, messages.Page)
    def set_stylesheets(self, request):

        ''' Set which stylsheets should be included on a page. '''

        pass

    @remote.method(messages.SetAssets, messages.Page)
    def set_javascripts(self, request):

        ''' Set which javascripts should be included on a page. '''

        pass

    @remote.method(messages.SetOpenGraph, messages.Page)
    def set_opengraph(self, request):

        ''' Set opengraph details for a page. '''

        pass

    @remote.method(messages.SetSecurity, messages.Page)
    def set_security(self, request):

        ''' Set security options for a page. '''

        pass

    @remote.method(messages.GetPage, messages.Page)
    def get(self, request):

        ''' Get a page. '''

        pass

    @remote.method(message_types.VoidMessage, message_types.VoidMessage)
    def publish(self, request):

        ''' Unpublish a page from the site. '''

        pass

    @remote.method(message_types.VoidMessage, message_types.VoidMessage)
    def unpublish(self, request):

        ''' Publish a page to the site. '''

        pass

    @remote.method(messages.ChangeWrapper, messages.Page)
    def change_wrapper(self, request):

        ''' Change the wrapper (parent template) for a page. '''

        pass
