import cv2
import numpy as np

def scale(img,x_scale,y_scale):
    h,w = img.shape[:2]
    scale_img = np.zeros([h*y_scale,w*x_scale],dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            #print(scale_img[i*y_scale][j*x_scale], img[i][j])
            scale_img[i*y_scale][j*x_scale] = img[i][j]
    return scale_img

img = cv2.imread('./img_sample/img2.jpg',0)
scale_img = scale(img,2,2)

cv2.imwrite('./processed_img/img2_scale.jpg',scale_img)
cv2.imshow('img',scale_img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)