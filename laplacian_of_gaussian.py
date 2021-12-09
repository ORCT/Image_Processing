import cv2
import numpy as np

def LoG(img):
    h,w = img.shape[:2]
    LoG_img = np.zeros((h,w))
    mask1 = np.array([[0,0,-1,0,0],[0,-1,-2,-1,0],[-1,-2,16,-2,-1],[0,-1,-2,-1,0],[0,0,-1,0,0]])
    mask2 = np.array([[0,0,-1,0,0],[0,-1,-2,-1,0],[-1,-2,16,-2,-1],[0,-1,-2,-1,0],[0,0,-1,0,0]])
    for row in range(h-5):
        for col in range(w-5):
            center_value1=0
            center_value2=0
            sum=0
            for i in range(5):
                for j in range(5):
                    center_value1 += int(img[i+row][j+col])*mask1[i][j]
                    center_value2 += int(img[i+row][j+col])*mask2[i][j]
            sum = abs(center_value1)+abs(center_value2)
            if sum > 255 : sum = 255
            LoG_img[row+1][col+1] = sum
    return LoG_img

img = cv2.imread('./img_sample/img2.jpg',0)
LoG_img = LoG(img)

cv2.imwrite('./processed_img/img2_LoG.jpg',LoG_img)
cv2.imshow('img',LoG_img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)