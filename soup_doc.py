#%%
from bs4 import BeautifulSoup

#%%
css_soup = BeautifulSoup('<p class="body"></p>')
css_soup.p['class']

#%%
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
css_soup.p['class']

#%%
id_soup = BeautifulSoup('<p id="my id"></p>')
id_soup.p['id']

#%%
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">home page</a></p>')
rel_soup.a['rel']

#%%
rel_soup.a['rel']=['index', 'contents']
print(rel_soup.p)

#%%
no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html', multi_valued_attributes=None)
no_list_soup.p['class']

#%%
no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html', multi_valued_attributes=None)

#%%
no_list_soup.p['class']

#%%
id_soup.p.get_attribute_list('id')

#%%
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')

#%%
xml_soup.p['class']

#%%
class_is_multi = {'*':'class'}
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml', multi_valued_attributes=class_is_multi)

#%%
id_soup.p.get_attribute_list('id')

#%%
soup = BeautifulSoup('<b class = "boldest">Extremely bold</b>')

#%%
tag = soup.b

#%%
tag.string

#%%
unicode_string = unicode(tag.string)
unicode_string

#%%
tag.string.replace_with("No longer bold")

#%%
tag

#%%
soup.name

#%%
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup)
comment = soup.b.string
type(comment)

#%%
comment

#%%
print(soup.b.prettify())

#%%
from bs4 import CData
cdata = CData("A CDATA block")
comment.replace_with(cdata)

#%%
print(soup.b.prettify())

#%%
soup.b

#%%
soup = BeautifulSoup(html_doc, 'html.parser')

#%%
