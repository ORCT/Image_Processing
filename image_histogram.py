import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram(img):#use counting sort 
    h,w = img.shape[:2]
    cnt = np.array([0 for i in range(256)])
    for i in range(h):
        for j in range(w):
            cnt[int(img[i][j])] += 1
    return cnt

img = cv2.imread('./img_sample/img0.jpg',0)
print(img)
img_hist = histogram(img)
x = np.arange(256)
y = img_hist
print(img_hist)
plt.bar(x, y)
plt.show()