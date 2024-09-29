import cv2
import camCaptureFaceModules as fm
import camCapturePoseModules as pm
import time

cap = cv2.VideoCapture(0)
pTime = 0
detectorFM = fm.faceDetector()
detectorPM = pm.poseDetector()




#def initBoot():
#    while True:


def faceAutoCenter(bboxs):
    for i in bboxs:
        bbox = i[1]
        faceVal = i[2]
        if faceVal is None:
            faceVal = 0
        elif (bboxCenterTracking(bbox) and faceVal[0] > 0.65):
            print("Ready to Save")
#            centerPOV = detectorPM.findPose(centerPOV)
#            lmList = detectorPM.findPosition(centerPOV)
#            if len(lmList) !=0:
#                print(lmList)
        else:
            print(faceCorrectionVal, faceVal)
#            return faceVal, faceCorrectionVal
#            print("Face NOT detected")


def bboxCenterTracking(bbox):
    try:
        faceLeft = bbox[0] - 160
        faceUp = bbox[1] - 80
        faceRight = bbox[2] + bbox[0] - 480
        faceDown = bbox[3] + bbox[1] - 400

        if faceLeft < 0 or faceUp < 0 or -faceRight < 0 or -faceDown < 0:
            faceCorrectionVal.append([faceLeft, faceUp, -faceRight, -faceDown])
            return False
        else:
            return True
    except:
        print("No matching bbox value in bboxParse()")

#Main loop
while True:
    cap.set(cv2.CAP_PROP_FPS,15)
    success, img = cap.read()
    centerPOV = img[80: 400,160: 480]
    img, bboxs = detectorFM.findFaces(img)
    faceCorrectionVal = []
#    if len(lmList) !=0:
#        print(lmList)

    faceAutoCenter(bboxs)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0 , 0), 3)
    cv2.imshow("Image", img)
    cv2.imshow("Center", centerPOV)

    cv2.waitKey(1)
