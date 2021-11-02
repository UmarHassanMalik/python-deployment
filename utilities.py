from PIL import Image, ImageDraw
import face_recognition
import numpy as np
from io import BytesIO

# Create arrays of known face encodings and their names
known_face_encodings = [  # array saving data of relatives.
]
known_face_names = [ # array saving names of relatives
]

# process the image uploaded by user
def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file)).convert('RGB')
    return image

# will get an image as argument
# generate its encoding and add in database
# which will be matched in /recognize
def registerRelative(name: str, image: Image.Image):

    # img = face_recognition.load_image_file(image)
    image_array = np.array(image)
    encoding = face_recognition.face_encodings(image_array)[0]

    known_face_encodings.append(encoding)
    known_face_names.append(name)

    return {"status" : "Relative Added!",
            "name" : name}


# will get unknown face image as argument
# search through avaiable encodings
# return matched entry if availbale
def searchRelative(image):
    unknown_image = np.array(image)
    # Find all the faces and face encodings in the unknown image
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    # Loop through each face found in the unknown image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        if matches.__len__() == 0:
            return {"relative_name": "no record found"}

        name = "Unknown"

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            return {"relative_name": name}






