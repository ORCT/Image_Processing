import cv2
import numpy as np

def k_nearest_neighbor_filter(n,img):
    h,w = img.shape[:2]
    img1 = img
    for i in range(1,h-1):
        for j in range(1,w-1):
            values = [img[i-1][j-1],img[i][j-1],img[i+1][j-1],img[i-1][j],img[i][j],img[i+1][j],img[i-1][j+1],img[i][j+1],img[i+1][j+1]]
            tmp = {0:abs(int(img[i-1][j-1])-int(img[i][j])),1:abs(int(img[i][j-1])-int(img[i][j])),2:abs(int(img[i+1][j-1])-int(img[i][j])),3:abs(int(img[i-1][j])-int(img[i][j])),4:abs(int(img[i][j])-int(img[i][j])),5:abs(int(img[i+1][j])-int(img[i][j])),6:abs(int(img[i-1][j+1])-int(img[i][j])),7:abs(int(img[i][j+1])-int(img[i][j])),8:abs(int(img[i+1][j+1])-int(img[i][j]))}
            tmp1 = sorted(tmp.items(), key=lambda x: x[1])
            tmp2 = 0
            for i in range(n):
                tmp2 += values[tmp1[i][0]]
            #print(img1[i][j], tmp2/n)
            img1[i][j] = tmp2/n
    return img1

img = cv2.imread('./img_sample/img2.jpg',0)
k_nearest_neighbor_img = k_nearest_neighbor_filter(4,img)
cv2.imwrite('./processed_img/img2_k_nearest_neighbor.jpg',k_nearest_neighbor_img)
cv2.imshow('img',k_nearest_neighbor_img)
cv2.waitKey(0)
cv2.destroyAllWindows()