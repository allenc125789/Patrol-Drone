import cv2
import mediapipe as mp
import time


class poseDetector():

    def __init__(self, mode=False, upBody=True, smooth=True, detectionCon=True, trackCon=0.4):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon


        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.upBody,self.smooth,self.detectionCon,self.trackCon)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c, = img.shape
                cx, cy, = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return lmList

    def confirmFacePose(self, img):
        try:
            centerPOV = self.findPose(img)
            lmList = self.findPosition(img)
            if len(lmList) !=0:
                #Face
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
                return "faceForward"
            #Detect looking right.
            if rightEar[1] > rightEye[1]:
                return "faceRight"
            #Detect looking left.
            if leftEar[1] < leftEye[1]:
                return "faceLeft"
            else:
                return False
        except:
            return False



def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img)
        print(lmList)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0 , 0), 3)
        cv2.imshow("Image", img)

        cv2.waitKey(1)


if __name__ == "__main__":
    main()
