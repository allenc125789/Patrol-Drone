import face_recognition
import os
import cv2

KNOWN_FACES_DIR ="/home/drone/Pictures/Faces/catologued"
UNKNOWN_FACES_DIR ="/home/drone/Pictures/Faces/uncatologued"
TOLERANCE = 0.6

FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "hog"

cap = cv2.VideoCapture(0)

known_faces = []
known_names = []

#Loading Known Faces
for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
        temp_encoding = face_recognition.face_encodings(image)

        if len(temp_encoding) > 0 :
            encoding = temp_encoding[0]
        else:
            print("no face found")
            continue
        print(encoding)
        known_faces.append(encoding)
        known_names.append(name)

#Loading Unknown Faces
for filename in os.listdir(UNKNOWN_FACES_DIR):
    try:
        print(filename)
        imageBGR = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")

        image = cv2.cvtColor(imageBGR, cv2.COLOR_BGR2RGB)
        locations = face_recognition.face_locations(image, model=MODEL)
        encodings = face_recognition.face_encodings(image, locations)

        for face_encoding, face_location in zip(encodings, locations):
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
            match = None
            if True in results:
                match = known_names[results.index(True)]
                print(f"Match found: {match}")

    except Exception as e:
        print(e)
