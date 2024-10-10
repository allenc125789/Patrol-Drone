# Modules for mediapipe's facial detection library. Function's are used to determine the position of a peron's face /
# on a video/image.

import cv2
import mediapipe as mp
import time


class faceDetector():
    def __init__(self, minDetectionCon= 0.5):

        self.minDetectionCon = minDetectionCon
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)

    def findFaces(self,img, draw= True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        bboxs = []

        if self.results.detections:
            for id,detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih) - 40, \
                       int(bboxC.width * iw), int(bboxC.height * ih) + 50
                bboxs.append([id, bbox, detection.score])
                cv2.rectangle(img,bbox,(255,0,255), 2)
                cv2.putText(img, f'{int(id)} [{int(detection.score[0] * 100)}%]', (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,255), 2)
        return img, bboxs

    def saveAdminFace(self, img, bbox, count):
        adminFolder = "/home/drone/Pictures/Faces/catologued/admin/"
        bboxX = bbox[0][3][0]
        bboxY = bbox[0][3][1]
        bboxW = bbox[0][3][2]
        bboxH = bbox[0][3][3]
        roi = img[bboxY:bboxY+bboxH, bboxX:bboxX+bboxW]
        adminPhoto = str(adminFolder) + str(count) + ".jpg"
        cv2.imwrite(adminPhoto, roi)


    #Determines pixel difference between faces and the centerPOV.
    def faceAutoCenter(self, bboxs):
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
            return False


#    def findFacePosition(self, img, draw= True):




def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = faceDetector()

    while True:
        success, img = cap.read()
        img, bboxs = detector.findFaces(img)
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.imshow("Image", img)
        cv2.waitKey(1)



if __name__ == "__main__":
    main()
