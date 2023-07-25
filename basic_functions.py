import cv2 as cv

img = cv.imread("face.jpg")

cv.imshow("face", img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#blur an image
blur = cv.GaussianBlur(img, (99,99), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

#edge cascade (find edges in image)
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny edges", canny)
#you can also find edges by passing in the blur image

#dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow("Dilated", dilated)

#eroding
eroded = cv.erode(dilated, (9,9), iterations=1)
cv.imshow("eroded", eroded)

#resize an iamge
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resize)

#cropping
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)


cv.waitKey(0)