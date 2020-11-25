import cv2

img1 = cv2.imread("luna.jpg")
img2 = cv2.imread("Output/luna_o.png")

img1 = cv2.resize(img1, (380,380))
img2 = cv2.resize(img2, (380,380))

img3 = cv2.hconcat([img1,img2])

cv2.imshow("out",img3)
cv2.waitKey(0)

cv2.imwrite("test1.png",img3)