# http://www.pythonchallenge.com/pc/def/peak.html

import pickle
from urllib import request

banner_file = request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
data = pickle.loads(banner_file)

for row in data:
    for (char, count) in row:
        for i in range(count):
            print(char, end='')
    print('\n')
