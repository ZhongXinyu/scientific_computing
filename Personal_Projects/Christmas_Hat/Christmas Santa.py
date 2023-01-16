from PIL import Image
import face_recognition
file_name="peterhouse_formal"
image = face_recognition.load_image_file(f'{file_name}.png')
background = Image.open(f'{file_name}.png')
foreground_hat= Image.open("hat.png")
foreground_beard= Image.open("beard.png")
face_locations = face_recognition.face_locations(image)
face_landmarks_lists = face_recognition.face_landmarks(image)

for face_landmarks_list in face_landmarks_lists:
    print (face_landmarks_list["nose_tip"])


for face_location in face_locations:
    # Print the location of each face in this image
    top, right, bottom, left = face_location
    dx=(right-left)
    dy=abs(top-bottom)
    #pil_image = Image.fromarray(image)
    foreground_hat=foreground_hat.resize((int(dx*1.2),dy))
    foreground_beard=foreground_beard.resize((int(dx*1.2),int(dy*0.8)))
    background.paste(foreground_hat, (int(left-0.2*dx), bottom-2*dy), foreground_hat)
    background.paste(foreground_beard, (int(left), int(top+0.5*dx)), foreground_beard)
    #print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    ###You can access the actual face itself like this:
    #face_image = image[top:bottom, left:right]
    #pil_image = Image.fromarray(face_image)
    #pil_image.show()


background.show()
background.save(f'{file_name}_Christmas_Santa.png', format="png")


