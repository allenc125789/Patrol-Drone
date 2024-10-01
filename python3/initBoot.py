import cv2
import camCaptureFaceModules as fm
import camCapturePoseModules as pm
import time

cap = cv2.VideoCapture(0)
pTime = 0
detectorFM = fm.faceDetector()
detectorPM = pm.poseDetector()

def saveAdminFace(img, bbox, count):
            adminFolder = "/home/drone/Pictures/Faces/admin/"
            bboxX = bbox[0][3][0]
            bboxY = bbox[0][3][1]
            bboxW = bbox[0][3][2]
            bboxH = bbox[0][3][3]
            roi = img[bboxY:bboxY+bboxH, bboxX:bboxX+bboxW]
            adminPhoto = str(adminFolder) + str(count) + ".jpg"
            cv2.imwrite(adminPhoto, roi)


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


while True:
    #initCam
    cap.set(cv2.CAP_PROP_FPS,15)
    success, img = cap.read()
    centerPOV = img[80: 400,160: 480]
    imgFace, bboxs = detectorFM.findFaces(img)

    #First boot. Determines admin's face by selecting the most prevelant face.
    facePose = detectorPM.confirmFacePose(centerPOV)
    bbox = detectorFM.faceAutoCenter(bboxs)
    faceCorrectionVal = bbox[0][2][0]
    faceDetectionVal = bbox[0][1][0]
    #Keep a multiple of 3 to split evenly between face poses.
    totalPics = 120
    count = 0

    #If the 'admin's face is in the CenterPOV and has a value of <0.70%, it'll initiate...something...
    print(count)
    if (count <= totalPics / 3 and facePose == "faceForward"):
        print("Look Forward")
        print(facePose)
        saveAdminFace(img, bbox, count)
        count += 1
    elif (all(i < 0 for i in faceCorrectionVal) and faceDetectionVal < 0.70):
        continue
    elif (count >= totalPics / 3 and count < (totalPics / 3) * 2 and facePose == "faceLeft"):
        print("Look Left")
        print(facePose)
        saveAdminFace(img, bbox, count)
        count += 1
    elif (count >= (totalPics / 3) * 2 and facePose == "faceRight"):
        print("Look Right")
        print(facePose)
        saveAdminFace(img, bbox, count)
        count += 1
    elif facePose == False:
        print("rip")
    if (count == totalPics):
        break
    #End of loop
    key = cv2.waitKey(30)
    #Press ESC key to exit.
    if key == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
