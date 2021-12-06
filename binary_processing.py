import cv2

#def cvt_to_gray(img,height,width,channel):
#    if channel == 3:
#        for i in range(height):
#            for j in range(width):
#                img[i][j] = int(img[i][j][0])*0.114 + int(img[i][j][1])*0.587 + int(img[i][j][2]*0.299)
#        return img
#    else:
#        return img

def cvt_to_binary(img,binary_threshold,height,width):
    for i in range(height):
        for j in range(width):
            if img[i][j] >= binary_threshold:
                img[i][j] = 1
            else :
                img[i][j] = 0
    return img

img_name = input('Input Image Name : ')
binary_threshold = int(input('Input Binary Threshold : '))
img = cv2.imread(f'./img_sample/{img_name}.jpg',0)
height,width = img.shape
#gray_img = cvt_to_gray(img,height,width,channel)
binary_img = cvt_to_binary(img,binary_threshold,height,width)

cv2.imwrite(f'./processed_img/{img_name}_binary.jpg',binary_img)
cv2.imshow('origin_img', binary_img)
cv2.waitKey(0)

print(img)
#img[i][j][0]*0.114 + img[i][j][1]*0.587 + img[i][j][2]*0.299 = intensity of 1 channel
#지금 흑백컨버트를 해도 1채널로 바뀌는게 아니라 모든 값이 같은 3채널 사진이 되어있다는게 문제임
cv2.destroyAllWindows()