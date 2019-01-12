# http://www.pythonchallenge.com/pc/return/balloons.html

import difflib
import gzip

data = gzip.open("assets/deltas.gz").readlines()
d1, d2 = [], []
for line in data:
    d1.append(line[:53].decode() + "\n")
    d2.append(line[56:].decode())

compare = difflib.Differ().compare(d1, d2)

f = open("assets/f.png", "wb")
f1 = open("assets/f1.png", "wb")
f2 = open("assets/f2.png", "wb")

for line in compare:
    bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])
    print(bs)
    if line[0] == '+':
        f1.write(bs)
    elif line[0] == '-':
        f2.write(bs)
    else:
        f.write(bs)

f.close()
f1.close()
f2.close()

# address of next page http://www.pythonchallenge.com/pc/hex/bin.html
# username : butter | password : fly
