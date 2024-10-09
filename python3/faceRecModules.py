import face_recognition
import os
import cv2
import pickle


KNOWN_FACES_DIR ="/home/drone/Pictures/Faces/catologued"
UNKNOWN_FACES_DIR ="/home/drone/Pictures/Faces/uncatologued"
TOLERANCE = 0.6

MODEL = "hog"

known_faces = []
known_names = []


class faceRec():


    def createFaceModel(self):
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
                known_faces.append(encoding)
                known_names.append(name)

        pickle_out = open("knownF.pickle","wb")
        pickle.dump(known_faces, pickle_out)
        pickle_out.close()

        pickle_out = open("knownN.pickle","wb")
        pickle.dump(known_names, pickle_out)
        pickle_out.close()

#        return known_faces, known_names


    def analyzeNewFaces(self):
        #Loading Unknown Faces
        known_faces = pickle.load(open("knownF.pickle","rb"))
        known_names = pickle.load(open("knownN.pickle","rb"))
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
