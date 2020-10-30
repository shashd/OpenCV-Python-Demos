# -*- coding: utf-8 -*-

import cv2
import numpy as np
"""
Show color space and channel split
cv2.split, cv2.merge, cv2.cvtColor, cv2.inRange
"""

class ColorSpace(object):
    def __init__(self):
        self.in_path = "images/Lenna.jpg"
        self.out_path = "images/"

    def channel_split(self, img_src):
        """
        Split the picture by channels
        :return: Image data
        """

        # split channels
        b, g, r = cv2.split(img_src)
        cv2.imshow("blue", b)
        cv2.imshow("green", g)
        cv2.imshow("red", r)

        # reset part value
        changed_image = img_src.copy()
        changed_image[:, :, 2] = 0
        cv2.imshow("change", changed_image)

        # merge channels
        merge_image = cv2.merge([b, g, r])
        cv2.imshow("merge", merge_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def color_space_transfer(self, img_src):
        """
        Transfer to another color space
        :return: Image data
        """

        gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray", gray)

        hsv = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv", hsv)

        yuv = cv2.cvtColor(img_src, cv2.COLOR_BGR2YUV)
        cv2.imshow("yuv", yuv)

        ycrcb = cv2.cvtColor(img_src, cv2.COLOR_BGR2YCrCb)
        cv2.imshow("ycrcb", ycrcb)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def extract_color_from_video(self):
        """
        Extract the target color and replace it from video
        """
        lower_green = np.array([35, 43, 46])
        higher_green = np.array([77, 255, 255])

        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # replace the target color with white, and the rest black
            mask = cv2.inRange(hsv, lower_green, higher_green)
            cv2.imshow("video", frame)
            cv2.imshow("mask",mask)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def main(self):
        img_src = cv2.imread(self.in_path)
        self.channel_split(img_src)
        self.color_space_transfer(img_src)
        self.extract_color_from_video()

if __name__ == '__main__':
    cs = ColorSpace()
    cs.main()