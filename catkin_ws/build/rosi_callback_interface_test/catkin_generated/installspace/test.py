#!/usr/bin/env python2

from __future__ import print_function

import rospy
import numpy as np
import cv2 as cv
import cv_bridge as cv_b

from rosi_callback_interface import RosiCallbackInterface

def tester():
    rospy.init_node('rosi_callback_interface_tester', anonymous=True)

    rosi = RosiCallbackInterface()

    @rosi.data('ur5toolCam')
    def show_image(img):
        bridge = cv_b.CvBridge()
        cv_img = bridge.imgmsg_to_cv2(img)
        cv.imshow('img', cv_img)
        cv.waitKey(3)

    rospy.spin()


if __name__ == '__main__':
    try:
        tester()
        cv.destroyAllWindows()
    except rospy.ROSInterruptException:
        pass
