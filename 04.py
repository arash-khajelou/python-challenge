# http://www.pythonchallenge.com/pc/def/linkedlist.php

from urllib import request
from bs4 import BeautifulSoup
import re

base_url = 'http://www.pythonchallenge.com/pc/def/'
html_content = request.urlopen(base_url + 'linkedlist.php').read().decode()
soup = BeautifulSoup(html_content, 'html.parser')
hyper_links = soup.select("a[href^='linkedlist.php']")
next_link = hyper_links[0]['href'] if len(hyper_links) > 0 else None
numbers_pattern = re.compile(r'[0-9]+')

# first step : 12345
# second step : 8022
# third step : 63579

base_number = None  # set it no None for a normal start
if base_number is not None:
    next_link = numbers_pattern.sub("%d" % base_number, next_link)

while next_link is not None:
    next_content = request.urlopen(base_url + next_link).read().decode()
    next_nothing = numbers_pattern.findall(next_content)
    next_nothing = next_nothing[0] if len(next_nothing) > 0 else None
    if next_nothing is None:
        next_link = None
    else:
        next_link = numbers_pattern.sub(next_nothing, next_link)

    print(next_content)
