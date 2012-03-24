from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\core\\base_web.html'

    def root(context, environment=environment):
        parent_template = None
        l_page = context.resolve('page')
        if 0: yield None
        parent_template = environment.get_template('core/__base.html', '/source\\core\\base_web.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/cms.html', '/source\\core\\base_web.html').module
        l_render_snippet = getattr(included_template, 'render_snippet', missing)
        if l_render_snippet is missing:
            l_render_snippet = environment.undefined("the template %r (imported on line 2 in '/source\\\\core\\\\base_web.html') does not export the requested name 'render_snippet'" % included_template.__name__, name='render_snippet')
        context.vars['render_snippet'] = l_render_snippet
        context.exported_vars.discard('render_snippet')
        if environment.getattr(l_page, 'ie'):
            if 0: yield None
        for event in parent_template.root_render_func(context):
            yield event

    def block_body(context, environment=environment):
        if 0: yield None
        yield u'\n  <div id="wrapper_shadow_mow">\n    <div id="wrapper" class="hfeed">\n\n\t  '
        for event in context.blocks['masthead'][0](context):
            yield event
        yield u'\n\n      <div id="top_image_mow">\n\t      '
        for event in context.blocks['top_image'][0](context):
            yield event
        yield u'\n\t\t  <div class="clear"></div>\n\t  </div>\n\n\n      '
        for event in context.blocks['body_content_wrapper'][0](context):
            yield event
        yield u'\n      <div class="clear"></div>\n\t</div><!-- wrapper -->\n\n    <div class="clear"></div>\n  </div><!-- wrapper_shadow -->\n\n  '
        for event in context.blocks['footer'][0](context):
            yield event
        yield u'\n'

    def block_footer(context, environment=environment):
        if 0: yield None
        yield u'\n\t'
        template = environment.get_template('sections/footers/default.html', '/source\\core\\base_web.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n  '

    def block_body_content_wrapper(context, environment=environment):
        if 0: yield None
        yield u'\n\n\t      <div id="body_content_mow">\n\t        <div id="content-mow">\n\n\t\t      '
        for event in context.blocks['body_content'][0](context):
            yield event
        yield u'\n\n\t        </div><!-- content -->\n\n\t        <div class="clear"></div>\n\t      </div><!-- body_content -->\n\n\t  '

    def block_body_content(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t\t\t\t<b>body content</b>\n\t          '

    def block_masthead(context, environment=environment):
        if 0: yield None
        yield u'\n\t      '
        template = environment.get_template('sections/mastheads/default.html', '/source\\core\\base_web.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n      '

    def block_top_image(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t\t\t<b>top image</b>\n\t      '

    blocks = {'body': block_body, 'footer': block_footer, 'body_content_wrapper': block_body_content_wrapper, 'body_content': block_body_content, 'masthead': block_masthead, 'top_image': block_top_image}
    debug_info = '1=10&2=13&4=19&8=24&12=27&17=30&24=33&45=36&46=43&24=48&29=51&12=59&13=62&17=67'
    return locals()