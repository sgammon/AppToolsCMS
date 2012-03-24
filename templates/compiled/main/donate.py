from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\main\\donate.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        included_template = environment.get_template('macros/cms.html', '/source\\main\\donate.html').module
        l_render_snippet = getattr(included_template, 'render_snippet', missing)
        if l_render_snippet is missing:
            l_render_snippet = environment.undefined("the template %r (imported on line 1 in '/source\\\\main\\\\donate.html') does not export the requested name 'render_snippet'" % included_template.__name__, name='render_snippet')
        context.vars['render_snippet'] = l_render_snippet
        context.exported_vars.discard('render_snippet')
        if parent_template is None:
            yield u'\n'
        parent_template = environment.get_template('core/base_web.html', '/source\\main\\donate.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_top_image(context, environment=environment):
        if 0: yield None
        yield u'\n  <b>top image</b>\n'

    def block_body_content(context, environment=environment):
        if 0: yield None
        yield u'\n  <b>body content</b>\n'

    blocks = {'top_image': block_top_image, 'body_content': block_body_content}
    debug_info = '1=9&2=17&4=23&8=27'
    return locals()