import cv2
import numpy as np

def inverse_transform(img):
    inv_img = np.where(img >= 0, 255-img, img)
    return inv_img

img = cv2.imread('./img_sample/img2.jpg',0)
inv_img = inverse_transform(img)

cv2.imwrite('./processed_img/img2_inverse.jpg',inv_img)
cv2.imshow('img',inv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()