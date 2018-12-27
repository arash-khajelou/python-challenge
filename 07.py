# http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image

file_address = 'assets/oxygen.png'
img = Image.open(file_address)

results = []
for xPos in range(img.width):
    for yPos in range(img.height):
        (r, g, b, a) = img.getpixel((xPos, yPos))
        if r == g == b and (len(results) == 0 or results[-1] != r):
            results.append(r)

print("".join(map(chr, results)))

nums = ['105', '110', '116', '101', '103', '114', '105', '116', '121']
print("".join(map(chr, map(int, nums))))
