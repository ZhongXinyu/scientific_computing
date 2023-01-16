from PIL import Image

image = Image.open('Picture3.png')
image = image.convert('RGBA')
print(image.mode)


# Transparency
newImage = []
for item in image.getdata():
    if item[:3] == (255, 255, 255):
        newImage.append((255, 255, 255, 0))
    else:
        newImage.append(item)

image.putdata(newImage)


image.save('output3.png')
print(image.mode, image.size)