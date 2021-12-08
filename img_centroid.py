import cv2
import numpy as np

def cvt_to_binary(img,binary_threshold):
    img1 = np.where(img > binary_threshold,255,img)
    img2 = np.where(img1 < binary_threshold,0,img1)
    return img2

def get_centroid(binary_img):
    h,w = binary_img.shape[:2]
    x=[]
    y=[]
    for i in range(h):
        for j in range(w):
            if binary_img[i][j] == 255:
                y.append(i)
                x.append(j)
    x_cen = sum(x)/len(x)
    y_cen = sum(y)/len(x)
    point = (x_cen,y_cen)
    return point

def draw_centroid(img,center_point):
    cv2.circle(img, center=tuple(np.int0(center_point)), radius=5, color=(255, 255, 0), thickness=4)

img = cv2.imread('./img_sample/img1.jpg',0)
binary_img = cvt_to_binary(img,90)
centroid = get_centroid(binary_img)
#print(centroid)
tmp = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
draw_centroid(img,centroid)

cv2.imwrite('./processed_img/img1_centroid.jpg', img)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()