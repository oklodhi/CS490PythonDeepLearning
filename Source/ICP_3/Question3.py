# import libraries
from bs4 import BeautifulSoup
import requests

# open the website and create a beautifulSoup object from the page
html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
bsobject = BeautifulSoup(html.content, "html.parser")

# return title of the website
title = bsobject.title.string
print("Title: ", title)

# get all the href links in the 'a' tag and append to list
links = []
for i in bsobject.find_all('a'):
    links.append(i.get('href'))
print(links)

# write href links to external txt file
with open('output.txt', 'w') as f:
    for item in links:
        f.write(str(item))
        f.write("\n")