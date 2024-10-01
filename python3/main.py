import cv2
import camCaptureFaceModules as fm
import camCapturePoseModules as pm
import time

cap = cv2.VideoCapture(0)
pTime = 0
detectorFM = fm.faceDetector()
detectorPM = pm.poseDetector()


def initBoot():
    count = 0
    WAIT = False
    while True:
        try:
            #initCam
            cap.set(cv2.CAP_PROP_FPS,15)
            success, img = cap.read()
            centerPOV = img[80: 400,160: 480]
            imgFace, bboxs = detectorFM.findFaces(img)

            #First boot. Determines admin's face by selecting the most prevelant face.
            adminFolder = "/home/drone/Pictures/Faces/admin/"
            bbox = faceAutoCenter(bboxs)
            faceCorrectionVal = bbox[0][2][0]
            faceDetectionVal = bbox[0][1][0]
            bboxX = bbox[0][3][0]
            bboxY = bbox[0][3][1]
            bboxW = bbox[0][3][2]
            bboxH = bbox[0][3][3]
            totalPics = 120



            #If the 'admin's face is in the CenterPOV and has a value of <0.70%, it'll initiate...something...
            if (all(i > 0 for i in faceCorrectionVal) and faceDetectionVal > 0.70):
                roi = img[bboxY:bboxY+bboxH, bboxX:bboxX+bboxW]
                adminPhoto = str(adminFolder) + str(count) + ".jpg"
                cv2.imwrite(adminPhoto, roi)
                count += 1
                print(count)
            else:
                print(faceCorrectionVal, faceDetectionVal)
#            if (count == 0):
#                print("Look Forward")
#            if (count == totalPics / 3):
#                print("Look Left")
#            if (count == (totalPics / 3) * 2):
#                print("Look Right")
            if (count == totalPics):
                break
        except:
            print("No faces detected.")

def confirmFacePose(centerPOV):
    try:
        centerPOV = detectorPM.findPose(centerPOV)
        lmList = detectorPM.findPosition(centerPOV)
        if len(lmList) !=0:
            rightEar = lmList[8]
            rightEyeO = lmList[6]
            rightEye = lmList[5]
            rightEyeI = lmList[4]
            leftEar = lmList[7]
            leftEyeO = lmList[3]
            leftEye = lmList[2]
            leftEyeI = lmList[1]
        #Detect looking forward.
        if rightEar[1] < rightEyeO[1] and leftEar[1] > leftEyeO[1]:
            print(rightEar[1] / rightEyeO[1])
            return "faceForward"
        #Detect looking right.
        if rightEar[1] > rightEye[1]:
            print("Looking right!")
            return "faceRight"
        #Detect looking left.
        if leftEar[1] < leftEye[1]:
            print("Looking left!")
            return "faceLeft"
        else:
            return False
    except:
        print("Can't estmate pose")

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


#initBoot()

#Main loop
while True:
    #initCam
    cap.set(cv2.CAP_PROP_FPS,15)
    success, img = cap.read()
    centerPOV = img[80: 400,160: 480]
    imgFace, bboxs = detectorFM.findFaces(img)

    confirmFacePose(centerPOV)

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
