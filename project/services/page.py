# -*- coding: utf-8 -*-
from apptools import BaseService

from apptools.services import remote
from apptools.services import message_types

from google.appengine.ext import ndb
from project.models import page as models
from project.messages import page as messages


class PageNotFound(remote.ApplicationError):

    ''' Thrown when a page cannot be found at a given key. '''

    pass


class PageService(BaseService):

    ''' Server-side backend for page management features. '''

    @remote.method(messages.Page, messages.Page)
    def put(self, request):

        ''' Create a page. '''

        try:
            if request.key is not None:
                page = ndb.Key(urlsafe=request.key)
                if page is None:
                    raise PageNotFound("The specified page could not be found.")
            else:
                if request.parent is not None:
                    page = models.Page(parent=ndb.Key(urlsafe=request.parent))
                    pageparent = request.parent
                else:
                    page = models.Page()
                    pageparent = None
        except PageNotFound:
            raise
        except Exception:
            raise PageNotFound("The specified page could not be found, either because the key is malformed or does not exist.")
        else:
            page.name = request.name
            page.title = request.title
            page.site = None
            page.adminonly = request.adminonly
            page.httpsonly = request.httpsonly
            page.published = request.published
            page.wrapper = request.wrapper
            page.urlpaths = request.urlpaths
            page.primary_path = request.primary_path

            pk = page.put()
            return messages.Page(

                key=pk.urlsafe(),
                name=page.name,
                title=page.title,
                site=str(page.site),
                parent=pageparent,
                adminonly=page.adminonly,
                httpsonly=page.httpsonly,
                published=page.published,
                wrapper=page.wrapper,
                urlpaths=page.urlpaths,
                primary_path=page.primary_path

            )

    @remote.method(message_types.VoidMessage, messages.Pages)
    def list(self, request):

        ''' List pages in the current site. '''

        pq = models.Page.query()
        pages = pq.fetch(pq.count())

        return messages.Pages(

            keys=[str(p.key.urlsafe()) for p in pages],
            pages=[messages.Page(

                key=page.key.urlsafe(),
                name=page.name,
                title=page.title,
                site=str(page.site),
                parent=map(lambda x: x.urlsafe() if isinstance(x, ndb.Key) else None, [page.key])[0],
                adminonly=page.adminonly,
                httpsonly=page.httpsonly,
                published=page.published,
                wrapper=page.wrapper,
                urlpaths=page.urlpaths,
                primary_path=page.primary_path

            ) for page in pages],
            count=len(pages)

        )

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
