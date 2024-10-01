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

def saveAdminFace(img, bbox, count):
            adminFolder = "/home/drone/Pictures/Faces/admin/"
            bboxX = bbox[0][3][0]
            bboxY = bbox[0][3][1]
            bboxW = bbox[0][3][2]
            bboxH = bbox[0][3][3]
            roi = img[bboxY:bboxY+bboxH, bboxX:bboxX+bboxW]
            adminPhoto = str(adminFolder) + str(count) + ".jpg"
            cv2.imwrite(adminPhoto, roi)






initBoot()

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
