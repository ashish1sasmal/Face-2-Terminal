
import cv2

img = cv2.imread("luna.jpg",0)



img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)[1]


cv2.imshow("out",img)
cv2.waitKey(0)

img = cv2.resize(img,(230,100))
w,h = img.shape
for i in range(w):
	for j in range(h):
		if img[i,j]==0:
			print(" ",end="")
		else:
			print("*",end="")
	print()

