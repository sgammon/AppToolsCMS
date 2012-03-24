from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\core\\__north.html'

    def root(context, environment=environment):
        l_api = context.resolve('api')
        l_asset = context.resolve('asset')
        l_page = context.resolve('page')
        if 0: yield None
        template = environment.get_template('core/__meta.html', '/source\\core\\__north.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'<title>'
        for event in context.blocks['title'][0](context):
            yield event
        yield u'Meals on Wheels - Powered by AppTools</title>\n\n<!-- Stylesheets -->\n<link rel="stylesheet" href="%s">\n\n' % (
            context.call(environment.getattr(l_asset, 'style'), 'main', 'compiled'), 
        )
        if environment.getattr(l_page, 'ie'):
            if 0: yield None
            yield u'\n\t<link rel="stylesheet" href="%s">\n' % (
                context.call(environment.getattr(l_asset, 'style'), 'ie', 'compiled'), 
            )
        yield u'\n\n'
        if context.call(environment.getattr(environment.getattr(l_api, 'users'), 'is_current_user_admin')):
            if 0: yield None
            yield u'\n<link rel="stylesheet" type="text/css" media="all" href="%s" />\n' % (
                context.call(environment.getattr(l_asset, 'style'), 'main.min', 'cms'), 
            )
        yield u'\n\n<script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>\n<script type="text/javascript" src="%s"></script>' % (
            context.call(environment.getattr(l_asset, 'script'), 'extern', 'mow'), 
        )

    def block_title(context, environment=environment):
        l_page = context.resolve('page')
        l_title = context.resolve('title')
        if 0: yield None
        if environment.getattr(l_page, 'title'):
            if 0: yield None
            yield to_string(environment.getattr(l_page, 'title'))
        else:
            if 0: yield None
            if l_title:
                if 0: yield None
                yield to_string(l_title)

    blocks = {'title': block_title}
    debug_info = '1=11&3=15&6=18&8=20&9=23&12=26&13=29&17=32&3=35'
    return locals()