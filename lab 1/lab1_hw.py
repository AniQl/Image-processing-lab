import numpy as np
import cv2

cap = cv2.VideoCapture('Highway.mp4')
if not cap.isOpened:
    print('Unable to open file')
    exit(0)

frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)

frames = []
for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)

medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
averageFrame = np.average(frames, axis=0).astype(dtype=np.uint8)

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
grayMedianFrame = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)
grayAverageFrame = cv2.cvtColor(averageFrame, cv2.COLOR_BGR2GRAY)

ret = True
while ret:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    median_dframe = cv2.absdiff(frame, grayMedianFrame)
    average_dframe = cv2.absdiff(frame, grayAverageFrame)
    th_median, median_dframe = cv2.threshold(median_dframe, 30, 255, cv2.THRESH_BINARY)
    th_average, average_dframe = cv2.threshold(average_dframe, 30, 255, cv2.THRESH_BINARY)

    cv2.imshow('average frame', average_dframe)
    cv2.imshow('median frame', median_dframe)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
