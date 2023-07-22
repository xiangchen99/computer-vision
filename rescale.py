import cv2 as cv

#rescale iamge
"""img = cv.imread("face.jpg")

def rescaleFrame(frame, scale=0.1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.imshow("face", rescaleFrame(img))"""



capture = cv.VideoCapture(0)


while True:
    isTrue, frame = capture.read()
    
    #resize video frame
    resized = cv.resize(frame, (1920, 1080))
    
    cv.imshow("Video", resized)
    
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()
    
cv.waitKey(0)