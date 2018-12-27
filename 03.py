# http://www.pythonchallenge.com/pc/def/equality.html

from urllib import request
import re

html_content = request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read().decode()
comment_pattern = re.compile(r'<!\-\-(.*?)\-\->', re.DOTALL)
comments = comment_pattern.findall(html_content)
data = comments[-1] if len(comments) > 0 else ''

needle_pattern = re.compile(r'[a-z]+?[A-Z]{3}([a-z])[A-Z]{3}[a-z]+?')
needles = needle_pattern.findall(data)
print("".join(needles))
