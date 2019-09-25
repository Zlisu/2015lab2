#%%
from bs4 import BeautifulSoup

#%%
soup = BeautifulSoup(html_doc, 'html.parser')

#%%
file = open("html_doc", 'r')
soup = BeautifulSoup(file, 'html.parser')
file.close
#%%
soup

#%%
soup.prettify()

#%%
title_tag = soup.title
title_tag
#%%
title_tag.parent

#%%
title_tag.string.parent

#%%
html_tag = soup.html
type(html_tag.parent)

#%%
print(soup.parent)

#%%
link = soup.a
link

#%%
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

#%%
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
print(sibling_soup.prettify())

#%%
sibling_soup.b.next_sibling

#%%
sibling_soup.c.previous_sibling

#%%
sibling_soup.b.string

#%%

print(sibling_soup.b.string.next_sibling)

#%%
link = soup.a
link

#%%
link.next_sibling

#%%
link.next_sibling.next_sibling

#%%
for sibling in soup.a.next_siblings:
    print(repr(sibling))

#%%
last_a_tag = soup.find("a", id="link3")
last_a_tag

#%%
last_a_tag.next_sibling

#%%
last_a_tag.next_element

#%%
last_a_tag.next_element.next_element

#%%
last_a_tag.previous_sibling

#%%
