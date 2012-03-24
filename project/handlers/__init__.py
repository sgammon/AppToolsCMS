# -*- coding: utf-8 -*-

## Basic Imports
import hashlib

## AppTools Imports
from apptools.core import BaseHandler

## Model Imports
from project.models.content import ContentSnippet

seen_snippets = []


class WebHandler(BaseHandler):

    ''' Handler for desktop web requests. '''

    SNIPPET_ERROR = lambda: '<b style="background: red; padding: 5px; position: absolute; margin: 10px; border-radius: 5px; color: white;">COULD NOT RESOLVE SNIPPET!! :(</b>'

    def retrieve_content_fragment(self, key_or_name, default_content=SNIPPET_ERROR):

        ''' Retrieve a fragment of content from the datastore, by key or key name. '''

        snippet = self.api.memcache.get('Snippet//' + hashlib.sha256(key_or_name).hexdigest())
        if snippet is None:
            snippet = ContentSnippet.get_by_key_name(key_or_name)
            if snippet is None:
                try:
                    snippet = self.api.db.get(self.api.db.Key(key_or_name))
                except:
                    snippet_content = default_content()
                if snippet is None:
                    snippet_content = default_content()
            else:
                snippet_content = snippet.content
            self.api.memcache.set('Snippet//' + hashlib.sha256(key_or_name).hexdigest(), snippet_content)
            return snippet_content
        else:
            return snippet

    def _bindRuntimeTemplateContext(self, context):

        ''' Add CMS stuff to the template context, when the user is logged in as an admin. '''

        context = super(WebHandler, self)._bindRuntimeTemplateContext(context)
        context['page']['cms'] = {}
        context['page']['cms']['enabled'] = True
        context['page']['cms']['snippets'] = {}
        context['page']['cms']['retrieve_content_fragment'] = self.retrieve_content_fragment

        return context

    def head(self):

        ''' Run GET, if defined, and return the headers only. '''

        if hasattr(self, 'get'):
            self.get()
        self.response.body = ''
        return


class MobileHandler(BaseHandler):

    ''' Handler for mobile web requests. '''
