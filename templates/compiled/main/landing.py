from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\main\\landing.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/base_web.html', '/source\\main\\landing.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_top_image(context, environment=environment):
        if 0: yield None
        yield u'\n  <img src="/assets/img/static/mow/main_image_home.jpg" alt="main_image_home.jpg" title="main_image_home.jpg" width="1000" height="173" />\n'

    def block_body_content(context, environment=environment):
        l_render_snippet = context.resolve('render_snippet')
        if 0: yield None
        yield u'\n<aside id="content-left-mow">\n\n  <div id="primary" class="editable widget-area" role="complementary" data-snippet-keyname=\'home-leftcontent\'>\n    '
        def macro():
            t_1 = []
            pass
            t_1.append(
                u'\n    <ul class="xoxo">\n\n      <li id="section-6" class="widget-container section-widget">\n        <a title= "Congregate Meal Sites" href="http://www.mowtest.com/congregate-meal-sites/">\n          <img src="/assets/img/static/mow/dining_out_sidebar.gif" width="203" height="74" class=\'image asset\' data-asset-key=\'dining_out_sidebar\' data-asset-package=\'mow\' />\n        </a>\n        <br/><br/>\n        <a title="Home Delivered Meals" href="http://www.mowtest.com/home-delivered-meals/">\n          <img src="/assets/img/static/mow/dining_home_sidebar.gif" width="203" height="74" class=\'image asset\' data-asset-key=\'dining_out_sidebar\' data-asset-package=\'mow\' />\n        </a>\n        <br/><br/>\n        <a title="What\'s for Lunch?" href="http://www.mowtest.com/documents/menu.pdf">\n          <img src="/assets/img/static/mow/what_for_lunch_sidebar.gif" width="203" height="74" class=\'image asset\' data-asset-key=\'whats_for_lunch\' data-asset-package=\'mow\' />\n        </a>\n        <br/><br/>\n        <a title="Make a Donation" href="http://www.mowtest.com/making-a-donation/">\n          <img src="/assets/img/static/mow/donate_sidebar.gif" width="203" height="74" class=\'image asset\' data-asset-key=\'make_a_donation\' data-asset-package=\'mow\' />\n        </a>\n      </li>\n\n    </ul>\n  ', 
            )
            return concat(t_1)
        caller = Macro(environment, macro, None, (), (), False, False, False)
        yield context.call(l_render_snippet, 'home-leftcontent', caller=caller)
        yield u'\n  </div>\n\n</aside>\n\n<section id="content-right-mow">\n\n  <article id="post-66" class="post-66 page type-page status-publish hentry">\n\n    <h2 class="entry-title">Home</h2>\n\n    <div class="entry-content editable" data-snippet-keyname=\'home-entrycontent\'>\n      '
        def macro():
            t_2 = []
            pass
            t_2.append(
                u'\n        <table id="content_table">\n          <tr>\n            <td width="150">\n              <img src="/assets/img/static/mow/hm_whatsnew_header.png" width="132" height="86" />\n            </td>\n            <td class="new-items">\n              <p>Watch our latest 30-second TV commercial for Meals On Wheels of Sacramento County.</p>\n              <p>\n                <iframe src="http://player.vimeo.com/video/23270002?title=0&amp;byline=0&amp;portrait=0" width="300" height="200" frameborder="0"></iframe>\n              </p>\n              <hr/>\n              <p>Meals on Wheels by ACC was featured on Sacramento &amp; Co. <br/>View the video <a href="http://www.news10.net/news/local/story.aspx?storyid=142700"><b>&#8216;Meals on Wheels&#8217; Rolls Again</b></a>.\n              </p>\n              <hr/>\n            </td>\n          </tr>\n        </table>\n      ', 
            )
            return concat(t_2)
        caller = Macro(environment, macro, None, (), (), False, False, False)
        yield context.call(l_render_snippet, 'home-entrycontent', caller=caller)
        yield u'\n    </div>\n\n  </article>\n\n</div><!-- content-right -->\n\n<div class="clear"></div>\n'

    blocks = {'top_image': block_top_image, 'body_content': block_body_content}
    debug_info = '1=9&3=15&7=19&11=23&45=33'
    return locals()