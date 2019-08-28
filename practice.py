#%%
import requests

#%%
req = requests.get("https://en.wikipedia.org/wiki/Harvard_University")

#%%
req

#%%
type(req)

#%%
dir(req)

#%%
page = req.text
page

#%%
type(page)

#%%
from bs4 import BeautifulSoup

#%%
soup = BeautifulSoup(page, 'html.parser')

#%%
soup

#%%
soup.title

#%%
soup.p

#%%
len(soup.find_all("p"))

#%%
soup.table["class"]

#%%
[t["class"] for t in soup.find_all("table") if t.get("class")]

#%%
table_html = str(soup.find("table", "wikitable"))

#%%
from IPython.core.display import HTML
HTML(table_html)

#%%
