import cv2
import numpy as np

def cvt_to_binary(img,binary_threshold):
    img1 = np.where(img > binary_threshold,255,0)
    img2 = np.where(img1 < binary_threshold,0,img1)
    return img2

img_name = input('Input Image Name : ')
binary_threshold = int(input('Input Binary Threshold : '))
img = cv2.imread(f'./img_sample/{img_name}.jpg',0)
binary_img = cvt_to_binary(img,binary_threshold)
print(binary_img)

cv2.imwrite(f'./processed_img/{img_name}_binary.jpg',binary_img)
cv2.imshow('origin_img', binary_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
#when you control the two value in np.where function it will make errors.