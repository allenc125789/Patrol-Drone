import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

def getDirs(dir_path):
    res = []
    for path in os.listdir(dir_path):
        if not os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    return(res)

faceDATADIR = "/home/drone/Pictures/Faces"
faceCATEGORIES = getDirs(faceDATADIR)

for category in faceCATEGORIES:
    path = os.path.join(faceDATADIR, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GREYSCALE)
        plt.imshow(img_array, cmap="gray")
        plt.show()
        break
    break
