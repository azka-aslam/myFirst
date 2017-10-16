import cv2
image = cv2.imread("pic.jpg")
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("over the clouds", image)
cv2.imshow("over the clouds-gray",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()