# -*- coding: utf-8 -*-
import cv2

"""
This demo shows how cv2 read image and output image
key words: cv2.read(), cv2.imwrite(),cv2.imshow(),cv2.VideoCapture(),cv2.cvtColor()
"""


class IoDemo(object):

    def __init__(self):
        self.in_path = "../images/Lenna.jpg"
        self.out_path = "../images/"
        self.video_path = "../video/Crystal.mp4"
        self.video_save_path = "../video/temp.avi"

    def read_image(self):
        """
        Read image from in_path
        :return: Image Data
        """
        print("read image")
        src = cv2.imread(self.in_path)
        return src

    def get_pic_info(self, img_src):
        """
        Get picture information
        :return: None
        """
        print("Data Type：", type(img_src))
        print("(Height,Width,Panels)", img_src.shape)
        print("Pixel number", img_src.size)
        print("Pixel type：", img_src.dtype)

    def write_image(self, img_name, img_src):
        """
        Write image to out_path
        img_name: Image name
        img_src: Image data
        :return: None
        """
        cv2.imwrite(img_name, img_src)

    def show_image(self, img_name, img_src):
        """
        Show image
        img_name: Image name
        img_src: Image data
        :return: None
        """

        cv2.imshow(img_name, img_src)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def get_picture_from_camera(self):
        """
        Get frames from camera
        """
        # parameter: camera id
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow("video", frame)
            # cv2.waitKey(0) & 0xFF, get first frame
            # turn on camera until input 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def get_picture_from_video(self):
        """
        Get frames from video
        """
        cap = cv2.VideoCapture(self.video_path)
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Cannot read the video")
                break
            cv2.imshow("frame", frame)
            if cv2.waitKey(1000) & 0xFF == ord('q'):
                break
        # release resources
        cap.release()
        cv2.destroyAllWindows()

    def save_video(self):
        """
        Save video from camera
        """
        cap = cv2.VideoCapture(0)
        # define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter(self.video_save_path, fourcc, 20.0, (640, 480))
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # release resources
        cap.release()
        out.release()
        cv2.destroyAllWindows()

    def get_gray_img(self, img_src):
        """
        Turn img to grey
        :param img_src: Image Data
        :return: Gray Image Data
        """
        return cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

    def main(self):

        # video part
        # self.get_picture_from_camera()
        self.save_video()

        # picture
        # src = self.read_image()
        # self.get_pic_info(src)
        # self.show_image("Lenna",src)


if __name__ == '__main__':
    io = IoDemo()
    io.main()
