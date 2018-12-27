# http://www.pythonchallenge.com/pc/def/ocr.html

from urllib import request
import re

html_content = request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read().decode()
pattern = re.compile(r'<!\-\-(.*?)\-\->', re.DOTALL)
comments = pattern.findall(html_content)
data = comments[-1] if len(comments) > 0 else ''

counts = {}

for char in data:
    counts[char] = counts.get(char, 0) + 1

sorted_counts = [(k, counts[k]) for k in sorted(counts, key=counts.get)]
print(sorted_counts)
