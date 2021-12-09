import cv2
import numpy as np
import math

def rot(img,theta):
    h,w = img.shape[:2]
    if h >= w:
        rot_img = np.zeros([h,h],dtype=np.uint8)
    else :
        rot_img = np.zeros([w,w],dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            rot_img[int(j*math.sin(theta*2*math.pi/360)+i*math.cos(theta*2*math.pi/360))][int(j*math.cos(theta*2*math.pi/360)-i*math.sin(theta*2*math.pi/360))] = img[i][j]
    return rot_img

img = cv2.imread('./img_sample/img2.jpg',0)
rot_img = rot(img,90)

cv2.imwrite('./processed_img/img2_rot.jpg',rot_img)
cv2.imshow('img',rot_img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)