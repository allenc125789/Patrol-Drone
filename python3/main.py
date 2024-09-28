import cv2
import camCapture-face-modules as fm
import camCapture-pose-modules as pm
import time

cap = cv2.VideoCapture(2)
pTime = 0
detectorFM = fm.faceDetector()
detectorPM = pm.poseDetector()




#def initBoot():
#    while True:


def saveFaceToFS(bboxs):
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
            print(faceCorrectionVal)
#            print("Face NOT detected")


def bboxCenterTracking(bbox):
    try:
        faceLeft = bbox[0] - 150
        faceUp = bbox[1] - 25
        faceRight = bbox[2] + bbox[0] - 500
        faceDown = bbox[3] + bbox[1] - 300

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
    centerPOV = img[25: 300,150: 500]
    img, bboxs = detectorFM.findFaces(img)
    faceCorrectionVal = []
#    if len(lmList) !=0:
#        print(lmList)

    saveFaceToFS(bboxs)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0 , 0), 3)
    cv2.imshow("Image", img)
    cv2.imshow("Center", centerPOV)

    cv2.waitKey(1)
