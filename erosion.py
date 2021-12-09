import cv2
import numpy as np

def cvt_to_binary(img,binary_threshold):
    img1 = np.where(img > binary_threshold,255,img)
    img2 = np.where(img1 < binary_threshold,0,img1)
    return img2

def erosion(binary_img):
    h,w = binary_img.shape[:2]
    erosion_img = np.zeros((h,w))
    for i in range(1,h-1):
        for j in range(1,w-1):
            sum = 0
            for row in range(3):
                for col in range(3):
                    sum += int(binary_img[i+row-1][j+col-1])
            if sum == 255*9:
                erosion_img[i][j] = 255
            else : 
                erosion_img[i][j] = 0
    return erosion_img

img = cv2.imread('./img_sample/img2.jpg',0)
binary_img = cvt_to_binary(img,90)
erosion_img = erosion(binary_img)

cv2.imwrite('./processed_img/img2_erosion.jpg',erosion_img)
cv2.imshow('img',erosion_img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)