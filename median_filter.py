import cv2
import numpy as np

def median_filter(img):
    h,w = img.shape[:2]
    img1 = img
    for i in range(1,h-1):
        for j in range(1,w-1):
            values = [img[i-1][j-1],img[i][j-1],img[i+1][j-1],img[i-1][j],img[i][j],img[i+1][j],img[i-1][j+1],img[i][j+1],img[i+1][j+1]]
            values.sort()
            img1[i][j] = values[4]
    return img1

img = cv2.imread('./img_sample/img2.jpg',0)
median_img = median_filter(img)
cv2.imwrite('./processed_img/img2_median.jpg',median_img)
cv2.imshow('img',median_img)
cv2.waitKey(0)
cv2.destroyAllWindows()