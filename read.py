import cv2 as cv

#takes an image and return as pixels
img = cv.imread('face.jpg')

#capture video: path for video, numbers for webcam
capture = cv.VideoCapture(0)

#reads video frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)
    
    #if key d is pressed then video stops
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()

#displays the image in new window
#cv.imshow('Face', img)

#waits (time) until a key is pressed
#cv.waitKey(0)