from PIL import Image
import face_recognition
file_name="peterhouse_formal"
image = face_recognition.load_image_file(f'{file_name}.png')
background = Image.open(f'{file_name}.png')
foreground = Image.open("hat2.png")
face_locations = face_recognition.face_locations(image)
print (face_locations)

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    dx=(right-left)
    dy=abs(top-bottom)
    #pil_image = Image.fromarray(image)
    foreground=foreground.resize((int(dx*1.2),dy))
    background.paste(foreground, (int(left-0.2*dx), bottom-2*dy), foreground)
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()


background.show()
background.save(f'{file_name}_Christmas_Hat.png', format="png")

