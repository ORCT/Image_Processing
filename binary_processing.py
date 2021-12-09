import cv2
import numpy as np

def cvt_to_binary(img,binary_threshold):
    img1 = np.where(img > binary_threshold,255,img)
    img2 = np.where(img1 < binary_threshold,0,img1)
    return img2

img = cv2.imread('./img_sample/img0.jpg',0)
binary_img = cvt_to_binary(img,100)
print(binary_img)

cv2.imwrite('./processed_img/img0_binary.jpg',binary_img)
cv2.imshow('origin_img', binary_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
#when you control the two value in np.where function it will make errors.