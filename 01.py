# http://www.pythonchallenge.com/pc/def/map.html

from urllib import request
from bs4 import BeautifulSoup

result = request.urlopen('http://www.pythonchallenge.com/pc/def/map.html').read()
soup = BeautifulSoup(result, 'html.parser')

sentence_tag = soup.find('font', {'color': '#f000f0'})
sentence = sentence_tag.contents[0] if len(sentence_tag) > 0 else None

base_chars = 'abcdefghijklmnopqrstuvwxyz'
res_chars = 'cdefghijklmnopqrstuvwxyzab'

translator = str.maketrans(base_chars, res_chars)

final_result = sentence.translate(translator)
print(final_result)
print('map'.translate(translator))
