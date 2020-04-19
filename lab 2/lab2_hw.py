import cv2
import numpy as np

cap = cv2.VideoCapture('paper_small.mp4')

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

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
grayMedianFrame = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)

ret = True
while ret:
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    median_dframe = cv2.absdiff(img, grayMedianFrame)
    th_median, median_dframe = cv2.threshold(median_dframe, 110, 255, cv2.THRESH_BINARY)

    corners = cv2.goodFeaturesToTrack(median_dframe, 10, .8, 300)
    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

    cv2.imshow('good corners', img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
