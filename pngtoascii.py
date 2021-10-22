from PIL import Image
from os import system

colors = " .:-=+*#%@"

def image_to_ascii(im: Image, size):
    width, height = im.size
    size = (2 * width * size // height, size)
    im = im.resize(size)
    pixels = im.load()

    # system('clear')
    for y in range(size[1]):
        for x in range(size[0]):
            avg = (pixels[x, y][0] + pixels[x, y][1] + pixels[x, y][2]) / 3
            avg = int(len(colors) * avg/256)
        
            print(colors[avg], end='')
        print()

img = input("Image: ")
size = int(input("Size: "))

image_to_ascii(Image.open(img), size)

