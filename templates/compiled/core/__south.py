from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\core\\__south.html'

    def root(context, environment=environment):
        l_api = context.resolve('api')
        l_asset = context.resolve('asset')
        l_page = context.resolve('page')
        if 0: yield None
        yield u'<!-- Core Scripts -->\n<script src="%s"></script>\n<script src="%s"></script>\n<script src="%s"></script>\n\n<script>window.jQuery || document.write(\'<script src="%s"><\\/script>\')</script>\n\n<!-- Base Scripts -->\n<script src="/_ah/channel/jsapi"></script>\n<script src="%s"></script>\n' % (
            context.call(environment.getattr(l_asset, 'script'), 'modernizr', 'core'), 
            context.call(environment.getattr(l_asset, 'script'), 'underscore', 'core'), 
            context.call(environment.getattr(l_asset, 'script'), 'easing', 'jquery'), 
            context.call(environment.getattr(l_asset, 'script'), 'jquery', 'core'), 
            context.call(environment.getattr(l_asset, 'script'), 'base', 'apptools'), 
        )
        if context.call(environment.getattr(environment.getattr(l_api, 'users'), 'is_current_user_admin')):
            if 0: yield None
            yield u'<script src="%s"></script>' % (
                context.call(environment.getattr(l_asset, 'script'), 'cms', 'apptools'), 
            )
        yield u'\n\n\n\n\n'
        if (environment.getattr(l_page, 'services') or environment.getattr(l_page, 'analytics')):
            if 0: yield None
            yield u'<script>\n'
            for event in context.blocks['page_services'][0](context):
                yield event
            yield u'\n\n'
            for event in context.blocks['page_analytics'][0](context):
                yield event
            yield u'\n</script>\n\n'
            if context.call(environment.getattr(environment.getattr(l_api, 'users'), 'is_current_user_admin')):
                if 0: yield None
                yield u"\n<script>\n\t$(document).ready(function () {\n\t  $('.editable').cms();\n\t});\n</script>"

    def block_page_services(context, environment=environment):
        l_build_page_object = context.resolve('build_page_object')
        l_page = context.resolve('page')
        if 0: yield None
        if environment.getattr(l_page, 'services'):
            if 0: yield None
            included_template = environment.get_template('macros/page_object.js', '/source\\core\\__south.html').module
            l_build_page_object = getattr(included_template, 'build_page_object', missing)
            if l_build_page_object is missing:
                l_build_page_object = environment.undefined("the template %r (imported on line 21 in '/source\\\\core\\\\__south.html') does not export the requested name 'build_page_object'" % included_template.__name__, name='build_page_object')
            yield u'\n\t'
            yield to_string(context.call(l_build_page_object, environment.getattr(environment.getattr(l_page, 'services'), 'services_manifest'), environment.getattr(environment.getattr(l_page, 'services'), 'config')))

    def block_page_analytics(context, environment=environment):
        l_util = context.resolve('util')
        l_google_analytics_async = context.resolve('google_analytics_async')
        l_page = context.resolve('page')
        if 0: yield None
        if (not environment.getattr(environment.getattr(l_util, 'config'), 'debug')):
            if 0: yield None
            if environment.getattr(l_page, 'analytics'):
                if 0: yield None
                included_template = environment.get_template('macros/page_analytics.js', '/source\\core\\__south.html').module
                l_google_analytics_async = getattr(included_template, 'google_analytics_async', missing)
                if l_google_analytics_async is missing:
                    l_google_analytics_async = environment.undefined("the template %r (imported on line 29 in '/source\\\\core\\\\__south.html') does not export the requested name 'google_analytics_async'" % included_template.__name__, name='google_analytics_async')
                yield u'\n\t\t'
                yield to_string(context.call(l_google_analytics_async, environment.getattr(l_page, 'analytics')))

    blocks = {'page_services': block_page_services, 'page_analytics': block_page_analytics}
    debug_info = '2=12&3=13&4=14&6=15&10=16&11=18&17=24&19=27&26=30&36=33&19=37&20=41&21=43&22=48&26=50&27=55&28=57&29=59&30=64'
    return locals()