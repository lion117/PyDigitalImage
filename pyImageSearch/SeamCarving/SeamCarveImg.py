# -*- coding: utf-8 -*-

import sys, os, time
from skimage import transform
from skimage import filters
import cv2



def carveImg(tImag, tType):
    if os.path.exists(tImag) is False:
        print(u"%s not found"%tImag)
        return

    # load the image and convert it to grayscale
    image = cv2.imread(tImag)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # compute the Sobel gradient magnitude representation
    # of the image -- this will serve as our "energy map"
    # input to the seam carving algorithm
    lTemp = filters.sobel(gray.astype("float"))

    # show the original image
    cv2.imshow("Original", image)
    cv2.imshow("temp", lTemp)

    # loop over a number of seams to remove
    for numSeams in range(10, 140, 5):
        # perform seam carving, removing the desired number
        # of frames from the image -- `vertical` cuts will
        # change the image width while `horizontal` cuts will
        # change the image height
        carved = transform.seam_carve(image, lTemp, tType,numSeams)
        print("[INFO] removing {} seams; new size: "
            "w={}, h={}".format(numSeams, carved.shape[1],
                carved.shape[0]))
        # show the output of the seam carving algorithm
        cv2.imshow("Carved", carved)
        cv2.waitKey(0)


class  MainTest():
    @staticmethod
    def testCarveImg():
        lImg = u"head.png"
        lType = u"horizontal"
        lTypeVetical = u"vertical"
        carveImg(lImg , tType=lTypeVetical)




if __name__ == "__main__":
    MainTest.testCarveImg()