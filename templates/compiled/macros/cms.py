from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\macros\\cms.html'

    def root(context, environment=environment):
        if 0: yield None
        def macro(l_name, l_caller):
            t_1 = []
            pass
            if l_caller:
                pass
                t_1.append(
                    u'\n\t\t', 
                )
                l_off = context.resolve('off')
                l_page = context.resolve('page')
                pass
                t_2 = context.eval_ctx.save()
                context.eval_ctx.autoescape = l_off
                t_1.extend((
                    (context.eval_ctx.autoescape and escape or to_string)((context.eval_ctx.autoescape and Markup or identity)(u'\n\t\t\t')), 
                    (context.eval_ctx.autoescape and escape or to_string)(context.call(environment.getattr(environment.getattr(l_page, 'cms'), 'retrieve_content_fragment'), l_name, l_caller)), 
                    (context.eval_ctx.autoescape and escape or to_string)((context.eval_ctx.autoescape and Markup or identity)(u'\n\t\t')), 
                ))
                context.eval_ctx.revert(t_2)
                t_1.append(
                    u'\n\t', 
                )
            else:
                pass
                t_1.append(
                    u'\n\t\t', 
                )
                l_off = context.resolve('off')
                l_page = context.resolve('page')
                pass
                t_3 = context.eval_ctx.save()
                context.eval_ctx.autoescape = l_off
                t_1.extend((
                    (context.eval_ctx.autoescape and escape or to_string)((context.eval_ctx.autoescape and Markup or identity)(u'\n\t\t\t')), 
                    (context.eval_ctx.autoescape and escape or to_string)(context.call(environment.getattr(environment.getattr(l_page, 'cms'), 'retrieve_content_fragment'), l_name)), 
                    (context.eval_ctx.autoescape and escape or to_string)((context.eval_ctx.autoescape and Markup or identity)(u'\n\t\t')), 
                ))
                context.eval_ctx.revert(t_3)
                t_1.append(
                    u'\n\t', 
                )
            return concat(t_1)
        context.exported_vars.add('render_snippet')
        context.vars['render_snippet'] = l_render_snippet = Macro(environment, macro, 'render_snippet', ('name',), (), False, False, True)

    blocks = {}
    debug_info = '1=8&2=11&3=22&4=23&7=41&8=42'
    return locals()