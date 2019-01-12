# http://www.pythonchallenge.com/pc/return/romance.html

import bz2
import re
from urllib.parse import unquote_to_bytes
from urllib.request import Request, urlopen
from urllib.parse import quote_plus

num = '12345'
info = ''
while True:
    h = urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' + num)
    raw = h.read().decode("utf-8")
    print(raw)
    cookie = h.getheader("Set-Cookie")
    info += re.search('info=(.*?);', cookie).group(1)
    match = re.search('the next busynothing is (\d+)', raw)
    if match is None:
        break
    else:
        num = match.group(1)
res = unquote_to_bytes(info.replace("+", " "))
print(res)
print(bz2.decompress(res).decode())
# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
# 555-VIOLIN
# the result of violin.php is "it's me. what do you want?"

url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
msg = "the flowers are on their way"
req = Request(url, headers={"Cookie": "info=" + quote_plus(msg)})

print(urlopen(req).read().decode())

# oh well, don't you dare to forget the balloons.
