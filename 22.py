# http://www.pythonchallenge.com/pc/hex/copper.html

from PIL import Image, ImageSequence, ImageDraw

file_address = 'assets/white.gif'
img = Image.open(file_address)
img_new = Image.new('RGB', (500, 200), 'black')
img_new_draw = ImageDraw.Draw(img_new)

base_x, base_y = 0, 100
for frame in ImageSequence.Iterator(img):
    (x, y, x2, y2) = frame.getbbox()
    (dx, dy, dx2, dy2) = (x - 100, y - 100, x2 - 100, y2 - 100)
    if dx == dy == 0:
        base_y = 100
        base_x += 50
    base_x += dx
    base_y += dy
    img_new_draw.point((base_x, base_y), 'white')

img_new.show()

# the result is bonus
