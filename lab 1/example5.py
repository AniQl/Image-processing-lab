import cv2 as cv

# MOG2
# backSub = cv.createBackgroundSubtractorMOG2()

# KNN
# backSub = cv.createBackgroundSubtractorKNN()

# AVG
backSub = cv.createBackgroundSubtractorMOG2(history=120, varThreshold=50, detectShadows=True)

backSub2 = cv.createBackgroundSubtractorMOG2()

cap = cv.VideoCapture('Highway.mp4')
if not cap.isOpened:
    print('Unable to open file')
    exit(0)

while True:
    ret, frame = cap.read()

    if ret is True:

        fgMask = backSub.apply(frame)
        fgMask2 = backSub2.apply(frame)

        cv.imshow('Frame', fgMask2)
        cv.imshow('FG Mask', fgMask)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break


    else:
        break

cap.release()
# Closes all frames
cv.destroyAllWindows()