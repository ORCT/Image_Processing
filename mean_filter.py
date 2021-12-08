import cv2
import numpy as np

def mean_filter(img):
    h,w = img.shape[:2]
    img1 = img
    for i in range(1,h-1):
        for j in range(1,w-1):
            img1[i][j] = (int(img[i-1][j-1])+int(img[i][j-1])+int(img[i+1][j-1])+int(img[i-1][j])+int(img[i][j])+int(img[i+1][j])+int(img[i-1][j+1])+int(img[i][j+1])+int(img[i+1][j+1]))/9
    return img1

img = cv2.imread('./img_sample/img2.jpg',0)
mean_img = mean_filter(img)
cv2.imwrite('./processed_img/img2_mean.jpg',mean_img)
cv2.imshow('img',mean_img)
cv2.waitKey(0)
cv2.destroyAllWindows()