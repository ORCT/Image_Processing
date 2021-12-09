import cv2
import numpy as np

def sobel(img):
    h,w = img.shape[:2]
    sobel_img = np.zeros((h,w))
    mask1 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    #mask1 = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
    mask2 = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
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
            sobel_img[row+1][col+1] = sum
    return sobel_img

img = cv2.imread('./img_sample/img2.jpg',0)
sobel_img = sobel(img)

cv2.imwrite('./processed_img/img2_sobel.jpg',sobel_img)
cv2.imshow('img',sobel_img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)