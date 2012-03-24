from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\sections\\footers\\default.html'

    def root(context, environment=environment):
        if 0: yield None
        included_template = environment.get_template('macros/cms.html', '/source\\sections\\footers\\default.html').module
        l_render_snippet = getattr(included_template, 'render_snippet', missing)
        if l_render_snippet is missing:
            l_render_snippet = environment.undefined("the template %r (imported on line 1 in '/source\\\\sections\\\\footers\\\\default.html') does not export the requested name 'render_snippet'" % included_template.__name__, name='render_snippet')
        context.vars['render_snippet'] = l_render_snippet
        context.exported_vars.discard('render_snippet')
        yield u'\n\t  <footer id="footer" role="contentinfo">\n\t    <div id="colophon">\n\t      <div id="footer-widget-area" role="complementary">\n\n\t        <div id="first" class="widget-area">\n\t          <ul class="xoxo">\n\t            <li id="text-3" class="widget-container widget_text">\n\t              <div class="textwidget">\n\n\t                <div id="footer_address" class=\'editable\' data-snippet-keyname=\'footer_address\'>\n\t                '
        def macro():
            t_1 = []
            pass
            t_1.append(
                u'\n\t                      7311 Greenhaven Drive, Ste. 190, Sacramento CA 95831<br/>\n\t                      Voice: (916) 444-9533<br/>\n\t                      TDD: (916) 394-9155<br/>\n\t                      Toll free: (877) 434-8075<br/>\n\t                      Fax: (916) 394-9156\n\t                ', 
            )
            return concat(t_1)
        caller = Macro(environment, macro, None, (), (), False, False, False)
        yield context.call(l_render_snippet, 'footer_address', caller=caller)
        yield u'\n\t                </div>\n\n\t              </div>\n\t            </li>\n\t          </ul>\n\t        </div>\n\n\t        <div id="fourth" class="widget-area">\n\t          <ul class="xoxo">\n\t            <li id="text-5" class="widget-container widget_text">\n\t              <div class="textwidget">\n\t                <div class="footer_nav editable" data-snippet-keyname=\'footer_nav\'>\n\t                  '
        def macro():
            t_2 = []
            pass
            t_2.append(
                u'\n\n\t                    <a title="Home" href="http://mowtest.com/">Home</a>&nbsp;|&nbsp;\n\t                    <a title="About Us" href="http://mowtest.com/what-we-do/">About Us</a>&nbsp;|&nbsp;\n\t                    <a title="Become a Volunteer" href="http://mowtest.com/volunteer/">Become a Volunteer</a>&nbsp;|&nbsp;\n\t                    <a title="If You Need Meals" href="http://mowtest.com/if-you-need-meals/">If You Need Meals</a>&nbsp;|&nbsp;\n\t                    <a title="Support Our Work" href="http://mowtest.com/support-our-work/">Support Our Work</a>\n\t                    <br/>\n\t                    <a title="FAQ" href="http://mowtest.com/faq/">FAQ</a>&nbsp;|&nbsp;\n\t                    <a title="Media" href="http://mowtest.com/media/">Media</a>&nbsp;|&nbsp;\n\t                    <a title="Resources" href="http://mowtest.com/resources/">Resources</a>&nbsp;|&nbsp;\n\t                    <a title="Contact Us" href="http://mowtest.com/contact/">Contact Us</a>\n\t                    <br/><br/>\n\t                    Copyright \xc2\xa9 2010 Meals on Wheels by ACC Inc.\n\t                    <br/>\n\t                    All Rights Reserved.\n\t                ', 
            )
            return concat(t_2)
        caller = Macro(environment, macro, None, (), (), False, False, False)
        yield context.call(l_render_snippet, 'footer_nav', caller=caller)
        yield u'\n\t                </div>\n\t              </div>\n\t            </li>\n\t          </ul>\n\t        </div>\n\t      </div>\n\t    </div>\n\t  </footer>'

    blocks = {}
    debug_info = '1=8&12=15&31=25'
    return locals()