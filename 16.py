# http://www.pythonchallenge.com/pc/return/mozart.html

from PIL import Image

file_address = 'assets/mozart.gif'
img = Image.open(file_address)
img = img.convert('RGB')

new_img = Image.new('RGB', (img.width, img.height), 'black')
new_img_pixels = new_img.load()
# pink color is (255, 0, 255)
pink = (255, 0, 255)

for yPos in range(img.height):
    tmp = []
    pink_passed = False
    counter = 0
    for xPos in range(img.width):
        current_pixel = img.getpixel((xPos, yPos))
        if pink_passed or current_pixel == pink:
            pink_passed = True
            new_img_pixels[counter, yPos] = current_pixel
            counter += 1
        else:
            tmp.append(current_pixel)

    for pixel in tmp:
        new_img_pixels[counter, yPos] = pixel
        counter += 1

new_img.show()
# the answer is romance
