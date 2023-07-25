import cv2 as cv

import numpy as np

#height, width, and color channel
blank = np.zeros((500,500, 3), dtype="uint8")

cv.imshow("blank", blank)

#paint the image a certain color
blank[:] = 0,255,0
cv.imshow("green", blank)

#draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,255), thickness=cv.FILLED)
cv.imshow("rectangle", blank)

#draw circle
cv.circle(blank, (250,250), 50, (255,0,0), 120)
cv.imshow("circle", blank)

#draw line
cv.line(blank, (0,0), (255,255), (255,255,0), 5)
cv.imshow("line", blank)

#write text on image
cv.putText(blank, "Hello", (255,255), cv.FONT_HERSHEY_COMPLEX, 5, (255,255,0), 5)
cv.imshow("text", blank)

cv.waitKey(0)