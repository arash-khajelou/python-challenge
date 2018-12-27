# http://www.pythonchallenge.com/pc/def/channel.html

import zipfile
import re

zipfile = zipfile.ZipFile("assets/channel.zip")
base_number = 90052
numbers_pattern = re.compile(r'[0-9]+')
comments = []

next_file_address = '{}.txt'.format(base_number)
while next_file_address is not None:
    next_contents = zipfile.read(next_file_address).decode('utf-8')
    comments.append(zipfile.getinfo(next_file_address).comment.decode('utf-8'))
    next_number = numbers_pattern.findall(next_contents)
    next_number = next_number[0] if len(next_number) > 0 else None

    if next_number is not None:
        next_file_address = numbers_pattern.sub(next_number, next_file_address)
    else:
        next_file_address = None

    print(next_contents)

for comment in comments:
    print(comment, end='')
