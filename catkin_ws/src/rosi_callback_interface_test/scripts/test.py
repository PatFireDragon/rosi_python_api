#!/usr/bin/env python

import rospy

import cv2 as cv
import cv_bridge as cv_b

import rosi_interface as ri

def tester():
    rospy.init_node('rosi_interface_tester', anonymous=True)

    rosi = ri.RosiInterface()

    @rosi.callback(ri.CALLBACK_UR5_TOOL_CAM)
    def show_camera_image(img):
        bridge = cv_b.CvBridge()
        cv_img = bridge.imgmsg_to_cv2(img)
        cv.imshow('img', cv_img)
        cv.waitKey(3)

    @rosi.callback(ri.CALLBACK_GPS)
    def print_gps_data(gps_data):
        rospy.loginfo(gps_data)


    @rosi.callback(ri.CALLBACK_TIME)
    def move_up_right_wheel_and_arm(t):
        rosi.publish(ri.PUBLISH_TRACTION_SPEED, 10, 10, 0, 0)
        rosi.publish(ri.PUBLISH_ARMS_SPEED, -0.52, -0.52, 0, 0)

    rospy.spin()


if __name__ == '__main__':
    try:
        tester()
        cv.destroyAllWindows()
    except rospy.ROSInterruptException:
        pass
