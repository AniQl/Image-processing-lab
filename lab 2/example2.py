from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse

source_window = 'Input image'
corners_window = 'Detected corners'
max_thresh = 255


def demo(val):
    thresh = val

    # detector parameters
    blockSize = 2
    apertureSize = 3
    k = 0.04

    # corners detection
    # TODO  What is a dst result of the function cornerHarris?
    dst = cv.cornerHarris(src_gray, blockSize, apertureSize, k)

    # Normalzation
    dst_norm = np.empty(dst.shape, dtype=np.float32)
    cv.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
    dst_norm_scaled = cv.convertScaleAbs(dst_norm)

    # Drawing a crircles around corners
    for i in range(dst_norm.shape[0]):
        for j in range(dst_norm.shape[1]):
            if int(dst_norm[i, j]) > thresh:
                cv.circle(dst_norm_scaled, (j, i), 5, (0), 2)

    # Displaying the results
    cv.namedWindow(corners_window)
    cv.imshow(corners_window, dst_norm_scaled)

cap = cv.VideoCapture('paper.mp4')
ret = True
while ret:
    ret, frame = cap.read()
    for img in frame:
        # Input image reading
        #src = cv.imread('building.jpg')
        #if src is None:
            #print('Nie można wczytać obrazka:', args.input)
            #exit(0)

        src_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Creating the window with trackbar
        cv.namedWindow(source_window)
        thresh = 200  # initial value of threshold
        cv.createTrackbar('Prog: ', source_window, thresh, max_thresh, demo)
        cv.imshow(source_window, frame)
        demo(thresh)
        cv.waitKey()