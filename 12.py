# http://www.pythonchallenge.com/pc/return/evil.html

file_address = 'assets/evil2.gfx'
data = open(file_address, 'rb').read()

for i in range(5):
    open('assets/%d.jpg' % i, 'wb').write(data[i::5])
