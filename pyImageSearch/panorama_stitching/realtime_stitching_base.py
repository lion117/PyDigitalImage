#-*- coding: utf-8 -*-

import sys, os, time



from panorama import Stitcher
from imutils.video import VideoStream
import numpy as np
import datetime
import imutils
import time
import cv2


def originFunc():
    # initialize the video streams and allow them to warmup
    print("[INFO] starting cameras...")
    leftStream = VideoStream(src=1).start()
    rightStream = VideoStream(src=0).start()
    time.sleep(2.0)

    # number of frames read
    stitcher = Stitcher()
    total = 0

    # loop over frames from the video streams
    while True:
        # grab the frames from their respective video streams
        left = leftStream.read()
        right = rightStream.read()

        # resize the frames
        left = imutils.resize(left, width=400)
        right = imutils.resize(right, width=400)

        # stitch the frames together to form the panorama
        # IMPORTANT: you might have to change this line of code
        # depending on how your cameras are oriented; frames
        # should be supplied in left-to-right order
        result = stitcher.stitch([left, right])
        # no homograpy could be computed
        if result is None:
            print("[INFO] homography could not be computed")
            break

        # show the output images
        cv2.imshow("Result", result)
        cv2.imshow("Left Frame", left)
        cv2.imshow("Right Frame", right)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # do a bit of cleanup
    print("[INFO] cleaning up...")
    cv2.destroyAllWindows()
    leftStream.stop()
    rightStream.stop()



class MainRun():
    @classmethod
    def testCamera(cls):
        leftStream = VideoStream(src=0).start()
        rightStream = VideoStream(src=1).start()
        time.sleep(2.0)
        while True:
            left = leftStream.read()
            right = rightStream.read()
            # resize the frames
            # left = imutils.resize(left, width=400)
            # right = imutils.resize(right, width=400)
            cv2.imshow("Left Frame", left)
            cv2.imshow("Right Frame", right)
            key = cv2.waitKey(1)

        cv2.destroyAllWindows()
        leftStream.stop()
        rightStream.stop()


    @classmethod
    def testOriginFunc(cls):
        originFunc()


if __name__ == "__main__":
    print(os.getcwd())
    # MainRun.testCamera()
    MainRun.testOriginFunc()

