import cv2

def cvt_to_gray(img):
    height,width,channel = img.shape
    if channel == 3:
        for i in range(height):
            for j in range(width):
                img[i][j] = img[i][j][0]*0.114 + img[i][j][1]*0.587 + img[i][j][2]*0.299
        return img
    else:
        return img
    
img = cv2.imread('./img_sample/img0.jpg')
gray_img = cvt_to_gray(img)

cv2.imwrite('./processed_img/img0_gray.jpg', gray_img)
cv2.imshow('gray_img', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#print(img)
#img[i][j][0]*0.114 + img[i][j][1]*0.587 + img[i][j][2]*0.299 = intensity of 1 channel