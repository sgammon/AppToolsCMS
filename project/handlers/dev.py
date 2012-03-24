from project.handlers import WebHandler
from project.models.content import ContentSnippet

footer_content = """
7311 Greenhaven Drive, Ste. 190, Sacramento CA 95831<br/>
Voice: (916) 444-9533<br/>
TDD: (916) 394-9155<br/>
Toll free: (877) 434-8075<br/>
Fax: (916) 394-9156
"""


support_work_top_mow_content = """
<table id="contact_table">
<tr>
  <td class="text-right">&copy;Address:</td>
  <td>
  <b>Meals on Wheels by ACC</b><br />
  7311 Greenhaven Drive, Ste. 190<br />
  Sacramento CA 95831</td>
</tr>
<tr>
  <td class="text-right">Voice:</td>
  <td>(916) 444-9533</td>
</tr>
<tr>
  <td class="text-right">TDD:</td>
  <td>(916) 394-9155</td>
</tr>
<tr>
  <td class="text-right">Toll Free: </td>
  <td>(877) 434-8075</td>
</tr>
</table>
"""


class AddSnippetsHandler(WebHandler):

    ''' Prime the datastore with a bunch of snippets. '''

    def get(self):
        global footer_content
        global support_work_top_mow_content

        content_snippets = []

        footer_address = ContentSnippet(key_name='footer_address')
        footer_address.content = footer_content

        support_work_top_mow = ContentSnippet(key_name='support_work_top_mow')
        support_work_top_mow.content = support_work_top_mow_content

        content_snippets.append(footer_address)
        content_snippets.append(support_work_top_mow)

        for snippet in content_snippets:
            key = snippet.put()
            self.logging.info('====Put content snippet at key "%s"' % str(key))
            self.response.write('<b>Put key:</b> %s<br />' % str(key))
