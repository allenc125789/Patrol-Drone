import cv2
import camCaptureFaceModules as fm
import camCapturePoseModules as pm
import time

cap = cv2.VideoCapture(0)
pTime = 0
detectorFM = fm.faceDetector()
detectorPM = pm.poseDetector()


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
