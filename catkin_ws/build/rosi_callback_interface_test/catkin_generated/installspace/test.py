#!/usr/bin/env python2

from __future__ import print_function

import rospy

import numpy as np
import cv2 as cv
import cv_bridge as cv_b

from rosi_interface import RosiInterface

def tester():
    rospy.init_node('rosi_interface_tester', anonymous=True)

    rosi = RosiInterface()

    @rosi.data(CALLBACK_UR5_TOOL_CAM)
    def show_image(img):
        bridge = cv_b.CvBridge()
        cv_img = bridge.imgmsg_to_cv2(img)
        cv.imshow('img', cv_img)
        cv.waitKey(3)

    rosi.publish(PUBLISH_TRACTION_SPEED, 10, 10, 0, 0)

    rospy.spin()


if __name__ == '__main__':
    try:
        tester()
        cv.destroyAllWindows()
    except rospy.ROSInterruptException:
        pass
