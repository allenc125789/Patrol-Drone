import face_recognition
import os
import cv2

KNOWN_FACES_DIR ="/home/drone/Pictures/Faces/catologued"
#UNKNOWN_FACES_DIR ="/home/drone/Pictures/Faces/uncatologued"
TOLERANCE = 0.6

FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "hog"

cap = cv2.VideoCapture(0)

print("loading known faces")

known_faces = []
known_names = []

for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
        temp_encoding = face_recognition.face_encodings(image)

        if len(temp_encoding) > 0 :
            encoding = temp_encoding[0]
        else:
            print("no face found")
            continue
#        encoding = face_recognition.face_encodings(image)
        print(encoding)
        known_faces.append(encoding)
        known_names.append(name)


print("process uknown faces")
while True:
    try:
#    print(filename)
#        image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
        cap.set(cv2.CAP_PROP_FPS,15)
        ret, video = cap.read()
        image = cv2.cvtColor(video, cv2.COLOR_BGR2RGB)
        locations = face_recognition.face_locations(image, model=MODEL)
        encodings = face_recognition.face_encodings(image, locations)

        for face_encoding, face_location in zip(encodings, locations):
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
            match = None
            if True in results:
                match = known_names[results.index(True)]
                print(f"Match found: {match}")
                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])
                color = [0, 255, 0]
                cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)

                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2]+22)
                cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
                cv2.putText(image, match, (face_location[3]+10, face_location[2]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200,200,200), FONT_THICKNESS)
        cv2.imshow("cap", image)
        key = cv2.waitKey(30)
        if key == 27:
            cv2.destroyAllWindows()
            break
    except Exception as e:
        print(e)
#        break
