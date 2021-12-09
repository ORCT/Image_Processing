import cv2
import numpy as np

def prewitt(img):
    h,w = img.shape[:2]
    prewitt_img = np.zeros((h,w))
    mask1 = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    mask2 = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    for row in range(h-3):
        for col in range(w-3):
            center_value1=0
            center_value2=0
            sum=0
            for i in range(3):
                for j in range(3):
                    center_value1 += int(img[i+row][j+col])*mask1[i][j]
                    center_value2 += int(img[i+row][j+col])*mask2[i][j]
            sum = abs(center_value1)+abs(center_value2)
            if sum > 255 : sum = 255
            prewitt_img[row+1][col+1] = sum
    return prewitt_img

img = cv2.imread('./img_sample/img2.jpg',0)
prewitt_img = prewitt(img)

cv2.imwrite('./processed_img/img2_prewitt.jpg',prewitt_img)
cv2.imshow('img',prewitt_img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)