import cv2
import numpy as np

#def rot(img,x_theta,y_theta):
#    h,w = img.shape[:2]
#    rot_img = np.zeros([h*y_theta,w*x_theta],dtype=np.uint8)
#    for i in range(h):
#        for j in range(w):
#            #print(rot_img[i*y_theta][j*x_theta], img[i][j])
#            rot_img[i*y_theta][j*x_theta] = img[i][j]
#    return rot_img
#
#img = cv2.imread('./img_sample/img2.jpg',0)
#rot_img = rot(img,2,2)
#
#cv2.imwrite('./processed_img/img2_rot.jpg',rot_img)
#cv2.imshow('img',rot_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows(0)