# -*- coding: utf-8 -*-

import cv2
import numpy as np

class Arithmetic(object):

    def add_demo(self,img1,img2):
        dst = cv2.add(img1,img2)
        cv2.imshow("add_demo",dst)

    def subtract_demo(self,img1,img2):
        dst = cv2.subtract(img1,img2)
        cv2.imshow("subtract_demo",dst)

    def divide_demo(self,img1,img2):
        dst = cv2.divide(img1,img2)
        cv2.imshow("divide_demo",dst)

    def multiply_demo(self,img1,img2):
        dst = cv2.multiply(img1,img2)
        cv2.imshow("multiply_demo",dst)

    def logic_demo(self):
        img_src = cv2.imread("../images/Lenna.jpg")
        cv2.imshow("image",img_src)
        dst = cv2.bitwise_not(img_src)
        cv2.imshow("logic_demo",dst)

    def contrast_brightness_demo(self,img_src,alpha,beta):
        h,w,ch = img_src.shape
        blank = np.zeros([h,w,ch],img_src.dtype)

        dst = cv2.addWeighted(img_src,alpha,blank,1-alpha,beta)
        cv2.imshow("contrast_brightness_demo",dst)

    def mean_variance(self,v1,v2):
        res1 = cv2.mean(v1)
        res2 = cv2.mean(v2)
        print(res1)
        print(res2)
        mean1, dev1 = cv2.meanStdDev(v1)
        # print("mean: " + mean1 + ",dev:" + dev1)

    def main(self):
        """Main process"""
        img_src1 = cv2.imread("../images/linux.jpg")
        img_src2 = cv2.imread("../images/windows.jpg")

        print(img_src1.shape)
        print(img_src2.shape)

        cv2.namedWindow("image1",cv2.WINDOW_AUTOSIZE)
        cv2.imshow("image1",img_src1)
        cv2.imshow("image2",img_src2)

        self.add_demo(img_src1, img_src2)
        self.subtract_demo(img_src1, img_src2)
        self.divide_demo(img_src1, img_src2)
        self.multiply_demo(img_src1,img_src2)
        self.mean_variance(img_src1, img_src2)

        temp_src = cv2.imread("../images/Lenna.jpg")
        self.contrast_brightness_demo(temp_src, 1.3, 80)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    arithmetic = Arithmetic()
    arithmetic.main()