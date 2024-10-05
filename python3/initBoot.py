import cv2
import camCaptureFaceModules as fm
import camCapturePoseModules as pm
import time

cap = cv2.VideoCapture(0)
pTime = 0
detectorFM = fm.faceDetector()
detectorPM = pm.poseDetector()


def setAdminFace():
    count = 0
    WAIT = False
    while True:
        #initCam
        cap.set(cv2.CAP_PROP_FPS,15)
        success, img = cap.read()
        centerPOV = img[80: 400,160: 480]
        imgFace, bboxs = detectorFM.findFaces(img)

        #First boot. Determines admin's face by selecting the most prevelant face.
        facePose = detectorPM.confirmFacePose(centerPOV)
        bbox = faceAutoCenter(bboxs)
        faceCorrectionVal = bbox[0][2][0]
        faceDetectionVal = bbox[0][1][0]
        #Keep a multiple of 3 to split evenly between face poses.
        totalPics = 120

        print(faceCorrectionVal, faceDetectionVal)
        #If the 'admin's face is in the CenterPOV and has a value of <0.70%, it'll print.
        if (all(i > 0 for i in faceCorrectionVal) and faceDetectionVal > 0.70):
            #<= Facing Forward, 1/3 of totalPics
            if (count <= totalPics / 3 and facePose == "faceForward"):
                print("Look Forward")
                print(facePose)
                detectorFM.saveAdminFace(img, bbox, count)
                count += 1
            #<= Facing Left, 2/3 of totalPics
            elif (count >= totalPics / 3 and count < (totalPics / 3) * 2 and facePose == "faceLeft"):
                print("Look Left")
                print(facePose)
                detectorFM.saveAdminFace(img, bbox, count)
                count += 1
            #<= Facing Right, 3/3 of totalPics
            elif (count >= (totalPics / 3) * 2 and facePose == "faceRight"):
                print("Look Right")
                print(facePose)
                detectorFM.saveAdminFace(img, bbox, count)
                count += 1
            #If all pictures taken.
            if (count == totalPics):
                break
        else:
            continue



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



#Main loop
while True:
    #initCam
    setAdminFace()

    #End of loop
    cap.release()
    cv2.destroyAllWindows()
    break
