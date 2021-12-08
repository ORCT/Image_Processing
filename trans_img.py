import cv2
import numpy as np

def trans(img,dx,dy):
    h,w = img.shape[:2]
    scale_img = np.zeros([h+dy,w+dx],dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            #print(scale_img[i*y_scale][j*x_scale], img[i][j])
            scale_img[i+dy][j+dx] = img[i][j]
    return scale_img

img = cv2.imread('./img_sample/img2.jpg',0)
trans_img = trans(img,100,100)

cv2.imwrite('./processed_img/img2_trans.jpg',trans_img)
cv2.imshow('img',trans_img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)