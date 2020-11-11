# -*- coding: utf-8 -*-

import cv2
import numpy as np
"""
Show different methods to change movements to the image
cv2.flip, cv2.resize, cv2.warpAffine, cv2.getRotationMatrix2D, cv2.getAffineTransform, cv2.getPerspectiveTransform,
cv2.warpPerspective
"""


class PerspectiveTransform(object):

    def __init__(self):

        self.img_path = "../images/Lenna.jpg"
        self.img_src = None
        self.h = None
        self.w = None

    def read_image(self):
        """
        Read image from in_path
        :return: Image Data
        """
        print("read image")
        self.img_src = cv2.imread(self.img_path)

    def show_origin(self):
        """
        Show origin image
        """
        cv2.imshow("origin",self.img_src)

    def flip(self):
        """
        Flip the image
        1: flip by y
        0: flip by x
        -1: flip by x and y
        """
        flip1 = cv2.flip(self.img_src,1)
        flip2 = cv2.flip(self.img_src,0)
        flip3 = cv2.flip(self.img_src,-1)

        cv2.imshow("flip1",flip1)
        cv2.imshow("flip2",flip2)
        cv2.imshow("flip3",flip3)


    def resize(self):
        """
        Resize the image
        """
        # method 1: use fx and fy, fx and fy are rescale factors
        res = cv2.resize(self.img_src, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

        # method 2: set new height and new weight
        # n_h, n_w = 2 * self.h, 2 * self.w
        # res = cv2.resize(self.img_src,(2*n_w,2*n_h),interpolation=cv2.INTER_CUBIC)

        cv2.imshow("resize",res)


    def move(self):
        """
        Show moved image
        M: 2×3 transformation matrix.
        """
        # x move 100 and y move 50
        M = np.float32([[1, 0, 100], [0, 1, 50]])
        dst = cv2.warpAffine(self.img_src, M, (self.w, self.h))
        cv2.imshow('move', dst)

    def rotation(self):
        """
        Rotate the image
        """
        # anticlockwise rotate 90 degrees
        M = cv2.getRotationMatrix2D((self.w / 2, self.h / 2), 90, 1)
        dst = cv2.warpAffine(self.img_src, M, (self.w, self.h))
        cv2.imshow('rotation', dst)


    def affine(self):
        """
        Affine transform the image
        """
        pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
        pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
        M = cv2.getAffineTransform(pts1, pts2)
        dst = cv2.warpAffine(self.img_src, M, (self.w, self.h))
        cv2.imshow("affine",dst)

    def perspective_transform(self):
        """
        Perspective transform the image
        """
        # the points before transform and after the transform
        pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
        pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(self.img_src, M, (300, 300))
        cv2.imshow("perspective_transform",dst)

    def main(self):
        self.read_image()
        self.h, self.w = self.img_src.shape[:-1]
        self.show_origin()
        # self.flip()
        self.resize()
        self.move()
        self.rotation()
        self.affine()
        self.perspective_transform()

        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    pt = PerspectiveTransform()
    pt.main()