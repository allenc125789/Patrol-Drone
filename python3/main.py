import cv2
import camCaptureFaceModules as fm
import camCapturePoseModules as pm
import faceRecModules as fr
import time

cap = cv2.VideoCapture(0)
pTime = 0
detectorFM = fm.faceDetector()
detectorPM = pm.poseDetector()
detectorFR = fr.faceRec()




#Determines pixel difference between faces and the centerPOV.
def faceAutoCenter(bboxs):
    try:
        output = []
        for i in bboxs:
            faceID = i[0]
            bboxSize = i[1]
            faceDetectionVal = i[2]
            faceCorrectionVal = bboxCenterTracking(bboxSize) # and faceVal[0] > 0.65):
            output.append([faceID, faceDetectionVal, faceCorrectionVal, bboxSize])
        return output
    except:
        return "null"

#Converts location of bbox into difference between centerPOV.
# `faceCorrectionVal` values are >= 0, if inside centerPOV.
def bboxCenterTracking(bbox):
    try:
        faceCorrectionVal = []
        faceLeft = bbox[0] - 160
        faceUp = bbox[1] - 80
        faceRight = bbox[2] + bbox[0] - 480
        faceDown = bbox[3] + bbox[1] - 400
        faceCorrectionVal.append([faceLeft, faceUp, -faceRight, -faceDown])
        return faceCorrectionVal
    except:
        return "null"



known_faces, known_names = detectorFR.createFaceModel()
detectorFR.analyzeNewFaces(known_faces, known_names)


#Main loop
while True:
    #initCam
    cap.set(cv2.CAP_PROP_FPS,15)
    success, img = cap.read()
    centerPOV = img[80: 400,160: 480]
    imgFace, bboxs = detectorFM.findFaces(img)


    #displayCam
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0 , 0), 3)
    cv2.imshow("Image", img)
    cv2.imshow("Center", centerPOV)




    #End of loop
    key = cv2.waitKey(30)
    #Press ESC key to exit.
    if key == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
