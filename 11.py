# http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image

file_address = 'assets/cave.jpg'
img = Image.open(file_address)

new_img_1 = Image.new('RGB', (img.width, img.height), 'black')
new_img_1_pixels = new_img_1.load()
new_img_2 = Image.new('RGB', (img.width, img.height), 'black')
new_img_2_pixels = new_img_2.load()

for xPos in range(img.width):
    for yPos in range(img.height):
        if (yPos + xPos) % 2 != 0:
            new_img_1_pixels[xPos, yPos] = img.getpixel((xPos, yPos))
        else:
            new_img_2_pixels[xPos, yPos] = img.getpixel((xPos, yPos))

new_img_2.show()  # evil is the result
