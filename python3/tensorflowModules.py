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
print(faceCATEGORIES)
