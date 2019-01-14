# a zip file
import bz2
import zlib

data = open('assets/l21/package.pack', 'rb').read()
result = ''

while True:
    if data.startswith(b'x'):
        data = zlib.decompress(data)
        result += '@'
    elif data.startswith(b'BZh'):
        data = bz2.decompress(data)
        result += '-'
    elif data.endswith(b'x'):
        data = data[::-1]
        result += '\n'
    else:
        break
print(result)
